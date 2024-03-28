from src.vidrovr.core import Client

from pydantic import BaseModel, ValidationError
from typing import Dict, Union


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
    :param template: Template string of the subscription text. Currently not implemented.
    :type template: str
    :param type: Type of the subscription
    :type type: str
    :param updated_date: Date of subscription update
    :type updated_date: str
    """

    creation_date: str = None
    event_type_id: str = None  # comes from get_events
    frequency: str = None
    id: str = None
    owner_id: str = None
    resource_id: str = None
    # template: str = None
    type: str = None
    updated_date: str = None
    receiver_ids: list[str] = None

    def __init__(self, **data):
        data.setdefault("creation_date", "Default")
        data.setdefault("event_type_id", "Default")
        data.setdefault("frequency", "Default")
        data.setdefault("id", "Default")
        data.setdefault("owner_id", "Default")
        data.setdefault("resource_id", "Default")
        # data.setdefault("template", "Default")
        data.setdefault("type", "Default")
        data.setdefault("updated_date", "Default")
        data.setdefault("receiver_ids", [])

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
            "data": {
                "event_type_id": data.event_type_id,
                "frequency": data.frequency,
                #'template': data.template,
                "resource_id": data.resource_id,
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
            url = (
                f"notifications/{project_id}/subscriptions/{subscription_id}/receivers"
            )

        response = Client.delete(url)

        if response is not None:
            subscription = SubscriptionsModel()

            return subscription
        else:
            return response

    @classmethod
    def read(
        cls, project_id: str, subscription_id: str = None, is_receivers: bool = False
    ):
        """
        Retreive subscriptions for the project

        :param project_id: ID of the project
        :type project_id: str
        :param subscription_id: ID of the subscription. Set to None to retrieve all subscriptions.
        :type subscription_id: str
        :param is_receivers: Set to True to retrieve the recevier IDs for a specific subscription ID.
        :type is_receivers: bool
        :return: Info for all subscriptions, a specific subscription or a list of receivers
        :rtype: SubscriptionModel or list[SubscriptionModel]
        """
        if not is_receivers:
            if subscription_id is None:
                url = f"notifications/{project_id}/subscriptions"
            else:
                url = f"notifications/{project_id}/subscriptions/{subscription_id}"
        else:
            url = (
                f"notifications/{project_id}/subscriptions/{subscription_id}/receivers"
            )

        response = Client.get(url)

        if response is not None:
            if isinstance(response, dict):
                subscription = SubscriptionsModel(
                    creation_date=response["creation_date"],
                    event_type_id=response["event_type_id"],
                    frequency=response["frequency"],
                    id=response["id"],
                    owner_id=response["owner_id"],
                    resource_id=response["resource_id"],
                    # template = response["template"],
                    type=response["type"],
                    updated_date=response["updated_date"],
                )
            elif isinstance(response, list):
                subscription = [SubscriptionsModel(**item) for item in response]

            return subscription
        else:
            return response

    @classmethod
    def update(
        cls,
        project_id: str,
        subscription_id: str,
        data: SubscriptionsModel,
        is_receivers: bool = False,
    ):
        """
        Update a subscription

        :param project_id: ID of the project
        :type project_id: str
        :param subscription_id: ID of the subscription
        :type subscription_id: str
        :param data: Information to update the subscription or the subscription receivers
        :type data: SubscriptionModel
        :param is_receviers: Indicates whether the update is for a subscription or the subscription receivers. Default is false.
        :type is_receivers: bool
        :return: Something
        :rtype: Something else
        """
        if not is_receivers:
            url = f"notifications/{project_id}/subscriptions/{subscription_id}"
            payload = {
                "data": {
                    "event_type_id": data.event_type_id,
                    "frequency": data.frequency,
                }
            }
        else:
            url = (
                f"notifications/{project_id}/subscriptions/{subscription_id}/receivers"
            )
            payload = {"data": {"receiver_ids": data.receiver_ids}}

        response = Client.patch(url, payload)

        if response is not None:
            return response
        else:
            return response
