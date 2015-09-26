# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import values
from twilio.rest import deserialize
from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource
from twilio.rest.base import ListResource


class MemberList(ListResource):

    def __init__(self, version, account_sid, queue_sid):
        """
        Initialize the MemberList
        
        :param Version version: Version that contains the resource
        :param account_sid: Contextual account_sid
        :param queue_sid: Contextual queue_sid
        
        :returns: MemberList
        :rtype: MemberList
        """
        super(MemberList, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'account_sid': account_sid,
            'queue_sid': queue_sid,
        }
        self._uri = '/Accounts/{account_sid}/Queues/{queue_sid}/Members.json'.format(**self._kwargs)

    def stream(self, limit=None, page_size=None, **kwargs):
        """
        Streams MemberInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
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
            'PageSize': limits['page_size'],
        })
        params.update(kwargs)
        
        return self._version.stream(
            self,
            MemberInstance,
            self._kwargs,
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def read(self, limit=None, page_size=None, **kwargs):
        """
        Reads MemberInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
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
            limit=limit,
            page_size=page_size,
            **kwargs
        ))

    def page(self, page_token=None, page_number=None, page_size=None, **kwargs):
        """
        Retrieve a single page of MemberInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50
        
        :returns: Page of MemberInstance
        :rtype: Page
        """
        params = values.of({
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })
        params.update(kwargs)
        
        return self._version.page(
            self,
            MemberInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def __call__(self, call_sid):
        """
        Constructs a MemberContext
        
        :param call_sid: Contextual call_sid
        
        :returns: MemberContext
        :rtype: MemberContext
        """
        return MemberContext(self._version, call_sid=call_sid, **self._kwargs)

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.MemberList>'


class MemberContext(InstanceContext):

    def __init__(self, version, account_sid, queue_sid, call_sid):
        """
        Initialize the MemberContext
        
        :param Version version
        :param account_sid: Contextual account_sid
        :param queue_sid: Contextual queue_sid
        :param call_sid: Contextual call_sid
        
        :returns: MemberContext
        :rtype: MemberContext
        """
        super(MemberContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'account_sid': account_sid,
            'queue_sid': queue_sid,
            'call_sid': call_sid,
        }
        self._uri = '/Accounts/{account_sid}/Queues/{queue_sid}/Members/{call_sid}.json'.format(**self._kwargs)

    def fetch(self):
        """
        Fetch a MemberInstance
        
        :returns: Fetched MemberInstance
        :rtype: MemberInstance
        """
        params = values.of({})
        
        return self._version.fetch(
            MemberInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def update(self, url, method):
        """
        Update the MemberInstance
        
        :param str url: The url
        :param str method: The method
        
        :returns: Updated MemberInstance
        :rtype: MemberInstance
        """
        data = values.of({
            'Url': url,
            'Method': method,
        })
        
        return self._version.update(
            MemberInstance,
            self._kwargs,
            'POST',
            self._uri,
            data=data,
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._kwargs.items())
        return '<Twilio.Api.V2010.MemberContext {}>'.format(context)


class MemberInstance(InstanceResource):

    def __init__(self, version, payload, account_sid, queue_sid, call_sid=None):
        """
        Initialize the MemberInstance
        
        :returns: MemberInstance
        :rtype: MemberInstance
        """
        super(MemberInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'call_sid': payload['call_sid'],
            'date_enqueued': deserialize.rfc2822_datetime(payload['date_enqueued']),
            'parent_sid': payload['parent_sid'],
            'position': payload['position'],
            'sid': payload['sid'],
            'uri': payload['uri'],
            'wait_time': payload['wait_time'],
        }
        
        # Context
        self._instance_context = None
        self._kwargs = {
            'account_sid': account_sid,
            'queue_sid': queue_sid,
            'call_sid': call_sid or self._properties['call_sid'],
        }

    @property
    def _context(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context
        
        :returns: MemberContext for this MemberInstance
        :rtype: MemberContext
        """
        if self._instance_context is None:
            self._instance_context = MemberContext(
                self._version,
                self._kwargs['account_sid'],
                self._kwargs['queue_sid'],
                self._kwargs['call_sid'],
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
    def call_sid(self):
        """
        :returns: Unique string that identifies this resource
        :rtype: str
        """
        return self._properties['call_sid']

    @property
    def date_enqueued(self):
        """
        :returns: The date the member was enqueued
        :rtype: datetime
        """
        return self._properties['date_enqueued']

    @property
    def parent_sid(self):
        """
        :returns: The parent_sid
        :rtype: str
        """
        return self._properties['parent_sid']

    @property
    def position(self):
        """
        :returns: This member's current position in the queue.
        :rtype: str
        """
        return self._properties['position']

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

    @property
    def wait_time(self):
        """
        :returns: The number of seconds the member has been in the queue.
        :rtype: str
        """
        return self._properties['wait_time']

    def fetch(self):
        """
        Fetch a MemberInstance
        
        :returns: Fetched MemberInstance
        :rtype: MemberInstance
        """
        return self._context.fetch()

    def update(self, url, method):
        """
        Update the MemberInstance
        
        :param str url: The url
        :param str method: The method
        
        :returns: Updated MemberInstance
        :rtype: MemberInstance
        """
        return self._context.update(
            url,
            method,
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._kwargs.items())
        return '<Twilio.Api.V2010.MemberInstance {}>'.format(context)
