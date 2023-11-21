from vidrovr.core import Client

from pydantic import BaseModel

class ClassifierModel(BaseModel):
    id: str | None
    name: str | None
    training_state: str | None
    is_active: bool | False

class Classifier:

    @classmethod
    def read(cls, project_id: str, classifier_id: str=None):
        """
        Returns an array of classifiers trained for a specific project or details for 
        a single classifier.

        :param project_id: ID of the project containing the classifier
        :type project_id: str
        :param classifier_id: ID of the classifier to retrieve or None
        :type classifier_id: str
        :return: Array of classifiers for the project or the details of a single classifier
        :rtype: list[ClassifierData] or ClassifierData
        """
        if classifier_id is None:
            url = f'customdata/classifiers/?project_uid={project_id}'
        else:
            url = f'customdata/classifiers/{classifier_id}?project_uid={project_id}'

        response = Client.get(url)

        if isinstance(response, dict):
            custom_tag = ClassifierModel(
                id=response['id'],
                name=response['name'],
                training_state=response['training_state'],
                is_active=response['is_active']
            )
        elif isinstance(response, list): 
            custom_tag = [ClassifierModel(**item) for item in response]

        return custom_tag
    
    @classmethod
    def create(cls, project_id: str):
        """
        Create and train classifiers for the project. The model will be trained across 
        all custom tags with is_active set to true at time of request.

        :param project_id: ID of the project containing the classifier
        :type project_id: str
        :return: JSON string containing the HTTP response
        :rtype; str
        """
        url     = f'customdata/classifiers'
        payload = {
            'data': {
                'project_uid': project_id
            }
        }
        response = Client.post(url, payload)

        return response 