from vidrovr.core import Client

from pydantic import BaseModel, ValidationError

class MessagesModel(BaseModel):
    """
    Model of a message.
    
    :param content: Content of the message
    :type content: str
    :param creation_date: Creation date of the message
    :type creation_date: str
    :param id: ID of the message
    :type id: str
    :param read: Indicates if the message has been read
    :type read: bool
    :param receiver_id: ID for the receiver of the message
    :type reeceiver_id: str
    :param status: Status of the message (Pending, Delivered, Failed)
    :type status: str
    :param subscription_id: ID of the subscription for the message
    :type subscription)id: str
    :param type: Type of message
    :type type: str
    :param updated_date: Updated date of the message
    :type updated_date: str
    """
    content: str = None
    creation_date: str = None
    id: str = None
    read: bool = False
    receiver_id: str = None
    status: str = None
    subscription_id: str = None
    type: str = None
    updated_date: str = None

    def __init__(self, **data):
        data.setdefault("content", "Default")
        data.setdefault("creation_date", "Default")
        data.setdefault("id", "Default")
        data.setdefault("read", False)
        data.setdefault("receiver_id", "Default")
        data.setdefault("status", "Default")
        data.setdefault("subscription_id", "Default")
        data.setdefault("type", "Default")
        data.setdefault("updated_date", "Default")

        super().__init__(**data)

class Messages:
    @classmethod
    def delete(cls, project_id: str, message_id: str):
        """
        Delete a specific message

        :param project_id: ID of the project containing the message to delete
        :type project_id: str
        :param message_id: ID of the message to delete
        :type message_id: str
        :return: ID of the deleted message
        :rtype: MessagesModel
        """
        url = f"notifications/{project_id}/messages/{message_id}"
        response = Client.delete(url)

        if response is not None:
            message = MessagesModel(id=response["id"], type=response["type"])

            return message
        else:
            return response

    @classmethod
    def read(cls, project_id: str, message_id: str = None):
        """
        Retrieve a list of messages for a specific project or details on a single message.

        :param project_id: ID of the project containing the messages
        :type project_id: str
        :param message_id: ID of the message, default is None
        :type message_id: str
        :return: A list of message IDs or detail on a single message
        :rtype: list[MessagesModel] or MessagesModel
        """
        if message_id is None:
            url = f"notifications/{project_id}/messages"
        else:
            url = f"notifications/{project_id}/messages/{message_id}"

        response = Client.get(url)

        if response is not None:
            if isinstance(response, dict):
                messages = MessagesModel(
                    content=response["content"],
                    creation_date=response["creation_date"],
                    id=response["id"],
                    read=response["read"],
                    receiver_id=response["receiver_id"],
                    status=response["status"],
                    subscription_id=response["subscription_id"],
                    type=response["type"],
                    updated_date=response["updated_date"]
                )
            elif isinstance(response, list):
                messages = [MessagesModel(**item) for item in response]

            return messages
        else:
            return response

    @classmethod
    def update(cls, project_id: str, message_id: str, read: bool, delivered: bool):
        """
        Update a specific message using the message ID.

        :param project_id: Project ID containing the message
        :type project_id: str
        :param message_id: ID of the message to update
        :type message_id: str
        :param read: Indicates if the message has been read
        :type read: bool
        :param delivered: Indicates if the message has been delivered
        :type delivered: bool
        :return: Updated message model
        :rtype: MessageModel
        """
        url = f"notifications/{project_id}/messages/{message_id}"
        payload = {
            "data": {
                "read": read,
                "delivered": delivered
            }
        }
        response = Client.patch(url, payload)

        if response is not None:
            message = MessagesModel(
                content=response["content"],
                creation_date=response["creation_date"],
                id=response["id"],
                read=response["read"],
                receiver_id=response["receiver_id"],
                status=response["status"],
                subscription_id=response["subscription_id"],
                type=response["type"],
                updated_date=response["updated_date"]
            )

            return message
        else:
            return response
