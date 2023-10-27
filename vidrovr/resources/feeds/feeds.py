from ...core import Client

from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class FeedData:
    type: str
    id: str
    name: str

@dataclass
class FeedItem:
    """
    Object for creating a new feed

    :param feed_type: Type of feed to create: youtube, instagram_profile, instagram_hastag, facebook_profile, hls
    :type feed_type: str
    :param name: Name of the feed
    :type name: str
    :param media_type: A thing
    """
    feed_type: str
    name: str
    media_type: str
    hls_link: str
    project_uids: str

class Feed(BaseModel):

    @classmethod
    def read(cls, project_id: str):
        """
        Returns a list of all feeds created by the user, including the name and the unique identifier of the feed.

        :param project_id: ID of the project to retrieve feeds from
        :type project_id: str
        :return: A list of all feeds in the project
        :rtype: list[FeedData]
        """
        url      = f'feeds/?project_uid={project_id}'
        response = Client.get(url)

        if isinstance(response, dict):
            feed_object = FeedData(
                type=response['type'],
                id=response['id'],
                name=response['name']
            )
        elif isinstance(response, list):
            feed_object = [FeedData(**item) for item in response]

        return feed_object
    
    @classmethod
    def delete(cls, feed_id: str, project_id: str):
        """
        Deletes a Feed from the Project, the media assets from that feed will not be deleted.

        :param feed_id: ID of the feed to delete
        :type feed_id: str
        :param project_id: ID of the project containing the feed to delete
        :type feed_id: str
        :return: JSON string of the HTTP response
        :rtype: str
        """
        url      = f'feeds/{feed_id}?project_uid={project_id}'
        response = Client.delete(url)

        return response
    
    @classmethod
    def update(cls, feed_id: str, project_id: str, status: bool):
        """
        Change the is_active property of a Feed. If set to false, Vidrovr will not 
        ingest data from that Feed. When set to true, Vidrovr will start polling media 
        as scheduled in the Feed.

        :param feed_id: ID of the feed to update
        :type feed_id: str
        :param project_id: ID of the project containing the feed to update
        :type project_id: str
        :param status: Status of the feed
        :type status: bool
        :return: JSON string of the HTTP response
        :rtype: str
        """
        url = f'feeds/{feed_id}'
        payload = {
            'data': {
                'is_active': status,
                'project_uids': project_id
            }
        }
        response = Client.patch(url, payload)

        return response
    
    @classmethod
    def create(cls, data: FeedItem):
        """
        Creates a feed which Vidrovr will poll to ingest data into the system.

        :param data: Dataclass object contiaining the info to create a feed
        :type data: FeedItem
        :return: JSON string containing the HTTP response
        :rtype: str
        """
        url     = 'feeds/'
        payload = {
            'data': {
                'feed_type': data.feed_type,
                'name': data.name,
                'media_type': data.media_type,
                'hls_link': data.hls_link,
                'project_uids': [data.project_uids]
            }
        }
        response = Client.post(url, payload)

        return response