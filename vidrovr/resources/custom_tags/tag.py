from ...core import Client

from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class CustomTagData:
    id: str
    name: str
    is_active: bool
    creation_date: str
    num_examples: int
    num_reviewed: int
    num_unreviewed: int

class CustomTag(BaseModel):

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
        :rtype: list[TagData] or TagData
        """
        if tag_id is None:
            url = f'customdata/tags/?project_uid={project_id}'
        else:
            url = f'customdata/tags/{tag_id}?project_uid={project_id}'

        response = Client.get(url)

        if isinstance(response, dict):
            custom_tag = CustomTagData(
                id=response['id'],
                name=response['name'],
                is_active=response['is_active'],
                creation_date=response['creation_date'],
                num_examples=response['num_examples'],
                num_reviewed=response['num_reviewed'],
                num_unreviewed=response['num_unreviewed']
            )
        elif isinstance(response, list): 
            custom_tag = [CustomTagData(**item) for item in response]

        return custom_tag
    
    @classmethod
    def delete(cls, tag_id: str, project_id: str):
        """
        Deletes a custom tag in a specific project.

        :param tag_id: ID of the tag to delete
        :type tag_id: str
        :param project_id: ID of the project containing the tag to delete
        :type project_id: str
        :return: JSON string of the HTTP response
        :rtype: str
        """
        url      = f'customdata/tags/{tag_id}?project_uid={project_id}'
        response = Client.delete(url)

        return response
    
    @classmethod
    def create(cls, project_id: str, tag_name: str):
        """
        Create a new custom tag in a project.

        :param project_id: ID of the project containing the new tag
        :type project_id: str
        :param tag_name: Name of the tag
        :type tag_name: str
        :return: JSON string of the HTTP response
        :rtype: str
        """
        url     = 'customdata/tags'
        payload = {
            'data': {
                'name': tag_name,
                'project_uid': project_id
            }
        }
        response = Client.post(url, payload)

        return response