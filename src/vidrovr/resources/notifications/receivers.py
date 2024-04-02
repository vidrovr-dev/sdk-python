from vidrovr.core import Client

from pydantic import BaseModel, ValidationError

class ReceiversModel(BaseModel):
    """
    Model of a notification receiver.
    
    :param email: Email of the receiver
    :type email: str
    :param id: ID of the receiver
    :type id: str
    :param method: Receiver's delivery method of the notificaton (SLACK, EMAIL, IN_APP, WEBHOOK)
    :type method: str
    :param user_id: User ID of the receiver
    :type user_id: str
    :param slackbot_api_key: Slack API key for delivery of notifications to Slack
    :type slackbot_api_key: str
    :param slack_channel_name: Name of the Slack channel to deliver notifications
    :type slack_channel_name: str
    :param webhook_url: URL of the webhook to use for notification delivery
    :type webhook_url: str
    :param webhook_headers: Webhook headers for the URL
    :type webhook_headers: str
    """
    email: str = None
    id: str = None
    method: str = None
    muted: bool = False
    type: str = None
    user_id: str = None
    slackbot_api_key: str = None
    slack_channel_name: str = None
    webhook_url: str = None
    webhook_headers: str = None

    def __init__(self, **data):
        data.setdefault("email", "Default")
        data.setdefault("id", "Default")
        data.setdefault("method", "Default")
        data.setdefault("muted", False)
        data.setdefault("type", "Default")
        data.setdefault("user_id", "Default")
        data.setdefault("slackbot_api_key", "Default")
        data.setdefault("slack_channel_name", "Default")
        data.setdefault("webhook_url", "Default")
        data.setdefault("webhook_headers", "Default")

        super().__init__(**data)

class Receivers:
    @classmethod
    def create(cls, project_id: str, data: ReceiversModel):
        """
        Create a new receiver

        :param project_id: ID of the project that will contain the receiver
        :type project_id: str
        :param data: Data definition of the new receiver
        :type data: ReceiversModel
        :return: Model of a new receiver
        :rtype: ReceiversModel
        """
        url = f"notifications/{project_id}/receivers"
        payload = {
            "data": {
            }
        }

        # update payload based on method
        if data.method == "EMAIL":
            if data.email is not None:
                if "email" not in payload["data"]:
                    payload["data"]["email"] = data.email

            if data.method is not None:
                if "method" not in payload["data"]:
                    payload["data"]["method"] = data.method

            if data.user_id is not None:
                if "user_id" not in payload["data"]:
                    payload["data"]["user_id"] = data.user_id

        if data.method == "SLACK":
            if data.slackbot_api_key is not None:
                if "slackbot_api_key" not in payload["data"]:
                    payload["data"]["slack_bot_api_key"] = data.slackbot_api_key

            if data.slack_channel_name is not None:
                if "slack_channel_name" not in payload["data"]:
                    payload["data"]["slack_channel_name"] = data.slack_channel_name

            if data.method is not None:
                if "method" not in payload["data"]:
                    payload["data"]["method"] = data.method

            if data.user_id is not None:
                if "user_id" not in payload["data"]:
                    payload["data"]["user_id"] = data.user_id

        if data.method == "IN_APP":
            if data.method is not None:
                if "method" not in payload["data"]:
                    payload["data"]["method"] = data.method

            if data.user_id is not None:
                if "user_id" not in payload["data"]:
                    payload["data"]["user_id"] = data.user_id

        if data.method == "WEBHOOK":
            if data.webhook_url is not None:
                if "webhook_url" not in payload["data"]:
                    payload["data"]["webhook_url"] = data.webhook_url

            if data.webhook_headers is not None:
                if "webhook_headers" not in payload["data"]:
                    payload["data"]["webhook_headers"] = data.webhook_headers

            if data.method is not None:
                if "method" not in payload["data"]:
                    payload["data"]["method"] = data.receiver_type

            if data.user_id is not None:
                if "user_id" not in payload["data"]:
                    payload["data"]["user_id"] = data.user_id                

        response = Client.post(url, payload)

        if response is not None:
            receiver = ReceiversModel(
                email=response["email"],
                id=response["id"],
                method=response["method"],
                muted=response["muted"],
                type=response["type"],
                user_id=response["user_id"]
            )

            return receiver
        else:
            return response            

    @classmethod
    def delete(cls, project_id: str, receiver_id: str):
        """
        Delete a receiver from the project

        :param project_id: ID of the project containing the receiver to delete
        :type proejct_id: str
        :param receiver_id: ID of the receiver to delete
        :type receiver_id: str
        :return: ID of the deleted receiver
        :rtype: ReceiversModel
        """
        url = f"notifications/{project_id}/receivers/{receiver_id}"
        response = Client.delete(url)

        if response is not None:
            message = ReceiversModel(id=response["id"], type=response["type"])

            return message
        else:
            return response


    @classmethod
    def read(cls, project_id: str, receiver_id: str = None):
        """
        Retrieves a list of receivers in the project or data for a specific receiver

        :param project_id: ID of the project
        :type project_id: str
        :param receiver_id: ID of the receiver, default is None
        :type receiver_id: str
        :return: A list of all receivers or a single receiver
        :rtype: list[ReceiversModel] or ReceiversModel
        """
        if receiver_id is None:
            url = f"notifications/{project_id}/receivers"
        else:
            url = f"notifications/{project_id}/receivers/{receiver_id}"
        
        response = Client.get(url)

        if response is not None:
            if isinstance(response, dict):
                receivers = ReceiversModel(
                    email=response["email"],
                    id=response["id"],
                    method=response["method"],
                    muted=response["muted"],
                    type=response["type"],
                    user_id=response["user_id"]
                )
            elif isinstance(response, list):
                receivers = [ReceiversModel(**item) for item in response]

            return receivers
        else:
            return response

    @classmethod
    def update(cls, project_id: str, receiver_id: str, muted: bool): 
        """
        Update a receiver

        :param project_id: ID of the project
        :type project_id: str
        :param receiver_id: ID of the receiver to update
        :type receiver_id: str
        :param muted: Sets the receiver on or off
        :type muted: bool
        :return: An updated receiver
        :rtype: ReceiversModel
        """
        url = f"notifications/{project_id}/receivers/{receiver_id}"
        payload = {
            "data": {
                "muted": muted
            }
        }
        response = Client.patch(url, payload)

        if response is not None:
            receivers = ReceiversModel(
                email=response["email"],
                id=response["id"],
                method=response["method"],
                muted=response["muted"],
                type=response["type"],
                user_id=response["user_id"]
            )

            return receivers
        else:
            return response