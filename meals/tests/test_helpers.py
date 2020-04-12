# -*- coding: utf-8 -*-
from unittest import TestCase

from meals import helpers


class UUIDTest(TestCase):
    def test_uuid_generation(self):
        uuid = helpers.generate_uuid()
        self.assertIsNotNone(uuid)
        self.assertTrue(uuid.__len__())
