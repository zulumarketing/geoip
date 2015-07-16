#!/bin/bash

URL="https://www.maxmind.com/app/geoip_download?edition_id=GeoIP2-City&date=$1&suffix=tar.gz&license_key=$MAX_MIND_LICENSE_KEY"

curl -s $URL | tar --to-stdout -xzf - "GeoIP2-City_$1/GeoIP2-City.mmdb"
