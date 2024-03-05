from src.vidrovr.core import Client

from pydantic import BaseModel, ValidationError

class SubscriptionsModel(BaseModel):
    """
    Model of a subscription

    :param creation_date: Creation date of subscription
    :type creation_date: str
    :param event_type_id: ID of the event to subscribe to
    :type event_type_id: str
    :param frequency: Frequency of the subscription deliver, REALTIME, DAILY_DIGEST, WEEKLY_DIGEST
    :type frequency: str
    :param id: ID of the subscription
    :type id: str
    :param owner_id: ID of the owner of the subscription
    :type owner_id: str
    :param resource_id: Resource of the subscription. Either feed ID or saved search ID
    :type resource_id: str
    :param template: Template string of the subscription text
    :type template: str
    :param type: Type of the subscription
    :type type: str
    :param updated_date: Date of subscription update
    :type updated_date: str
    """
    creation_date: str = None
    event_type_id: str = None # comes from get_events
    frequency: str = None # REALTIME, DAILY_DIGEST, WEEKLY_DIGEST
    id: str = None
    owner_id: str = None
    resource_id: str = None # feed_id or saved_search_id
    template: str = None
    type: str = None
    updated_date: str = None

    def __init__(self, **data):
        data.setdefault("creation_date", "Default")
        data.setdefault("event_type_id", "Default")
        data.setdefault("frequency", "Default")
        data.setdefault("id", "Default")
        data.setdefault("owner_id", "Default")
        data.setdefault("resource_id", "Default")
        data.setdefault("template", "Default")
        data.setdefault("type", "Default")
        data.setdefault("updated_date", "Default")

        super().__init__(**data)

class Subscriptions:
    @classmethod
    def create(cls, project_id: str, data: SubscriptionsModel):
        """
        Create a new subscription

        :param project_id: ID of the project containing the subscription
        :type project_id: str
        :param data: Data model for the subscription
        :type data: SubscriptionModel
        :return:
        :rtype: SubscriptionModel
        """
        url = f"notifications/{project_id}/subscriptions"
        payload = {
            'data': {
                'event_type_id': data.event_type_id, 
                'frequency': data.frequency,
                'template': data.template,
                'resource_id': data.resource_id 
            }
        }
        response = Client.post(url, payload)

        if response is not None:
            return response
        else:
            return response

    @classmethod
    def delete(cls, project_id: str, subscription_id: str, is_receivers: bool = False):
        """
        Delete a subscription
        """
        if not is_receivers:
            url = f"notifications/{project_id}/subscriptions/{subscription_id}"
        else:
            url = f"notifications/{project_id}/subscriptions/{subscription_id}/receivers"

        response = Client.delete(url)

        if response is not None:
            subscription = SubscriptionsModel()

            return subscription
        else:
            return response

    @classmethod
    def read(cls, project_id: str, subscription_id: str = None, is_receivers: bool = False):
        """
        Retreive subscriptions for the project
        """
        if not is_receivers:
            if subscription_id is None:
                url = f"notifications/{project_id}/subscriptions"
            else:
                url = f"notifications/{project_id}/receivers/{subscription_id}"
        else:
            url = f"notifications/{project_id}/subscriptions/{subscription_id}/receivers"

        response = Client.get(url)

        if response is not None:
            subscription = SubscriptionsModel()

            return subscription
        else:
            return response

    @classmethod
    def update(cls, project_id: str, subscription_id: str, data: SubscriptionsModel, is_receivers: bool = False):
        """
        Update a subscription
        """
        if not is_receivers:
            url = f"notifications/{project_id}/subscriptions/{subscription_id}"
        else:
            url = f"notifications/{project_id}/subscriptions/{subscription_id}/receivers"

        payload = {
            "data": {

            }
        }

        response = Client.patch(url, payload)

        if response is not None:
            return response
        else:
            return response