from vidrovr.core.client import Client

from pydantic import BaseModel


class AssetItemModel(BaseModel):
    """
    Model of an asset item

    :param creation_date: Date the asset was created
    :type creation_date: str
    :param duration: Length of the asset
    :type duration: float
    :param feed_id: ID of the feed the asset is associated with
    :type feed_id: str
    :param fps: FPS of the asset
    :type fps: float
    :param height: Height of the asset in pixels
    :type height: int
    :param asset_id: ID of the asset
    :type asset_id: str
    :param media_url: Cloudfront URL of the asset
    :type media_url: str
    :param mime_type: MIME type of the asset
    :type mime_type: str
    :param processing_info: Processing start and end times as well as status
    :type processing_info: str
    :param thumbnail: Cloudfront URL of the asset thumbnail
    :type thumbnail: str
    :param title: Title of the asset
    :type title: str
    :param width: Width of the asset in pixels
    :type width: int
    """

    creation_date: str = None
    duration: float = 0.0
    feed_id: str = None
    fps: float = 0.0
    height: int = 0
    asset_id: str = None
    media_url: str = None
    mime_type: str = None
    processing_info: dict = None
    thumbnail: str = None
    title: str = None
    width: int = 0


class AssetItem:
    @classmethod
    def read(cls, asset_id: str):
        """
        Retrieve general details about a specific asset.

        :param asset_id: ID of the asset
        :type asset_id: str
        :return: Information about the asset
        :rtype: AssetItemModel
        """
        url = f"metadata/{asset_id}"
        response = Client.get(url)

        if response is not None:
            asset = AssetItemModel(
                creation_date=response["creation_date"],
                duration=response["duration"],
                feed_id=response["feed_id"],
                fps=response["fps"],
                height=response["height"],
                asset_id=response["id"],
                media_url=response["media_url"],
                mime_type=response["mime_type"],
                processing_info=response["processing_info"],
                thumbnail=response["thumbnail"],
                title=response["title"],
                width=response["width"],
            )

            return asset
        else:
            return response
