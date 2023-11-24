from vidrovr.core import Client

from pydantic import BaseModel

class CustomTagModel(BaseModel):
    """
    Model of a custom tag.

    :param id: ID of the custom tag
    :type id: str
    :param name: Name of the custom tag
    :type name: str
    :param type: Type of tag
    :type type: str
    :param is_active: Indicates if the custom tag is active or not
    :type is_active: bool
    :param creation_date: Date the custom tag was created
    :type creation_date: str
    :param num_examples: Number of examples for the custom tag
    :type num_examples: int
    :param num_reviewed: Number of reviewd examples for the custom tag
    :type num_reviewed: int
    :param num_unreviewed: Number of unreviewed examples for the custom tag
    :type num_unreviewed: int
    """
    id: str | None
    name: str | None
    type: str | None
    is_active: bool | False
    creation_date: str | None
    num_examples: int | 0
    num_reviewed: int | 0
    num_unreviewed: int | 0

class CustomTag:

    @classmethod
    def read(cls, project_id: str, tag_id: str=None):
        """
        Returns an array with the Custom Tags associated to the project uid or 
        the details of a tag from a specific ID. 

        :param project_id: ID of the project
        :type project_id: str
        :param tag_id: ID of the custom tag or None
        :type tag_id: str
        :return: Array of custom tags in the project or the details of a specific tag
        :rtype: list[CustomTagModel] or CustomTagModel
        """
        if tag_id is None:
            url = f'customdata/tags/?project_uid={project_id}'
        else:
            url = f'customdata/tags/{tag_id}?project_uid={project_id}'

        response = Client.get(url)

        if response is not None:
            if isinstance(response, dict):
                custom_tag = CustomTagModel(
                    id=response['id'],
                    name=response['name'],
                    is_active=response['is_active'],
                    creation_date=response['creation_date'],
                    num_examples=response['num_examples'],
                    num_reviewed=response['num_reviewed'],
                    num_unreviewed=response['num_unreviewed']
                )
            elif isinstance(response, list): 
                custom_tag = [CustomTagModel(**item) for item in response]

            return custom_tag
        else:
            return response
    
    @classmethod
    def delete(cls, tag_id: str, project_id: str):
        """
        Deletes a custom tag in a specific project.

        :param tag_id: ID of the tag to delete
        :type tag_id: str
        :param project_id: ID of the project containing the tag to delete
        :type project_id: str
        :return: Data object containing the ID of the deleted custom tag
        :rtype: CustomTagModel
        """
        url      = f'customdata/tags/{tag_id}?project_uid={project_id}'
        response = Client.delete(url)

        if response is not None:
            tag = CustomTagModel(
                id=response['id'],
                type=response['type']
            )

            return tag
        else:
            return response
    
    @classmethod
    def create(cls, project_id: str, tag_name: str):
        """
        Create a new custom tag in a project.

        :param project_id: ID of the project containing the new tag
        :type project_id: str
        :param tag_name: Name of the tag
        :type tag_name: str
        :return: Data object containing the id and name of the new custom tag
        :rtype: CustomTagModel
        """
        url     = 'customdata/tags'
        payload = {
            'data': {
                'name': tag_name,
                'project_uid': project_id
            }
        }
        response = Client.post(url, payload)

        if response is not None:
            tag = CustomTagModel(
                id=response['id'],
                name=response['name']
            )

            return tag
        else:
            return response