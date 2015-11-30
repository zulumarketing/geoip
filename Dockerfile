FROM gliderlabs/alpine:3.2
RUN mkdir /srv
WORKDIR /srv
COPY src/ ./
COPY bin/get-mmdb /usr/local/bin/get-mmdb
RUN apk --update add python py-pip openssl ca-certificates uwsgi-python \
        && apk add --virtual build-deps python-dev \
        && pip install . \
        && apk del build-deps
ENTRYPOINT ["/srv/wrapper.sh"]
