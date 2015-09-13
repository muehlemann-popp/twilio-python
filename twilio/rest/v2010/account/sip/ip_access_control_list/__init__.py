# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio.rest.resources.util import (
    parse_date,
    parse_iso_date,
)
from twilio.rest.resources.base import InstanceResource
from twilio.rest.v2010.account.sip.ip_access_control_list.ip_address import (
    IpAddress,
    IpAddresses,
)
from twilio.rest.resources.base import ListResource


class IpAccessControlList(InstanceResource):
    """
    .. attribute:: sid
    
        A 34 character string that uniquely identifies this resource.
    
    .. attribute:: account_sid
    
        The unique id of the Account that sent this message.
    
    .. attribute:: friendly_name
    
        A human readable descriptive text, up to 64 characters long.
    
    .. attribute:: date_created
    
        The date that this resource was created, given as GMT in RFC 2822
        format.
    
    .. attribute:: date_updated
    
        The date that this resource was last updated, given as GMT in RFC 2822
        format.
    
    .. attribute:: subresource_uris
    
        The subresource_uris
    
    .. attribute:: uri
    
        The URI for this resource, relative to `https://api.twilio.com`
    """
    id_key = "sid"
    subresources = [
        IpAddresses
    ]

    def load(self, *args, **kwargs):
        super(IpAccessControlList, self).load(*args, **kwargs)
        
        if hasattr(self, "date_created") and self.date_created:
            self.date_created = parse_iso_date(self.date_created)
        
        if hasattr(self, "date_updated") and self.date_updated:
            self.date_updated = parse_iso_date(self.date_updated)

    def update(self, **kwargs):
        """
        Rename an IpAccessControlList
        
        :param str friendly_name: A human readable descriptive text, up to 64 characters
            long.
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`UpdateQuery`
        :returns: An UpdateQuery when executed returns a new instance of the updated :class:`IpAccessControlList`
        """
        return self.update_instance(kwargs)

    def delete(self):
        """
        Delete an IpAccessControlList from the requested account
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`DeleteQuery`
        :returns: A DeleteQuery when executed returns True iff the deletion is successful
        """
        return self.delete_instance()


class IpAccessControlLists(ListResource):
    name = "SIP/IpAccessControlLists"
    mount_name = "ip_access_control_lists"
    key = "ip_access_control_lists"
    instance = IpAccessControlList

    def __init__(self, *args, **kwargs):
        super(IpAccessControlLists, self).__init__(*args, **kwargs)

    def list(self, **kwargs):
        """
        Retrieve a list of ip-access-control-lists belonging to the account used to make the request
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`ListQuery`
        :returns: A ListQuery when executed returns a list of :class:`IpAccessControlList`
        """
        return self.get_instances(kwargs)

    def create(self, friendly_name, **kwargs):
        """
        Create a new IpAccessControlList resource
        
        :param str friendly_name: A human readable descriptive text, up to 64 characters
            long.
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`CreateQuery`
        :returns: A CreateQuery when executed returns an instance of the created :class:`IpAccessControlList`
        """
        kwargs["FriendlyName"] = friendly_name
        return self.create_instance(kwargs)

    def get(self, sid):
        """
        Fetch a specific instance of an IpAccessControlList
        
        :param str sid: The ip-access-control-list Sid that uniquely identifies this
            resource
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`IpAccessControlList`
        :returns: A placeholder for a :class:`IpAccessControlList` resource
        """
        return self.get_instance(sid)

    def update(self, sid, friendly_name, **kwargs):
        """
        Rename an IpAccessControlList
        
        :param str friendly_name: A human readable descriptive text, up to 64 characters
            long.
        :param str sid: The sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`UpdateQuery`
        :returns: An UpdateQuery when executed returns an instance of the updated :class:`IpAccessControlList`
        """
        kwargs["FriendlyName"] = friendly_name
        return self.update_instance(sid, kwargs)

    def delete(self, sid):
        """
        Delete an IpAccessControlList from the requested account
        
        :param str sid: The ip-access-control-list Sid that uniquely identifies this
            resource
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`DeleteQuery`
        :returns: A DeleteQuery when executed returns True iff the deletion is successful
        """
        return self.delete_instance(sid)

    def iter(self, **kwargs):
        """
        Retrieve a list of ip-access-control-lists belonging to the account used to make the request
        
        :raises TwilioRestException: when the request fails on execute
        
        :returns: An iterator to fetch all :class:`IpAccessControlList`
        """
        return super(IpAccessControlLists, self).iter(**kwargs)