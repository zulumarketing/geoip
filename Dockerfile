FROM gliderlabs/alpine:3.2
MAINTAINER Carlos Killpack <carlos@infinite.ai>
ENV GEOIP_DB /srv/GeoIP2-City.mmdb
RUN mkdir /srv
WORKDIR /srv
COPY src/ ./
COPY bin/get-mmdb /usr/local/bin/get-mmdb
RUN apk --update add python py-pip curl uwsgi-python \
        && pip install .
EXPOSE 80
ENTRYPOINT ["/srv/wrapper.sh"]
