# -*- coding: utf-8 -*-
"""
geoip-service
~~~~~~~~~~~~~

A simple, free GeoIP REST endpoint.
"""

import os

from itertools import chain
from functools import wraps

from flask import Flask, request, jsonify, current_app
from flask.ext.cache import Cache

from geoip2 import database
from geoip2.errors import AddressNotFoundError

cache = Cache(config={
    "CACHE_TYPE": "redis",
    "CACHE_REDIS_HOST": os.environ.get("REDIS_PORT_6379_TCP_ADDR",
                                       "localhost")
})

application = app = Flask(__name__)

DEBUG = True if os.environ.get("DEBUG") == "True" else False
LOCALES = {"de", "en", "es", "fr", "ja", "pt-BR", "ru", "zh-CN"}
GEOIP_DB = os.environ.get("GEOIP_DB", "GeoIP2.mmdb")

app.config.from_object(__name__)

cache.init_app(app)

reader = database.Reader(os.path.abspath(app.config["GEOIP_DB"]))


def jsonp(fn):
    """
    Wraps JSON-ified output for JSONP requests.
    """
    @wraps(fn)
    def wrapper(*args, **kwargs):
        callback = request.args.get("callback", None)
        if callback is not None:
            data = fn(*args, **kwargs).data.decode()
            content = "{callback}({data});".format(callback=callback,
                                                   data=data)
            mimetype = "application/javascript"
            return current_app.response_class(content, mimetype=mimetype)
        else:
            return fn(*args, **kwargs)
    return wrapper


def get_subdivision(locale, row, all=False):
    if all is False:
        subdivision = row.subdivisions.most_specific
        return {"name": subdivision.names.get(locale, subdivision.name),
                "abbr": subdivision.iso_code, }
    elif all is True:
        return [{"name": subdivision.names.get(locale, subdivision.name),
                 "abbr": subdivision.iso_code, }
                for subdivision in row.subdivisions]


def get_location(locale, ip):
    """
    Retrieves the location of a given IP address from a MaxMind GeoIP database.

    This product includes GeoLite2 data created by MaxMind, available from
    `<http://www.maxmind.com>`_.
    """
    try:
        row = reader.city(ip)
    except AddressNotFoundError:
        return None
    location = {key: value
                for key, value
                in chain(row.traits.__dict__.items(),
                         row.location.__dict__.items())}
    location.update(locale=locale,
                    city={"name": row.city.names.get(locale, row.city.name), },
                    subdivision=get_subdivision(locale, row),
                    subdivisions=get_subdivision(locale, row, all=True),
                    postal_code=row.postal.code,
                    country={
                        "name": row.country.names.get(locale,
                                                      row.country.name),
                        "abbr": row.country.iso_code, },
                    continent={
                        "name": row.continent.names.get(locale,
                                                        row.continent.name),
                        "abbr": row.continent.code, })
    return location


@app.route("/")
@app.route("/<ip>/")
@jsonp
def geo_ip_lookup(ip=None):
    """
    GeoIP lookup handler.
    """
    get_location_ = cache.memoize(120)(get_location)
    locale = request.accept_languages.best_match(app.config["LOCALES"])
    ip = request.remote_addr if ip is None else ip
    location = get_location_(locale, ip)
    if location is not None:
        response = jsonify({"ok": True, "res": location})
    else:
        response = jsonify({"ok": False, "res": "Not Found"})
        response.status_code = 404
    return response

if __name__ == "__main__":
    app.run()
