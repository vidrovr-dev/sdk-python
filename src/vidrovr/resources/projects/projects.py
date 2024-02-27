from src.vidrovr.core import Client

from pydantic import BaseModel, ValidationError, validator


class ProjectModel(BaseModel):
    """
    Model of a project

    :param id: ID of the project
    :type id: str
    :param name: Name of the project
    :type name: str
    :param user_ids: List of user ID values
    :type user_ids: list[str]
    :param creation_date: Creation date of the project
    :type creation_date: str
    :param type: Type of project
    :type type: str
    """

    id: str = None
    name: str = None
    user_ids: list[str] = None
    creation_date: str = None
    type: str = None

    @validator("user_ids", pre=True)
    def check_user_ids(cls, value):
        if value is None:
            value = "Default"

        return value

    @validator("creation_date", pre=True)
    def check_creation_date(cls, value):
        if value is None:
            value = "None"

        return value

    @validator("type", pre=True)
    def check_type(cls, value):
        if value is None:
            value = "None"

        return value


class Project:
    @classmethod
    def read(cls, project_id: str = None):
        """
        Retrieve a list of projects in the organization or details about a specific project.

        :param project_id: ID of the projec or None
        :type project_id: str
        :return: Array of project information or a single project
        :rtype: list[ProjectData] or ProjectData
        """
        if project_id is None:
            url = f"projects/"
        else:
            url = f"projects/{project_id}"

        response = Client.get(url)

        if response is not None:
            if isinstance(response, dict):
                project = ProjectModel(
                    id=response["id"],
                    name=response["name"],
                    user_ids=response["user_ids"],
                    creation_date=response["creation_date"],
                )
            elif isinstance(response, list):
                project = [ProjectModel(**item) for item in response]

            return project
        else:
            return response

    @classmethod
    def delete(cls, project_id: str):
        """
        Delete a specific project from the organization.

        :param project_id: ID of the project
        :type project_id: str
        :return: A ProjectModel on success
        :rtype: ProjectModel
        """
        url = f"projects/{project_id}"
        response = Client.delete(url)

        if response is not None:
            project = ProjectModel(id=response["id"], type=response["type"])

            return project
        else:
            return response

    @classmethod
    def update(
        cls, project_id: str, name: str, user_id: str = None, operation: str = None
    ):
        """
        Update a project in an organization.

        :param project_id: ID of the project
        :type project_id: str
        :param name: Name of the project
        :type name: str
        :param user_id: ID of user to add or remove from project, optional
        :type user_id: str
        :param operation: Add or remove user from project, optional but required if using user_id
        :type operation: str
        :return: A ProjectModel on success
        :rtype: ProjectModel
        """
        url = f"projects/{project_id}"
        payload = {"data": {"name": name}}

        # check for optional items
        if user_id is not None:
            if "user_ids" not in payload["data"]:
                payload["data"]["user_ids"] = user_id

        if operation is not None:
            if "operation" not in payload["data"]:
                payload["data"]["operation"] = operation

        response = Client.patch(url, payload)

        if response is not None:
            project = ProjectModel(
                id=response["id"],
                name=response["name"],
                user_ids=response["user_ids"],
                creation_date=response["creation_date"],
            )

            return project
        else:
            return response

    @classmethod
    def create(cls, data: ProjectModel):
        """
        Create a new project in the organization.

        :param user_id: ID of the user associated with the project
        :type user_id: str
        :param name: Name of the project
        :type name: str
        :return: A ProjectModel on success
        :rtype: ProjectModel
        """
        url = f"projects/"
        payload = {"data": {"name": data.name, "user_ids": [data.user_ids]}}
        response = Client.post(url, data=payload)

        if response is not None:
            project = ProjectModel(
                id=response["id"],
                name=response["name"],
                creation_date=response["creation_date"],
                user_ids=response["user_ids"],
            )

            return project
        else:
            return response
