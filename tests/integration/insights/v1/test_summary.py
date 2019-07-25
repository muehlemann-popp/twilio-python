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


class CallSummaryTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.insights.v1.summary(call_sid="CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://insights.twilio.com/v1/Voice/CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Summary',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "call_sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "call_type": "carrier",
                "call_state": "ringing",
                "processing_state": "complete",
                "direction": "inbound",
                "disconnected_by": "callee",
                "start_time": "2015-07-30T20:00:00Z",
                "end_time": "2015-07-30T20:00:00Z",
                "duration": 100,
                "connect_duration": 99,
                "from": {},
                "to": {},
                "carrier_edge": {},
                "client_edge": {},
                "sdk_edge": {},
                "sip_edge": {},
                "tags": [
                    "tags"
                ],
                "attributes": {},
                "properties": {},
                "url": "https://insights.twilio.com/v1/Voice/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Summary"
            }
            '''
        ))

        actual = self.client.insights.v1.summary(call_sid="CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)
