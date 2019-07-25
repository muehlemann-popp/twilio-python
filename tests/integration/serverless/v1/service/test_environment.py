# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class EnvironmentTestCase(IntegrationTestCase):

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.serverless.v1.services(sid="ZSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .environments.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://serverless.twilio.com/v1/Services/ZSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Environments',
        ))

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "environments": [],
                "meta": {
                    "first_page_url": "https://serverless.twilio.com/v1/Services/ZS00000000000000000000000000000000/Environments?PageSize=50&Page=0",
                    "key": "environments",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://serverless.twilio.com/v1/Services/ZS00000000000000000000000000000000/Environments?PageSize=50&Page=0"
                }
            }
            '''
        ))

        actual = self.client.serverless.v1.services(sid="ZSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                          .environments.list()

        self.assertIsNotNone(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.serverless.v1.services(sid="ZSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .environments(sid="ZEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://serverless.twilio.com/v1/Services/ZSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Environments/ZEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "ZE00000000000000000000000000000000",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "ZS00000000000000000000000000000000",
                "build_sid": "ZB00000000000000000000000000000000",
                "unique_name": "testing-environment",
                "domain_suffix": "testing",
                "domain_name": "foobar-1234-testing.twil.io",
                "date_created": "2018-11-10T20:00:00Z",
                "date_updated": "2018-11-10T20:00:00Z",
                "url": "https://serverless.twilio.com/v1/Services/ZS00000000000000000000000000000000/Environments/ZE00000000000000000000000000000000",
                "links": {
                    "variables": "https://serverless.twilio.com/v1/Services/ZS00000000000000000000000000000000/Environments/ZE00000000000000000000000000000000/Variables",
                    "deployments": "https://serverless.twilio.com/v1/Services/ZS00000000000000000000000000000000/Environments/ZE00000000000000000000000000000000/Deployments"
                }
            }
            '''
        ))

        actual = self.client.serverless.v1.services(sid="ZSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                          .environments(sid="ZEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.serverless.v1.services(sid="ZSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .environments.create(unique_name="unique_name")

        values = {'UniqueName': "unique_name", }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://serverless.twilio.com/v1/Services/ZSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Environments',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "sid": "ZE00000000000000000000000000000000",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "ZS00000000000000000000000000000000",
                "build_sid": null,
                "unique_name": "staging",
                "domain_suffix": "stage",
                "domain_name": "foobar-1234-stage.twil.io",
                "date_created": "2018-11-10T20:00:00Z",
                "date_updated": "2018-11-10T20:00:00Z",
                "url": "https://serverless.twilio.com/v1/Services/ZS00000000000000000000000000000000/Environments/ZE00000000000000000000000000000000",
                "links": {
                    "variables": "https://serverless.twilio.com/v1/Services/ZS00000000000000000000000000000000/Environments/ZE00000000000000000000000000000000/Variables",
                    "deployments": "https://serverless.twilio.com/v1/Services/ZS00000000000000000000000000000000/Environments/ZE00000000000000000000000000000000/Deployments"
                }
            }
            '''
        ))

        actual = self.client.serverless.v1.services(sid="ZSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                          .environments.create(unique_name="unique_name")

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.serverless.v1.services(sid="ZSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .environments(sid="ZEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://serverless.twilio.com/v1/Services/ZSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Environments/ZEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.serverless.v1.services(sid="ZSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                          .environments(sid="ZEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.assertTrue(actual)
