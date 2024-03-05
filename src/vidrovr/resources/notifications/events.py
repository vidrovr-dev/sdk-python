from src.vidrovr.core import Client

from pydantic import BaseModel, ValidationError

class EventsModel(BaseModel):
    """
    Model of events list

    :param description: Event description
    :type description: str
    :param id: ID of the evnt
    :type id: str
    :param name: Name of the event
    :type name: str
    :param type: Type of event
    :type type: str
    """
    description: str = None
    id: str = None
    name: str = None
    type: str = None

class Events:
    @classmethod
    def read(cls, project_id: str):
        """
        Returns a list of all events for the given project ID.

        :param project_id: ID of the project
        :type project_id: str
        :return: A list of events
        :rtype: list[EventsModel]
        """
        url = f"notifications/{project_id}/events"

        response = Client.get(url)

        if response is not None:
            events = [EventsModel(**item) for item in response]

            return events
        else:
            return response