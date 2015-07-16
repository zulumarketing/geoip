#!/bin/bash

URL="https://www.maxmind.com/app/geoip_download?edition_id=GeoIP2-City&date=$1&suffix=tar.gz&license_key=$2"

curl -s $URL | tar --to-stdout -xzf - "GeoIP2-City_$1/GeoIP2-City.mmdb"
