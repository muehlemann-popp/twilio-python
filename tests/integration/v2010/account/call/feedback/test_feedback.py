# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

import unittest
from datetime import datetime
from twilio.ext.holodeck import Holodeck
from twilio.rest.v2010.client import V2010Client
from twilio.rest.http import Response
from twilio.rest import (
    deserialize,
    serialize,
)


class FeedbackIntegrationTest(unittest.TestCase):

    def test_create_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "date_created": "Thu, 20 Aug 2015 21:45:46 +0000",
            "date_updated": "Thu, 20 Aug 2015 21:45:46 +0000",
            "issues": [
                "imperfect-audio",
                "post-dial-delay"
            ],
            "quality_score": 5,
            "sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .calls.get("CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .feedback.create(
                1,
                issue=['audio-latency']
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "POST",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Feedback.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            query_params={},
            form_params={
                "Issue": [
                    "audio-latency"
                ],
                "QualityScore": 1
            },
        )

    def test_create_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "date_created": "Thu, 20 Aug 2015 21:45:46 +0000",
            "date_updated": "Thu, 20 Aug 2015 21:45:46 +0000",
            "issues": [
                "imperfect-audio",
                "post-dial-delay"
            ],
            "quality_score": 5,
            "sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .calls.get("CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .feedback.create(
                1,
                issue=['audio-latency']
            )
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(deserialize.iso8601_datetime('Thu, 20 Aug 2015 21:45:46 +0000'), instance.date_created)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(deserialize.iso8601_datetime('Thu, 20 Aug 2015 21:45:46 +0000'), instance.date_updated)
        self.assertIsNotNone(instance.quality_score)
        self.assertEqual(5, instance.quality_score)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)

    def test_fetch_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "date_created": "Thu, 20 Aug 2015 21:45:46 +0000",
            "date_updated": "Thu, 20 Aug 2015 21:45:46 +0000",
            "issues": [
                "imperfect-audio",
                "post-dial-delay"
            ],
            "quality_score": 5,
            "sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .calls.get("CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .feedback.get()
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Feedback.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            query_params={},
            form_params={},
        )

    def test_fetch_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "date_created": "Thu, 20 Aug 2015 21:45:46 +0000",
            "date_updated": "Thu, 20 Aug 2015 21:45:46 +0000",
            "issues": [
                "imperfect-audio",
                "post-dial-delay"
            ],
            "quality_score": 5,
            "sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .calls.get("CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .feedback.get()
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(deserialize.iso8601_datetime('Thu, 20 Aug 2015 21:45:46 +0000'), instance.date_created)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(deserialize.iso8601_datetime('Thu, 20 Aug 2015 21:45:46 +0000'), instance.date_updated)
        self.assertIsNotNone(instance.quality_score)
        self.assertEqual(5, instance.quality_score)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)

    def test_update_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "date_created": "Thu, 20 Aug 2015 21:45:46 +0000",
            "date_updated": "Thu, 20 Aug 2015 21:45:46 +0000",
            "issues": [
                "imperfect-audio",
                "post-dial-delay"
            ],
            "quality_score": 5,
            "sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .calls.get("CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .feedback.update(
                1,
                issue=['audio-latency']
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "POST",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Feedback.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            query_params={},
            form_params={
                "Issue": [
                    "audio-latency"
                ],
                "QualityScored": 1
            },
        )

    def test_update_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "date_created": "Thu, 20 Aug 2015 21:45:46 +0000",
            "date_updated": "Thu, 20 Aug 2015 21:45:46 +0000",
            "issues": [
                "imperfect-audio",
                "post-dial-delay"
            ],
            "quality_score": 5,
            "sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .calls.get("CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .feedback.update(
                1,
                issue=['audio-latency']
            )
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(deserialize.iso8601_datetime('Thu, 20 Aug 2015 21:45:46 +0000'), instance.date_created)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(deserialize.iso8601_datetime('Thu, 20 Aug 2015 21:45:46 +0000'), instance.date_updated)
        self.assertIsNotNone(instance.quality_score)
        self.assertEqual(5, instance.quality_score)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)
