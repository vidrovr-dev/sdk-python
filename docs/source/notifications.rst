Notifications
=============

Events
------

To retrieve a list of events for a specific project, you can use the
vidrovr.resources.notifications.events.Event object.

.. autopydantic_model:: src.vidrovr.resources.notifications.events.EventsModel

.. autofunction:: src.vidrovr.resources.notifications.events.Events.read

Messages
--------

To delete, retrieve or update messages for a specific project, you can use the 
vidrovr.resources.notifications.messages.Messages object.

.. autopydantic_model:: src.vidrovr.resources.notifications.messages.MessagesModel

.. autofunction:: src.vidrovr.resources.notifications.messages.Messages.delete

.. autofunction:: src.vidrovr.resources.notifications.messages.Messages.read

.. autofunction:: src.vidrovr.resources.notifications.messages.Messages.update

Receivers
---------

To create, delete, retrieve or update receivers for a notification in a specific project, 
you can use the vidrovr.resources.notifications.messages.Messages object.

.. autopydantic_model:: src.vidrovr.resources.notifications.receivers.ReceiversModel

.. autofunction:: src.vidrovr.resources.notifications.receivers.Receivers.create

.. autofunction:: src.vidrovr.resources.notifications.receivers.Receivers.delete

.. autofunction:: src.vidrovr.resources.notifications.receivers.Receivers.read

.. autofunction:: src.vidrovr.resources.notifications.receivers.Receivers.updaate

Subscriptions
-------------

To create, delete, retrieve or update subscribers for a notification in a specific project, 
you can use the vidrovr.resources.notifications.subscriptions.Subscriptions object.

.. autopydantic_model:: src.vidrovr.resources.notifications.subscriptions.SubscriptionsModel

.. autofunction:: src.vidrovr.resources.notifications.subscriptions.Subscriptions.create

.. autofunction:: src.vidrovr.resources.notifications.subscriptions.Subscriptions.delete

.. autofunction:: src.vidrovr.resources.notifications.subscriptions.Subscriptions.read

.. autofunction:: src.vidrovr.resources.notifications.subscriptions.Subscriptions.updaate