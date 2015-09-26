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


class SandboxContext(InstanceContext):

    def __init__(self, version, account_sid):
        """
        Initialize the SandboxContext
        
        :param Version version
        :param account_sid: Contextual account_sid
        
        :returns: SandboxContext
        :rtype: SandboxContext
        """
        super(SandboxContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'account_sid': account_sid,
        }
        self._uri = '/Accounts/{account_sid}/Sandbox.json'.format(**self._kwargs)

    def fetch(self):
        """
        Fetch a SandboxInstance
        
        :returns: Fetched SandboxInstance
        :rtype: SandboxInstance
        """
        params = values.of({})
        
        return self._version.fetch(
            SandboxInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def update(self, voice_url=values.unset, voice_method=values.unset,
               sms_url=values.unset, sms_method=values.unset,
               status_callback=values.unset, status_callback_method=values.unset):
        """
        Update the SandboxInstance
        
        :param str voice_url: The voice_url
        :param str voice_method: The voice_method
        :param str sms_url: The sms_url
        :param str sms_method: The sms_method
        :param str status_callback: The status_callback
        :param str status_callback_method: The status_callback_method
        
        :returns: Updated SandboxInstance
        :rtype: SandboxInstance
        """
        data = values.of({
            'VoiceUrl': voice_url,
            'VoiceMethod': voice_method,
            'SmsUrl': sms_url,
            'SmsMethod': sms_method,
            'StatusCallback': status_callback,
            'StatusCallbackMethod': status_callback_method,
        })
        
        return self._version.update(
            SandboxInstance,
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
        return '<Twilio.Api.V2010.SandboxContext {}>'.format(context)


class SandboxInstance(InstanceResource):

    def __init__(self, version, payload, account_sid=None):
        """
        Initialize the SandboxInstance
        
        :returns: SandboxInstance
        :rtype: SandboxInstance
        """
        super(SandboxInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'date_created': deserialize.rfc2822_datetime(payload['date_created']),
            'date_updated': deserialize.rfc2822_datetime(payload['date_updated']),
            'pin': payload['pin'],
            'account_sid': payload['account_sid'],
            'phone_number': payload['phone_number'],
            'application_sid': payload['application_sid'],
            'api_version': payload['api_version'],
            'voice_url': payload['voice_url'],
            'voice_method': payload['voice_method'],
            'sms_url': payload['sms_url'],
            'sms_method': payload['sms_method'],
            'status_callback': payload['status_callback'],
            'status_callback_method': payload['status_callback_method'],
            'uri': payload['uri'],
        }
        
        # Context
        self._instance_context = None
        self._kwargs = {
            'account_sid': account_sid or self._properties['account_sid'],
        }

    @property
    def _context(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context
        
        :returns: SandboxContext for this SandboxInstance
        :rtype: SandboxContext
        """
        if self._instance_context is None:
            self._instance_context = SandboxContext(
                self._version,
                self._kwargs['account_sid'],
            )
        return self._instance_context

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
    def pin(self):
        """
        :returns: The pin
        :rtype: str
        """
        return self._properties['pin']

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: str
        """
        return self._properties['account_sid']

    @property
    def phone_number(self):
        """
        :returns: The phone_number
        :rtype: str
        """
        return self._properties['phone_number']

    @property
    def application_sid(self):
        """
        :returns: The application_sid
        :rtype: str
        """
        return self._properties['application_sid']

    @property
    def api_version(self):
        """
        :returns: The api_version
        :rtype: str
        """
        return self._properties['api_version']

    @property
    def voice_url(self):
        """
        :returns: The voice_url
        :rtype: str
        """
        return self._properties['voice_url']

    @property
    def voice_method(self):
        """
        :returns: The voice_method
        :rtype: str
        """
        return self._properties['voice_method']

    @property
    def sms_url(self):
        """
        :returns: The sms_url
        :rtype: str
        """
        return self._properties['sms_url']

    @property
    def sms_method(self):
        """
        :returns: The sms_method
        :rtype: str
        """
        return self._properties['sms_method']

    @property
    def status_callback(self):
        """
        :returns: The status_callback
        :rtype: str
        """
        return self._properties['status_callback']

    @property
    def status_callback_method(self):
        """
        :returns: The status_callback_method
        :rtype: str
        """
        return self._properties['status_callback_method']

    @property
    def uri(self):
        """
        :returns: The uri
        :rtype: str
        """
        return self._properties['uri']

    def fetch(self):
        """
        Fetch a SandboxInstance
        
        :returns: Fetched SandboxInstance
        :rtype: SandboxInstance
        """
        return self._context.fetch()

    def update(self, voice_url=values.unset, voice_method=values.unset,
               sms_url=values.unset, sms_method=values.unset,
               status_callback=values.unset, status_callback_method=values.unset):
        """
        Update the SandboxInstance
        
        :param str voice_url: The voice_url
        :param str voice_method: The voice_method
        :param str sms_url: The sms_url
        :param str sms_method: The sms_method
        :param str status_callback: The status_callback
        :param str status_callback_method: The status_callback_method
        
        :returns: Updated SandboxInstance
        :rtype: SandboxInstance
        """
        return self._context.update(
            voice_url=voice_url,
            voice_method=voice_method,
            sms_url=sms_url,
            sms_method=sms_method,
            status_callback=status_callback,
            status_callback_method=status_callback_method,
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._kwargs.items())
        return '<Twilio.Api.V2010.SandboxInstance {}>'.format(context)
