#!/bin/bash

DATE="$1"
KEY="$2"
URL="https://www.maxmind.com/app/geoip_download?edition_id=GeoIP2-City&date=$DATE&suffix=tar.gz&license_key=$KEY"

curl -s $URL | tar --to-stdout -xzf - "GeoIP2-City_$DATE/GeoIP2-City.mmdb"
