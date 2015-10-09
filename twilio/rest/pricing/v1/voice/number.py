# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import values
from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource


class NumberContext(InstanceContext):

    def __init__(self, version, number):
        """
        Initialize the NumberContext
        
        :param Version version
        :param number: The number
        
        :returns: NumberContext
        :rtype: NumberContext
        """
        super(NumberContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'number': number,
        }
        self._uri = '/Voice/Numbers/{number}'.format(**self._kwargs)

    def fetch(self):
        """
        Fetch a NumberInstance
        
        :returns: Fetched NumberInstance
        :rtype: NumberInstance
        """
        params = values.of({})
        
        return self._version.fetch(
            NumberInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._kwargs.items())
        return '<Twilio.Pricing.V1.NumberContext {}>'.format(context)


class NumberInstance(InstanceResource):

    def __init__(self, version, payload, number=None):
        """
        Initialize the NumberInstance
        
        :returns: NumberInstance
        :rtype: NumberInstance
        """
        super(NumberInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'number': payload['number'],
            'country': payload['country'],
            'iso_country': payload['iso_country'],
            'outbound_call_price': payload['outbound_call_price'],
            'inbound_call_price': payload['inbound_call_price'],
            'price_unit': payload['price_unit'],
            'uri': payload['uri'],
        }
        
        # Context
        self._instance_context = None
        self._kwargs = {
            'number': number or self._properties['number'],
        }

    @property
    def _context(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context
        
        :returns: NumberContext for this NumberInstance
        :rtype: NumberContext
        """
        if self._instance_context is None:
            self._instance_context = NumberContext(
                self._version,
                self._kwargs['number'],
            )
        return self._instance_context

    @property
    def number(self):
        """
        :returns: The number
        :rtype: str
        """
        return self._properties['number']

    @property
    def country(self):
        """
        :returns: The country
        :rtype: str
        """
        return self._properties['country']

    @property
    def iso_country(self):
        """
        :returns: The iso_country
        :rtype: str
        """
        return self._properties['iso_country']

    @property
    def outbound_call_price(self):
        """
        :returns: The outbound_call_price
        :rtype: str
        """
        return self._properties['outbound_call_price']

    @property
    def inbound_call_price(self):
        """
        :returns: The inbound_call_price
        :rtype: str
        """
        return self._properties['inbound_call_price']

    @property
    def price_unit(self):
        """
        :returns: The price_unit
        :rtype: str
        """
        return self._properties['price_unit']

    @property
    def uri(self):
        """
        :returns: The uri
        :rtype: str
        """
        return self._properties['uri']

    def fetch(self):
        """
        Fetch a NumberInstance
        
        :returns: Fetched NumberInstance
        :rtype: NumberInstance
        """
        return self._context.fetch()

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._kwargs.items())
        return '<Twilio.Pricing.V1.NumberInstance {}>'.format(context)