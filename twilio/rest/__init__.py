# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

import os
import platform
from twilio.exceptions import TwilioException
from twilio.http.httplib2_client import Httplib2Client
from twilio.rest.api import Api
from twilio.rest.conversations import Conversations
from twilio.rest.lookups import Lookups
from twilio.rest.monitor import Monitor
from twilio.rest.pricing import Pricing
from twilio.rest.taskrouter import Taskrouter
from twilio.rest.trunking import Trunking
from twilio.version import __version__


class Twilio(object):
    """ A client for accessing the Twilio API. """

    def __init__(self, account_sid=None, auth_token=None, http_client=None,
                 environment=None):
        """
        Initializes the Twilio Client
        
        :param str account_sid: Account Sid to authenticate with
        :param str auth_token: Auth Token to authenticate with
        :param HttpClient http_client: HttpClient, defaults to Httplib2Client
        :param dict environment: Environment to look for auth details, defaults to os.environ
        
        :returns: Twilio Client
        :rtype: twilio.rest.Twilio
        """
        environment = environment or os.environ
        
        self.account_sid = account_sid or environment.get('TWILIO_ACCOUNT_SID')
        """ :type : str """
        self.auth_token = auth_token or environment.get('TWILIO_AUTH_TOKEN')
        """ :type : str """
        
        if not self.account_sid or not self.auth_token:
            raise TwilioException("Credentials are required to create a TwilioClient")
        
        self.auth = (self.account_sid, self.auth_token)
        """ :type : tuple(str, str) """
        self.http_client = http_client or Httplib2Client()
        """ :type : HttpClient """
        
        # Domains
        self._api = None
        self._conversations = None
        self._lookups = None
        self._monitor = None
        self._pricing = None
        self._taskrouter = None
        self._trunking = None

    def request(self, method, uri, params=None, data=None, headers=None, auth=None,
                timeout=None, allow_redirects=False):
        """
        Makes a request to the Twilio API using the configured http client
        Authentication information is automatically added if none is provided
        
        :param str method: HTTP Method
        :param str uri: Fully qualified url
        :param dict[str, str] params: Query string parameters
        :param dict[str, str] data: POST body data
        :param dict[str, str] headers: HTTP Headers
        :param tuple(str, str) auth: Authentication
        :param int timeout: Timeout in seconds
        :param bool allow_redirects: Should the client follow redirects
        
        :returns: Response from the Twilio API
        :rtype: twilio.http.response.Response
        """
        auth = auth or self.auth
        headers = headers or {}
        
        headers['User-Agent'] = 'twilio-python/{} (Python {})'.format(
            __version__,
            platform.python_version(),
        )
        headers['Accept-Charset'] = 'utf-8'
        
        if method == 'POST' and 'Content-Type' not in headers:
            headers['Content-Type'] = 'application/x-www-form-urlencoded'
        
        if 'Accept' not in headers:
            headers['Accept'] = 'application/json'
        
        return self.http_client.request(
            method,
            uri,
            params=params,
            data=data,
            headers=headers,
            auth=auth,
            timeout=timeout,
            allow_redirects=allow_redirects
        )

    @property
    def api(self):
        """
        Access the Api Twilio Domain
        
        :returns: Api Twilio Domain
        :rtype: Api
        """
        if self._api is None:
            self._api = Api(self)
        return self._api

    @property
    def conversations(self):
        """
        Access the Conversations Twilio Domain
        
        :returns: Conversations Twilio Domain
        :rtype: Conversations
        """
        if self._conversations is None:
            self._conversations = Conversations(self)
        return self._conversations

    @property
    def lookups(self):
        """
        Access the Lookups Twilio Domain
        
        :returns: Lookups Twilio Domain
        :rtype: Lookups
        """
        if self._lookups is None:
            self._lookups = Lookups(self)
        return self._lookups

    @property
    def monitor(self):
        """
        Access the Monitor Twilio Domain
        
        :returns: Monitor Twilio Domain
        :rtype: Monitor
        """
        if self._monitor is None:
            self._monitor = Monitor(self)
        return self._monitor

    @property
    def pricing(self):
        """
        Access the Pricing Twilio Domain
        
        :returns: Pricing Twilio Domain
        :rtype: Pricing
        """
        if self._pricing is None:
            self._pricing = Pricing(self)
        return self._pricing

    @property
    def taskrouter(self):
        """
        Access the Taskrouter Twilio Domain
        
        :returns: Taskrouter Twilio Domain
        :rtype: Taskrouter
        """
        if self._taskrouter is None:
            self._taskrouter = Taskrouter(self)
        return self._taskrouter

    @property
    def trunking(self):
        """
        Access the Trunking Twilio Domain
        
        :returns: Trunking Twilio Domain
        :rtype: Trunking
        """
        if self._trunking is None:
            self._trunking = Trunking(self)
        return self._trunking

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio {}>'.format(self.account_sid)
