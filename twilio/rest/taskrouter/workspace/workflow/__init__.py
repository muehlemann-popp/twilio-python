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
from twilio.rest.taskrouter.workspace.workflow.statistics import (
    Statistics,
    StatisticsList,
)
from twilio.rest.resources.base import NextGenListResource


class Workflow(NextGenInstanceResource):
    """
    .. attribute:: account_sid
    
        The account_sid
    
    .. attribute:: assignment_callback_url
    
        The assignment_callback_url
    
    .. attribute:: configuration
    
        The configuration
    
    .. attribute:: date_created
    
        The date_created
    
    .. attribute:: date_updated
    
        The date_updated
    
    .. attribute:: document_content_type
    
        The document_content_type
    
    .. attribute:: fallback_assignment_callback_url
    
        The fallback_assignment_callback_url
    
    .. attribute:: friendly_name
    
        The friendly_name
    
    .. attribute:: sid
    
        The sid
    
    .. attribute:: task_reservation_timeout
    
        The task_reservation_timeout
    
    .. attribute:: workspace_sid
    
        The workspace_sid
    """
    id_key = "sid"
    subresources = [
        StatisticsList
    ]

    def load(self, *args, **kwargs):
        super(Workflow, self).load(*args, **kwargs)
        
        if hasattr(self, "date_created") and self.date_created:
            self.date_created = deserialize.iso8601_datetime(self.date_created)
        
        if hasattr(self, "date_updated") and self.date_updated:
            self.date_updated = deserialize.iso8601_datetime(self.date_updated)

    def update(self, **kwargs):
        """
        Update the instance
        
        :param str assignment_callback_url: The assignment_callback_url
        :param str configuration: The configuration
        :param str fallback_assignment_callback_url: The
            fallback_assignment_callback_url
        :param str friendly_name: The friendly_name
        :param str task_reservation_timeout: The task_reservation_timeout
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`UpdateQuery`
        :returns: An UpdateQuery when executed returns a new instance of the updated :class:`Workflow`
        """
        return self.update_instance(kwargs)

    def delete(self):
        """
        Delete the instance
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`DeleteQuery`
        :returns: A DeleteQuery when executed returns True iff the deletion is successful
        """
        return self.delete_instance()


class Workflows(NextGenListResource):
    name = "Workflows"
    mount_name = "workflows"
    key = "workflows"
    instance = Workflow

    def __init__(self, *args, **kwargs):
        super(Workflows, self).__init__(*args, **kwargs)

    def get(self, sid):
        """
        Get a placeholder for an instance resource.
        
        :param str sid: The sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`Workflow`
        :returns: A placeholder for a :class:`Workflow` resource
        """
        return self.get_instance(sid)

    def update(self, sid, friendly_name=None, assignment_callback_url=None,
               fallback_assignment_callback_url=None, configuration=None,
               task_reservation_timeout=None, **kwargs):
        """
        Update a :class:`Workflow`
        
        :param str assignment_callback_url: The assignment_callback_url
        :param str configuration: The configuration
        :param str fallback_assignment_callback_url: The
            fallback_assignment_callback_url
        :param str friendly_name: The friendly_name
        :param str sid: The sid
        :param str task_reservation_timeout: The task_reservation_timeout
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`UpdateQuery`
        :returns: An UpdateQuery when executed returns an instance of the updated :class:`Workflow`
        """
        kwargs['FriendlyName'] = friendly_name
        kwargs['AssignmentCallbackUrl'] = assignment_callback_url
        kwargs['FallbackAssignmentCallbackUrl'] = fallback_assignment_callback_url
        kwargs['Configuration'] = configuration
        kwargs['TaskReservationTimeout'] = task_reservation_timeout
        return self.update_instance(sid, kwargs)

    def delete(self, sid):
        """
        Delete the :class:`Workflow`
        
        :param str sid: The sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`DeleteQuery`
        :returns: A DeleteQuery when executed returns True iff the deletion is successful
        """
        return self.delete_instance(sid)

    def list(self, friendly_name=None, **kwargs):
        """
        Retrieve a collection of :class:`Workflow`
        
        :param str friendly_name: The friendly_name
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`ListQuery`
        :returns: A ListQuery when executed returns a list of :class:`Workflow`
        """
        kwargs['FriendlyName'] = friendly_name
        return self.get_instances(kwargs)

    def create(self, friendly_name, configuration, assignment_callback_url,
               fallback_assignment_callback_url=None, task_reservation_timeout=None,
               **kwargs):
        """
        Create a new :class:`Workflow`
        
        :param str assignment_callback_url: The assignment_callback_url
        :param str configuration: The configuration
        :param str fallback_assignment_callback_url: The
            fallback_assignment_callback_url
        :param str friendly_name: The friendly_name
        :param str task_reservation_timeout: The task_reservation_timeout
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`CreateQuery`
        :returns: A CreateQuery when executed returns an instance of the created :class:`Workflow`
        """
        kwargs['FriendlyName'] = friendly_name
        kwargs['Configuration'] = configuration
        kwargs['AssignmentCallbackUrl'] = assignment_callback_url
        kwargs['FallbackAssignmentCallbackUrl'] = fallback_assignment_callback_url
        kwargs['TaskReservationTimeout'] = task_reservation_timeout
        return self.create_instance(kwargs)

    def iter(self, friendly_name=None, **kwargs):
        """
        Return all instances of :class:`Workflow` using an iterator
        
        :param str friendly_name: The friendly_name
        
        :raises TwilioRestException: when the request fails on execute
        
        :returns: An iterator to fetch all :class:`Workflow`
        """
        kwargs['FriendlyName'] = friendly_name
        return super(Workflows, self).iter(**kwargs)
