# heropunch/geoip-service
FROM gliderlabs/alpine:3.2
ENV GEOIP_DB /srv/GeoIP2.mmdb
RUN mkdir /srv
WORKDIR /srv
COPY src/ ./
COPY bin/get-mmdb /usr/local/bin/get-mmdb
RUN apk --update add python py-pip curl uwsgi-python \
        && pip install .
EXPOSE 80
ENTRYPOINT ["/srv/wrapper.sh"]
