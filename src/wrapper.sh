#!/bin/sh

case "$1" in
    "free") get-mmdb $1 > /srv/GeoIP2-City.mmdb;;
    "commercial") get-mmdb $1 $2 > /srv/GeoIP2-City.mmdb;;
    *)
        >&2 echo "geoip-service: usage: [ free | commercial <license_key> ]"
        exit 1;;
esac

exec uwsgi --yaml /srv/uwsgi.yaml
