from vidrovr.core import Client

from pydantic import BaseModel

class CustomTagExampleModel(BaseModel):
    """
    Model of a custom tag example.

    :param id: ID of the custom tag example
    :type id: str
    :param href: Cloudfront URL of the tag example image
    :type href: str
    :param source: Source of the tag example - search or user_upload
    :type source: str
    :param status: Status of the tag example - accepted, rejected or candidate
    :type status: str
    """
    id: str | None
    href: str | None
    source: str | None
    status: str | None

class CustomTagExample:

    @classmethod
    def read(cls, project_id: str, tag_id: str, example_id: str=None):
        """
        Returns either a single tag example or an array of tag examples identifiers, 
        paginated, and filtered by status, which can be one of three values: accepted, 
        rejected or candidate. The first value of page is always 0.

        :param project_id: ID of the project from which to retrieve tag examples
        :type project_id: str
        :param tag_id: ID of the tag from which to retrieve examples
        :type tag_id: str
        :param example_id: ID of the example to retrieve or None
        :type example_id: str
        :return: An array of tag examples or a single example
        :rtype: list[CustomTagExampleModel] or CustomTagExampleModel
        """
        if example_id is None:
            url = f'customdata/tags/{tag_id}/examples?project_uid={project_id}&status=&page_size=&page='
        else:
            url = f'customdata/tags/{tag_id}/examples/{example_id}?project_uid={project_id}'

        response = Client.get(url)

        if response is not None:
            if isinstance(response, dict):
                custom_tag = CustomTagExampleModel(
                    id=response['id'],
                    href=response['href'],
                    source=response['source'],
                    status=response['status']
                )
            elif isinstance(response, list): 
                custom_tag = [CustomTagExampleModel(**item) for item in response]

            return custom_tag
        else:
            return response
    
    @classmethod
    def update(cls, tag_id: str, example_id: str, project_id: str, new_label: str):
        """
        Updates the status of the Tag Example, for instance from candidate to accepted or rejected

        :param tag_id: ID of the tag containing the example to update
        :type tag_id: str
        :param example_id: ID of the example to update
        :type example_id: str
        :param project_id: ID of the project containing the tag example
        :type project_id: str
        :param new_label: Label for the status (candidate, accepted, rejected)
        :type new_label: str
        :return: Data object containing updated status value
        :rtype: CustomTagExampleModel
        """
        url     = f'customdata/tags/{tag_id}/examples/{example_id}?project_uid={project_id}'
        payload = {
            'data': {
                'status': new_label,
                'project_uid': project_id
            }
        }
        response = Client.patch(url, payload)

        if response is not None:
            tag = CustomTagExampleModel(
                id=response['id'],
                href=response['href'],
                source=response['source'],
                status=response['status']
            )

            return tag
        else:
            return response