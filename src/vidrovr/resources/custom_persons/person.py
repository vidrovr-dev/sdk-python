from vidrovr.core import Client

from pydantic import BaseModel


class PersonModel(BaseModel):
    """
    Model of a person.

    :param id: ID of the person
    :type id: str
    :param name: Name of the person
    :type name: str
    :param creation_date: Creation date of the person
    :type creation_date: str
    :param is_active: Indicates if the person is active or not
    :type is_active: bool
    :param num_examples: Number of examples of the person
    :type num_examples: int
    :param num_reviewed: Number of examples of the peson that have been reviewed
    :type num_reviewed: int
    :param num_unreviewed: Number of example of the person that have not been reviewed
    :type num_unreviewed: int
    """

    id: str = None
    name: str = None
    creation_date: str = None
    is_active: bool = False
    num_examples: int = 0
    num_reviewed: int = 0
    num_unreviewed: int = 0


class Person:
    @classmethod
    def read(cls, project_id: str, person_id: str = None):
        """
        Returns an array with the Custom Persons associated to the project uid or
        the details of a person from a specific ID.

        :param project_id: ID of the project
        :type project_id: str
        :param person_id: ID of the person or None
        :type person_id: str
        :return: Array of persons in the project or the details of a specific person
        :rtype: list[PersonModel] or PersonModel
        """
        if person_id is None:
            url = f"customdata/persons/?project_uid={project_id}"
        else:
            url = f"customdata/persons/{person_id}?project_uid={project_id}"

        response = Client.get(url)

        if isinstance(response, dict):
            person = PersonModel(
                id=response["id"],
                name=response["name"],
                creation_date=response["creation_date"],
                is_active=response["is_active"],
                num_examples=response["num_examples"],
                num_reviewed=response["num_reviewed"],
                num_unreviewed=response["num_unreviewed"],
            )
        elif isinstance(response, list):
            person = [PersonModel(**item) for item in response]

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
        url = f"customdata/persons/{person_id}?project_uid={project_id}"
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
        :return: Data object of a person
        :rtype: PersonModel
        """
        url = "customdata/persons/"
        payload = {"data": {"name": name, "project_uid": project_id}}
        response = Client.post(url, payload)

        if response is not None:
            person = PersonModel(id=response["id"], name=response["name"])

            return person
        else:
            return response
