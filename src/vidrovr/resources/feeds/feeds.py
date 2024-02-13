from src.vidrovr.core import Client

from pydantic import BaseModel, ValidationError 
from typing import Dict, Union

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
    additional_metadata: str = None
    creation_date: str = None
    is_active: bool = True
    next_poll_date: str = None
    num_feed_items: int = 0
    priority: int = 0
    query_parameters: Dict[str, Union[str, int]] = None
    status: str = None
    updated_date: str = None
    name: str = "Default"
    profile: str = None
    hashtag: str = None
    polling_freq: int = 3600
    media_type: str = None
    link: str = None
    segment_length: int = 3
    project_uids: list[str] = None

    def __init__(self, **data):
        default_dict = {'default_key': 'default_value'}

        data.setdefault("additional_metadata", "Default")
        data.setdefault("creation_date", "Default")
        data.setdefault("is_active", True)
        data.setdefault("next_poll_date", "Default")
        data.setdefault("num_feed_items", 0)
        data.setdefault("priority", 0)
        data.setdefault("query_parameters", default_dict)
        data.setdefault("status", "Default")
        data.setdefault("updated_date", "Default")
        data.setdefault("name", "Default")
        data.setdefault("profile", "Default")
        data.setdefault("hashtag", "Default")
        data.setdefault("polling_freq", 3600)
        data.setdefault("media_type", "Default")
        data.setdefault("link", "Default")
        data.setdefault("segment_length", 3)
        data.setdefault("project_uids", [])

        super().__init__(**data)

class Feed:
    @classmethod
    def read(cls, feed_id: str, project_id: str):
        """
        Returns a list of all feeds created by the user, including the name and the unique identifier of the feed.

        :param project_id: ID of the project to retrieve feeds from
        :type project_id: str
        :return: A list of all feeds in the project
        :rtype: list[FeedModel]
        """
        if feed_id is None:
            url = f"feeds/?project_uid={project_id}"
        else:
            url = f"feeds/{feed_id}?project_uid={project_id}"

        response = Client.get(url)

        if response is not None:
            
            if isinstance(response, dict):
                feed = FeedModel(
                    id=response["id"],
                    type=response["type"],
                    creation_date=response["creation_date"],
                    is_active=response["is_active"],
                    next_poll_date=response["next_poll_date"],
                    num_feed_items=response["num_feed_items"],
                    priority=response["priority"],
                    query_parameters=response["query_parameters"],
                    status=response["status"],
                    updated_date=response["updated_date"],
                    name=response["name"],
                )
            elif isinstance(response, list):
                feed = [FeedModel(**item) for item in response]

        return feed

    @classmethod
    def delete(cls, feed_id: str, project_id: str):
        """
        Deletes a Feed from the Project, the media assets from that feed will not be deleted.

        :param feed_id: ID of the feed to delete
        :type feed_id: str
        :param project_id: ID of the project containing the feed to delete
        :type feed_id: str
        :return: A FeedModel on success
        :rtype: FeedModel
        """
        url = f"feeds/{feed_id}?project_uid={project_id}"
        response = Client.delete(url)

        if response is not None:
            feed = FeedModel(id=response["id"], type=response["type"])

            return feed
        else:
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
        :return: A FeedModel on success
        :rtype: FeedModel
        """
        url = f"feeds/{feed_id}"
        payload = {"data": {"is_active": status, "project_uid": project_id}}
        response = Client.patch(url, payload)

        if response is not None:
            feed = FeedModel(
                additional_metadata=response["additional_metadata"],
                creation_date=response["creation_date"],
                id=response["id"],
                is_active=response["is_active"],
                name=response["name"],
                next_poll_date=response["next_poll_date"],
                num_feed_items=response["num_feed_items"],
                polling_freq=response["polling_frequency"],
                priority=response["priority"],
                query_parameters=response["query_parameters"],
                status=response["status"],
                type=response["type"],
                updated_date=response["updated_date"],
            )

            return feed
        else:
            return response

    @classmethod
    def create(cls, data: FeedModel):
        """
        Creates a feed which Vidrovr will poll to ingest data into the system.

        :param data: FeedModel object containing the info to create a feed
        :type data: FeedModel
        :return: A FeedModel on success
        :rtype: FeedModel
        """
        url = "feeds/"
        payload = {
            "data": {
                "name": data.name,
                "polling_frequency": data.polling_freq,
                "project_uids": data.project_uids,
                "feed_type": data.type,
            }
        }

        # put the url in the right slot
        if data.type == "youtube":
            if "youtube_url" not in payload["data"]:
                payload["data"]["youtube_url"] = data.link
        elif data.type == "hls":
            if "hls_link" not in payload["data"]:
                payload["data"]["hls_link"] = data.link
        elif data.type == "rtmp":
            if "rtmp_link" not in payload["data"]:
                payload["data"]["rtmp_link"] = data.link
        elif data.type == "rtsp":
            if "rtsp_link" not in payload["data"]:
                payload["data"]["rtsp_link"] = data.link

        # check for optional items
        if data.profile is not None:
            if "profile" not in payload["data"]:
                payload["data"]["profile"] = data.profile

        if data.hashtag is not None:
            if "hashtag" not in payload["data"]:
                payload["data"]["hashtag"] = data.hashtag

        if data.media_type is not None:
            if "media_type" not in payload["data"]:
                payload["data"]["media_type"] = data.media_type

        response = Client.post(url, payload)

        if response is not None:
            feed = FeedModel(id=response["id"], name=response["name"])

            return feed
        else:
            return response
