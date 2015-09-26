# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import values
from twilio.rest import deserialize
from twilio.rest import serialize
from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource
from twilio.rest.base import ListResource


class NotificationList(ListResource):

    def __init__(self, version, account_sid, call_sid):
        """
        Initialize the NotificationList
        
        :param Version version: Version that contains the resource
        :param account_sid: Contextual account_sid
        :param call_sid: Contextual call_sid
        
        :returns: NotificationList
        :rtype: NotificationList
        """
        super(NotificationList, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'account_sid': account_sid,
            'call_sid': call_sid,
        }
        self._uri = '/Accounts/{account_sid}/Calls/{call_sid}/Notifications.json'.format(**self._kwargs)

    def stream(self, log=values.unset, message_date_before=values.unset,
               message_date=values.unset, message_date_after=values.unset,
               limit=None, page_size=None, **kwargs):
        """
        Streams NotificationInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param str log: The log
        :param date message_date_before: The message_date
        :param date message_date: The message_date
        :param date message_date_after: The message_date
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)
        
        :returns: Generator that will yield up to limit results
        :rtype: generator
        """
        limits = self._version.read_limits(limit, page_size)
        
        params = values.of({
            'Log': log,
            'MessageDate<': serialize.iso8601_date(message_date_before),
            'MessageDate': serialize.iso8601_date(message_date),
            'MessageDate>': serialize.iso8601_date(message_date_after),
            'PageSize': limits['page_size'],
        })
        params.update(kwargs)
        
        return self._version.stream(
            self,
            NotificationInstance,
            self._kwargs,
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def read(self, log=values.unset, message_date_before=values.unset,
             message_date=values.unset, message_date_after=values.unset, limit=None,
             page_size=None, **kwargs):
        """
        Reads NotificationInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param str log: The log
        :param date message_date_before: The message_date
        :param date message_date: The message_date
        :param date message_date_after: The message_date
        :param int limit: Upper limit for the number of records to return. read() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, read() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)
        
        :returns: Generator that will yield up to limit results
        :rtype: generator
        """
        return list(self.stream(
            log=log,
            message_date_before=message_date_before,
            message_date=message_date,
            message_date_after=message_date_after,
            limit=limit,
            page_size=page_size,
            **kwargs
        ))

    def page(self, log=values.unset, message_date_before=values.unset,
             message_date=values.unset, message_date_after=values.unset,
             page_token=None, page_number=None, page_size=None, **kwargs):
        """
        Retrieve a single page of NotificationInstance records from the API.
        Request is executed immediately
        
        :param str log: The log
        :param date message_date_before: The message_date
        :param date message_date: The message_date
        :param date message_date_after: The message_date
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50
        
        :returns: Page of NotificationInstance
        :rtype: Page
        """
        params = values.of({
            'Log': log,
            'MessageDate<': serialize.iso8601_date(message_date_before),
            'MessageDate': serialize.iso8601_date(message_date),
            'MessageDate>': serialize.iso8601_date(message_date_after),
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })
        params.update(kwargs)
        
        return self._version.page(
            self,
            NotificationInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def __call__(self, sid):
        """
        Constructs a NotificationContext
        
        :param sid: Contextual sid
        
        :returns: NotificationContext
        :rtype: NotificationContext
        """
        return NotificationContext(self._version, sid=sid, **self._kwargs)

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.NotificationList>'


class NotificationContext(InstanceContext):

    def __init__(self, version, account_sid, call_sid, sid):
        """
        Initialize the NotificationContext
        
        :param Version version
        :param account_sid: Contextual account_sid
        :param call_sid: Contextual call_sid
        :param sid: Contextual sid
        
        :returns: NotificationContext
        :rtype: NotificationContext
        """
        super(NotificationContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'account_sid': account_sid,
            'call_sid': call_sid,
            'sid': sid,
        }
        self._uri = '/Accounts/{account_sid}/Calls/{call_sid}/Notifications/{sid}.json'.format(**self._kwargs)

    def fetch(self):
        """
        Fetch a NotificationInstance
        
        :returns: Fetched NotificationInstance
        :rtype: NotificationInstance
        """
        params = values.of({})
        
        return self._version.fetch(
            NotificationInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def delete(self):
        """
        Deletes the NotificationInstance
        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._kwargs.items())
        return '<Twilio.Api.V2010.NotificationContext {}>'.format(context)


class NotificationInstance(InstanceResource):

    def __init__(self, version, payload, account_sid, call_sid, sid=None):
        """
        Initialize the NotificationInstance
        
        :returns: NotificationInstance
        :rtype: NotificationInstance
        """
        super(NotificationInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'api_version': payload['api_version'],
            'call_sid': payload['call_sid'],
            'date_created': deserialize.rfc2822_datetime(payload['date_created']),
            'date_updated': deserialize.rfc2822_datetime(payload['date_updated']),
            'error_code': payload['error_code'],
            'log': payload['log'],
            'message_date': deserialize.rfc2822_datetime(payload['message_date']),
            'message_text': payload['message_text'],
            'more_info': payload['more_info'],
            'request_method': payload['request_method'],
            'request_url': payload['request_url'],
            'request_variables': payload['request_variables'],
            'response_body': payload['response_body'],
            'response_headers': payload['response_headers'],
            'sid': payload['sid'],
            'uri': payload['uri'],
        }
        
        # Context
        self._instance_context = None
        self._kwargs = {
            'account_sid': account_sid,
            'call_sid': call_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _context(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context
        
        :returns: NotificationContext for this NotificationInstance
        :rtype: NotificationContext
        """
        if self._instance_context is None:
            self._instance_context = NotificationContext(
                self._version,
                self._kwargs['account_sid'],
                self._kwargs['call_sid'],
                self._kwargs['sid'],
            )
        return self._instance_context

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: str
        """
        return self._properties['account_sid']

    @property
    def api_version(self):
        """
        :returns: The api_version
        :rtype: str
        """
        return self._properties['api_version']

    @property
    def call_sid(self):
        """
        :returns: The call_sid
        :rtype: str
        """
        return self._properties['call_sid']

    @property
    def date_created(self):
        """
        :returns: The date_created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date_updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def error_code(self):
        """
        :returns: The error_code
        :rtype: str
        """
        return self._properties['error_code']

    @property
    def log(self):
        """
        :returns: The log
        :rtype: str
        """
        return self._properties['log']

    @property
    def message_date(self):
        """
        :returns: The message_date
        :rtype: datetime
        """
        return self._properties['message_date']

    @property
    def message_text(self):
        """
        :returns: The message_text
        :rtype: str
        """
        return self._properties['message_text']

    @property
    def more_info(self):
        """
        :returns: The more_info
        :rtype: str
        """
        return self._properties['more_info']

    @property
    def request_method(self):
        """
        :returns: The request_method
        :rtype: str
        """
        return self._properties['request_method']

    @property
    def request_url(self):
        """
        :returns: The request_url
        :rtype: str
        """
        return self._properties['request_url']

    @property
    def request_variables(self):
        """
        :returns: The request_variables
        :rtype: str
        """
        return self._properties['request_variables']

    @property
    def response_body(self):
        """
        :returns: The response_body
        :rtype: str
        """
        return self._properties['response_body']

    @property
    def response_headers(self):
        """
        :returns: The response_headers
        :rtype: str
        """
        return self._properties['response_headers']

    @property
    def sid(self):
        """
        :returns: The sid
        :rtype: str
        """
        return self._properties['sid']

    @property
    def uri(self):
        """
        :returns: The uri
        :rtype: str
        """
        return self._properties['uri']

    def fetch(self):
        """
        Fetch a NotificationInstance
        
        :returns: Fetched NotificationInstance
        :rtype: NotificationInstance
        """
        return self._context.fetch()

    def delete(self):
        """
        Deletes the NotificationInstance
        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._context.delete()

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._kwargs.items())
        return '<Twilio.Api.V2010.NotificationInstance {}>'.format(context)
