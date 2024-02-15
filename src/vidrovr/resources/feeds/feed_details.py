from src.vidrovr.core import Client

from pydantic import BaseModel


class FeedDetailModel(BaseModel):
    """
    Model of detail data for a feed.

    :param type: Type of the feed
    :type type: str
    :param id: ID of the feed
    :type id: str
    :param creation_date: Date the feed  was created
    :type creation_date: str
    :param is_active: Indicates of the feed is on or off
    :type is_active: bool
    :param name: Name of the feed
    :type name: str
    :param next_poll_date: Next date for polling the feed
    :type next_poll_date: str
    :param polling_frequency: Frequency for polling the feed
    :type polling_frequency: int
    :param query_parameters: Does something?
    :type query_parameters: str
    :param status: Status of the feed
    :type status: str
    :param updated_date: Last date the feed was updated
    :type updated_date: str
    """

    type: str = None
    id: str = None
    creation_date: str = None
    is_active: bool = False
    name: str = None
    next_poll_date: str = None
    num_feed_items: str = None
    polling_frequency: int = 0
    query_parameters: str = None
    status: str = None
    updated_date: str = None


class FeedDetail:
    @classmethod
    def read(cls, feed_id: str, project_id: str):
        """
        Retreive information about a specific feed.

        :param feed_id: ID of the feed item
        :type feed_id: str
        :param project_id: ID of the project containing the feed
        :type project_id: str
        :return: Information about the feed
        :rtype: FeedDetailData
        """
        url = f"feeds/{feed_id}?project_uid={project_id}"
        response = Client.get(url)

        if response is not None:
            feed_detail = FeedDetailModel(
                type=response["type"],
                id=response["id"],
                creation_date=response["creation_date"],
                is_active=response["is_active"],
                name=response["name"],
                next_poll_date=response["next_poll_date"],
                num_feed_items=response["num_feed_items"],
                polling_frequency=response["polling_frequency"],
                query_parameters=response["query_parameters"],
                status=response["status"],
                updated_date=response["updated_date"],
            )

            return feed_detail
        else:
            return response
