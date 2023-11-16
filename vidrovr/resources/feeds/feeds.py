from vidrovr.core import Client

from pydantic import BaseModel, ValidationError, validator

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
    id: str = None
    type: str = None
    name: str = 'Default'
    profile: str = None
    hashtag: str = None
    polling_freq: int = 3600
    media_type: str = None
    link: str = None
    segment_length: int = 3
    project_uids: list[str] = None

    @validator("name", pre=True)
    def check_name(cls, value):
        if value is None:
            value = 'Default'

        return value
    
    @validator("polling_freq", pre=True)
    def check_polling_freq(cls, value):
        if value is None:
            value = 3600

        return value
    
    @validator("segment_length", pre=True)
    def check_segment_length(cls, value):
        if value is None:
            value = 3

        return value

class Feed:

    @classmethod
    def read(cls, project_id: str):
        """
        Returns a list of all feeds created by the user, including the name and the unique identifier of the feed.

        :param project_id: ID of the project to retrieve feeds from
        :type project_id: str
        :return: A list of all feeds in the project
        :rtype: list[FeedModel]
        """
        url      = f'feeds/?project_uid={project_id}'
        response = Client.get(url)
        feeds    = []

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