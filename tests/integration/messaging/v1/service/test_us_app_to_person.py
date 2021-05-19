# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base import serialize
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class UsAppToPersonTestCase(IntegrationTestCase):

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.messaging.v1.services("MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                    .us_app_to_person.create(brand_registration_sid="BNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", description="description", message_samples=['message_samples'], us_app_to_person_usecase="us_app_to_person_usecase", has_embedded_links=True, has_embedded_phone=True)

        values = {
            'BrandRegistrationSid': "BNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            'Description': "description",
            'MessageSamples': serialize.map(['message_samples'], lambda e: e),
            'UsAppToPersonUsecase': "us_app_to_person_usecase",
            'HasEmbeddedLinks': True,
            'HasEmbeddedPhone': True,
        }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://messaging.twilio.com/v1/Services/MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Compliance/Usa2p',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "sid": "QE2c6890da8086d771620e9b13fadeba0b",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "brand_registration_sid": "BNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "messaging_service_sid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "description": "Send marketing messages about sales to opted in customers.",
                "message_samples": [
                    "EXPRESS: Denim Days Event is ON",
                    "LAST CHANCE: Book your next flight for just 1 (ONE) EUR"
                ],
                "us_app_to_person_usecase": "MARKETING",
                "has_embedded_links": true,
                "has_embedded_phone": false,
                "campaign_status": "PENDING",
                "campaign_id": "CXaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "is_externally_registered": false,
                "rate_limits": {
                    "att": {
                        "mps": 600,
                        "msg_class": "A"
                    },
                    "tmobile": {
                        "brand_tier": "TOP"
                    }
                },
                "date_created": "2021-02-18T14:48:52Z",
                "date_updated": "2021-02-18T14:48:52Z",
                "url": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Compliance/Usa2p/QE2c6890da8086d771620e9b13fadeba0b"
            }
            '''
        ))

        actual = self.client.messaging.v1.services("MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                         .us_app_to_person.create(brand_registration_sid="BNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", description="description", message_samples=['message_samples'], us_app_to_person_usecase="us_app_to_person_usecase", has_embedded_links=True, has_embedded_phone=True)

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.messaging.v1.services("MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                    .us_app_to_person("QEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://messaging.twilio.com/v1/Services/MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Compliance/Usa2p/QEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.messaging.v1.services("MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                         .us_app_to_person("QEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.assertTrue(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.messaging.v1.services("MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                    .us_app_to_person.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://messaging.twilio.com/v1/Services/MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Compliance/Usa2p',
        ))

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "compliance": [
                    {
                        "sid": "QE2c6890da8086d771620e9b13fadeba0b",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "brand_registration_sid": "BNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "messaging_service_sid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "description": "Send marketing messages about sales to opted in customers.",
                        "message_samples": [
                            "EXPRESS: Denim Days Event is ON",
                            "LAST CHANCE: Book your next flight for just 1 (ONE) EUR"
                        ],
                        "us_app_to_person_usecase": "MARKETING",
                        "has_embedded_links": true,
                        "has_embedded_phone": false,
                        "campaign_status": "PENDING",
                        "campaign_id": "CXaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "is_externally_registered": false,
                        "rate_limits": {
                            "att": {
                                "mps": 600,
                                "msg_class": "A"
                            },
                            "tmobile": {
                                "brand_tier": "TOP"
                            }
                        },
                        "date_created": "2021-02-18T14:48:52Z",
                        "date_updated": "2021-02-18T14:48:52Z",
                        "url": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Compliance/Usa2p/QE2c6890da8086d771620e9b13fadeba0b"
                    }
                ],
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Compliance/Usa2p?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "next_page_url": null,
                    "url": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Compliance/Usa2p?PageSize=50&Page=0",
                    "key": "compliance"
                }
            }
            '''
        ))

        actual = self.client.messaging.v1.services("MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                         .us_app_to_person.list()

        self.assertIsNotNone(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.messaging.v1.services("MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                    .us_app_to_person("QEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://messaging.twilio.com/v1/Services/MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Compliance/Usa2p/QEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "QE2c6890da8086d771620e9b13fadeba0b",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "brand_registration_sid": "BNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "messaging_service_sid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "description": "Send marketing messages about sales to opted in customers.",
                "message_samples": [
                    "EXPRESS: Denim Days Event is ON",
                    "LAST CHANCE: Book your next flight for just 1 (ONE) EUR"
                ],
                "us_app_to_person_usecase": "MARKETING",
                "has_embedded_links": true,
                "has_embedded_phone": false,
                "campaign_status": "PENDING",
                "campaign_id": "CXaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "is_externally_registered": false,
                "rate_limits": {
                    "att": {
                        "mps": 600,
                        "msg_class": "A"
                    },
                    "tmobile": {
                        "brand_tier": "TOP"
                    }
                },
                "date_created": "2021-02-18T14:48:52Z",
                "date_updated": "2021-02-18T14:48:52Z",
                "url": "https://messaging.twilio.com/v1/Services/MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Compliance/Usa2p/QE2c6890da8086d771620e9b13fadeba0b"
            }
            '''
        ))

        actual = self.client.messaging.v1.services("MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                         .us_app_to_person("QEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)
