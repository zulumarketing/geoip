# -*- coding: utf-8 -*-

from unittest import TestCase

from geoip import get_location


class TestGeoIPService(TestCase):
    def setUp(self):
        self.ips = {"136.39.103.199": None,
                    "113.106.129.229": None,
                    "146.40.46.177": None,
                    "132.125.225.179": None,
                    "26.128.146.170": None,
                    "108.146.116.228": None,
                    "165.117.98.236": None,
                    "150.158.81.32": None,
                    "197.183.230.56": None,
                    "34.105.31.180": None,
                    "145.76.102.22": None,
                    "201.73.201.226": None}

    def test_get_location(self):
        for ip, location in self.ips.items():
            self.assertEqual(get_location('en', ip)["city"], location)
