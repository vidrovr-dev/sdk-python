from ...core import Client

from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class PersonData:
    id: str
    name: str
    creation_date: str
    is_active: bool
    num_examples: int
    num_reviewed: int
    num_unreviewed: int

class Person(BaseModel):

    @classmethod
    def read(cls, project_id: str, person_id: str=None):
        """
        Returns an array with the Custom Persons associated to the project uid or 
        the details of a person from a specific ID.

        :param project_id: ID of the project
        :type project_id: str
        :param person_id: ID of the person or None
        :type person_id: str
        :return: Array of persons in the project or the details of a specific person
        :rtype: list[PersonData] or PersonData
        """
        if person_id is None:
            url = f'customdata/persons/?project_uid={project_id}'
        else:
            url = f'customdata/persons/{person_id}?project_uid={project_id}'

        response = Client.get(url)

        if isinstance(response, dict):
            person = PersonData(
                id=response['id'],
                name=response['name'],
                creation_date=response['creation_date'],
                is_active=response['is_active'],
                num_examples=response['num_examples'],
                num_reviewed=response['num_reviewed'],
                num_unreviewed=response['num_unreviewed']
            )
        elif isinstance(response, list): 
            person = [PersonData(**item) for item in response]

        return person

    @classmethod
    def delete(cls, person_id: str, project_id: str):
        """
        Deletes a Person from the VIdrovr system.

        :param person_id: ID of the person to be deleted
        :type person_id: str
        :param project_id: ID of the project that contains the person to be deleted
        :type project_id: str
        :return: JSON string of the HTTP response
        :rtype: str
        """
        url      = f'customdata/persons/{person_id}?project_uid={project_id}'
        response = Client.delete(url)

        return response
        
    @classmethod
    def create(cls, project_id: str, name: str):
        """
        Creates a new person for the given project.

        :param project_id: ID of the project to contain the new person
        :type project_id: str
        :param name: Name of the person to be created
        :type name: str
        :return: JSON string of the HTTP response containing the ID of the new person
        :rtype: str
        """
        url     = 'customdata/persons/'
        payload = {
            'data': {
                'name': name,
                'project_uid': project_id
            }
        }
        response = Client.post(url, payload)

        return response
