from ...core import Client

from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class PersonExampleData:
    id: str
    href: str
    source: str
    status: str

class PersonExample(BaseModel):

    @classmethod
    def read(cls, project_id: str, person_id: str, example_id: str=None):
        """
        Returns either a single person or an array of person examples identifiers, 
        paginated, and filtered by status, which can be one of three values: accepted, 
        rejected or candidate. The first value of page is always 0.

        :param project_id: ID of the project containing the person examples
        :type project_id: str
        :param person_id: ID of the person in the project
        :type person_id: str
        :param example_id: ID of the specific example to pull details. Defaults to None to return the array of all examples.
        :type example_id: str
        :return: A single person or an array of person examples
        :rtype: PersonExampleData
        """
        if example_id is None:
            url = f'customdata/persons/{person_id}/examples?project_uid{project_id}=&status=&page_size=&page='
        else:
            url = f'customdata/persons/{person_id}/examples/{example_id}?project_uid={project_id}'

        response = Client.get(url)

        if isinstance(response, dict):
            person = PersonExampleData(
                id=response['id'],
                href=response['href'],
                source=response['source'],
                status=response['status']
            )
        elif isinstance(response, list): 
            person = [PersonExampleData(**item) for item in response]

        return person
    
    @classmethod
    def update(cls, person_id: str, example_id: str, project_id: str, new_label: str):
        """
        Updates the status of the Person Example, for instance from candidate to accepted or rejected

        :param person_id: ID of the person to update
        :type person_id: str
        :param example_id: ID of the example containing the person
        :type example_id: str
        :param project_id: ID of the project containing the person example
        :type project_id: str
        :param new_label: Label for the status (candidate, accepted, rejected)
        :type new_label: str
        :return: JSON string of containing the HTTP response
        :rtype: str
        """
        url     = f'customdata/persons/{person_id}/examples/{example_id}?project_uid={project_id}'
        payload = {
            'data': {
                'status': new_label,
                'project_uid': project_id
            }
        }
        response = Client.patch(url, payload)
        
        return response
    
    @classmethod
    def create(cls):
        return NotImplementedError