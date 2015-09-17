# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio.rest import (
    deserialize,
    serialize,
)
from twilio.rest.resources.base import NextGenInstanceResource
from twilio.rest.resources.base import NextGenListResource
from twilio.rest.resources.base import GetQuery


class Statistics(NextGenInstanceResource):
    """
    .. attribute:: account_sid
    
        The account_sid
    
    .. attribute:: cumulative
    
        The cumulative
    
    .. attribute:: realtime
    
        The realtime
    
    .. attribute:: workflow_sid
    
        The workflow_sid
    
    .. attribute:: workspace_sid
    
        The workspace_sid
    """
    id_key = "sid"

    def __init__(self, parent, *args, **kwargs):
        self.parent = parent
        super(Statistics, self).__init__(parent, None)


class StatisticsList(NextGenListResource):
    name = "Statistics"
    mount_name = "statistics"
    key = "statistics"
    instance = Statistics

    def __init__(self, *args, **kwargs):
        super(StatisticsList, self).__init__(*args, **kwargs)

    def get(self, minutes=None, start_date=None, end_date=None, **kwargs):
        """
        Get the Statistics
        
        :param date end_date: The end_date
        :param date start_date: The start_date
        :param str minutes: The minutes
        
        :raises TwilioRestException: when the request fails on execute
        """
        kwargs['Minutes'] = minutes
        kwargs['StartDate'] = serialize.iso8601_date(start_date)
        kwargs['EndDate'] = serialize.iso8601_date(end_date)
        
        return GetQuery(self, self.uri, self.use_json_extension,
                        params=kwargs)

    def load_instance(self, data):
        """ Override because Statistics does not have a sid """
        instance = self.instance(self)
        instance.load(data)
        instance.load_subresources()
        return instance
