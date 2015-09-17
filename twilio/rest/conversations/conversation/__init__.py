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
from twilio.rest.conversations.conversation.participant import (
    Participant,
    Participants,
)
from twilio.rest.resources.base import NextGenListResource
from twilio.rest.conversations.conversation.in_progress import (
    InProgresses,
    InProgress,
)
from twilio.rest.conversations.conversation.completed import (
    Completeds,
    Completed,
)


class Conversation(NextGenInstanceResource):
    """
    .. attribute:: sid
    
        The sid
    
    .. attribute:: status
    
        The status
    
    .. attribute:: duration
    
        The duration
    
    .. attribute:: date_created
    
        The date_created
    
    .. attribute:: start_time
    
        The start_time
    
    .. attribute:: end_time
    
        The end_time
    
    .. attribute:: account_sid
    
        The account_sid
    
    .. attribute:: url
    
        The url
    """
    id_key = "sid"
    CREATED = "created"
    ENDED = "ended"
    FAILED = "failed"
    IN_PROGRESS = "in-progress"
    subresources = [
        Participants
    ]

    def load(self, *args, **kwargs):
        super(Conversation, self).load(*args, **kwargs)
        
        if hasattr(self, "date_created") and self.date_created:
            self.date_created = deserialize.iso8601_datetime(self.date_created)
        
        if hasattr(self, "start_time") and self.start_time:
            self.start_time = deserialize.iso8601_datetime(self.start_time)
        
        if hasattr(self, "end_time") and self.end_time:
            self.end_time = deserialize.iso8601_datetime(self.end_time)


class Conversations(NextGenListResource):
    name = "Conversations"
    mount_name = "conversations"
    key = "conversations"
    instance = Conversation

    def __init__(self, *args, **kwargs):
        super(Conversations, self).__init__(*args, **kwargs)
        self.in_progress = InProgresses(*args, **kwargs)
        self.completed = Completeds(*args, **kwargs)

    def get(self, sid):
        """
        Get a placeholder for an instance resource.
        
        :param str sid: The sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`Conversation`
        :returns: A placeholder for a :class:`Conversation` resource
        """
        return self.get_instance(sid)
