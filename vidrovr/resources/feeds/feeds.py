import json

from ...core import Client

from typing import Optional
from pydantic import BaseModel, ValidationError, Field
from icecream import ic

class BaseResource(BaseModel):
    type: str
    id: str

class FeedModel(BaseModel):
    """
    Model of a feed

    :param id: ID value of the feed
    :type id: str
    :param type: Type of feed to create: youtube, twitter_profile, twitter_hashtag, instagram_profile, instagram_hastag, facebook_profile, hls, rtmp, rtsp
    :type type: str
    :param name: Name of the feed, optional
    :type name: str
    :param profile: Account handle for twitter, instagram and facebook. Required if type is twitter_profile, instagram_profile or facebook_profile
    :type profile: str
    :param hashtag: Name of the hashtag without the # symbol. Required if type is twitter_hashtag, instagram_hashtag or facebook_hashtag
    :type hashtag: str
    :param polling_freq: Polling frequency for the feed in seconds. Defaults to 3600.
    :type polling_freq: int
    :param media_type: Type of media in the feed: video, image, user_upload
    :type media_type: str
    :param link: URL of the HLS, rtmp, rtsp or YouTube stream
    :type link: str
    :param segment_length: Segment length of the RTMP feed in minutes. Defaults to 3.
    :type segment_length: int
    :param project_uids: Project ID that this feed will be associated with
    :type project_uids: str
    """
    id: Optional[str] = Field(default=None)
    type: str = Field(default=None)
    name: Optional[str] = Field(default="Default")
    profile: Optional[str] = Field(default=None)
    hashtag: Optional[str] = Field(default=None)
    polling_freq: int = Field(default=3600)
    media_type: Optional[str] = Field(default=None)
    link: str = Field(default="Default")
    segment_length: Optional[int] = Field(default=3)
    project_uids: str = Field(default=None)

    def __init__(self, **data):
        data['id']             = data.get('id', None)
        data['type']           = data.get('type', None)
        data['name']           = data.get('name', 'Default')
        data['profile']        = data.get('profile', None)
        data['hashtag']        = data.get('hashtag', None)
        data['polling_freq']   = data.get('polling_freq', 3600) 
        data['media_type']     = data.get('media_type', None)
        data['link']           = data.get('link', 'Default')
        data['segment_length'] = data.get('segment_length', 3)
        data['project_uids']   = data.get('id', None)

        super().__init__(**data)

class Feed:

    @classmethod
    def read(cls, project_id: str) -> FeedModel:
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
            feed = FeedModel(
                id=response['id'],
                feed_type=response['type'],
                name=response['name']
            )
        elif isinstance(response, list):
            feeds = []

            for item in response:
                try:
                    feed = FeedModel(
                        id=item['id'],
                        type=item['type'],
                        name=item['name']
                    )
                    feeds.append(feed)
                except ValidationError as e:
                    print(f'Feed.read(): Validation error for {item}: {e}')

        return feeds
    
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
    def create(cls, data: FeedModel):
        """
        Creates a feed which Vidrovr will poll to ingest data into the system.

        :param data: FeedModel object contiaining the info to create a feed
        :type data: FeedModel
        :return: JSON string containing the HTTP response
        :rtype: str
        """
        url     = 'feeds/'
        payload = {
            'data': {
                'name': data.name,
                'polling_frequency': data.polling_freq,
                'project_uids': [data.project_uids],
                'feed_type': data.type
            }
        }

        # put the url in the right slot
        if data.type == 'youtube':
            if 'youtube_url' not in payload['data']:
                payload['data']['youtube_url'] = data.link
        elif data.type == 'hls':
            if 'hls_link' not in payload['data']:
                payload['data']['hls_link'] = data.link
        elif data.type == 'rtmp':
            if 'rtmp_link' not in payload['data']:
                payload['data']['rtmp_link'] = data.link
        elif data.type == 'rtsp':
            if 'rtsp_link' not in payload['data']:
                payload['data']['rtsp_link'] = data.link

        # check for optional items
        if data.profile is not None:
            if 'profile' not in payload['data']:
                payload['data']['profile'] = data.profile

        if data.hashtag is not None:
            if 'hashtag' not in payload['data']:
                payload['data']['hashtag'] = data.hashtag

        if data.media_type is not None:
            if 'media_type' not in payload['data']:
                payload['data']['media_type'] = data.media_type

        response = Client.post(url, payload)

        return response