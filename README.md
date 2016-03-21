### geoip

A simple, free GeoIP REST endpoint.

### Usage

```sh
# Build
docker build -t geoip .

# Load GeoLite2-City
$ docker run -d geoip free

# Load GeoIP-City (requires a license key)
$ docker run -d geoip commercial $license_key

# Caching is enabled by linking to a container running `redis-server`
$ docker run -d --name redis redis-server
$ docker run -d --link redis:redis geoip free
```

### API

`geoip` supports IPv4 and IPv6 addresses.

```sh
$ curl http://geoip.ns/113.106.129.229/
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
```
