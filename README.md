[![Travis CI](https://travis-ci.org/heropunch/geoip-service.svg?branch=master)](https://travis-ci.org/heropunch/geoip-service)

### geoip-service

A simple, free GeoIP REST endpoint.

### Usage

```sh
$ docker pull heropunch/geoip-service
$ # Load GeoLite2-City
$ docker run -d heropunch/geoip-service free
$ # Load GeoIP-City (requires a license key)
$ docker run -d heropunch/geoip-service commercial $license_key
```

### API

`geoip-service` support IPv4 and IPv6 addresses.

```sh
$ curl http://geoip-service/113.106.129.229/
{
  "ok": true, 
  "res": {
    "accuracy_radius": null, 
    "autonomous_system_number": null, 
    "autonomous_system_organization": null, 
    "average_income": null, 
    "city": {
      "name": "Guangzhou"
    }, 
    "continent": {
      "abbr": "AS", 
      "name": "Asia"
    }, 
    "country": {
      "abbr": "CN", 
      "name": "China"
    }, 
    "domain": null, 
    "ip_address": "113.106.129.229", 
    "is_anonymous_proxy": false, 
    "is_satellite_provider": false, 
    "isp": null, 
    "latitude": 23.1167, 
    "locale": null, 
    "longitude": 113.25, 
    "metro_code": null, 
    "organization": null, 
    "population_density": null, 
    "postal_code": null, 
    "postal_confidence": null, 
    "subdivision": {
      "abbr": "44", 
      "name": "Guangdong"
    }, 
    "subdivisions": [
      {
        "abbr": "44", 
        "name": "Guangdong"
      }
    ], 
    "time_zone": "Asia/Shanghai", 
    "user_type": null
  }
}
