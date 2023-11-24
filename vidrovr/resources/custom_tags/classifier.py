from vidrovr.core import Client

from pydantic import BaseModel

class ClassifierModel(BaseModel):
    """
    Model of a classifier.

    :param id: ID of the classifier
    :type id: str
    :param name: Name of the classifer
    :type name: str
    :param training_state: Current state of training for the classifier
    :type training_state: str
    :param is_active: Indicates if the classifier is active or not
    :type is_active: bool
    """
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
        :rtype: list[ClassifierModel] or ClassifierModel
        """
        if classifier_id is None:
            url = f'customdata/classifiers/?project_uid={project_id}'
        else:
            url = f'customdata/classifiers/{classifier_id}?project_uid={project_id}'

        response = Client.get(url)

        if response is not None:
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
        else:
            return response
    
    @classmethod
    def create(cls, project_id: str):
        """
        Create and train classifiers for the project. The model will be trained across 
        all custom tags with is_active set to true at time of request. This will fail 
        if there are not enough labeled custom tags in a project.

        :param project_id: ID of the project containing the classifier
        :type project_id: str
        :return: Data object representing the new classifer
        :rtype: ClassifierModel
        """
        url     = f'customdata/classifiers'
        payload = {
            'data': {
                'project_uid': project_id
            }
        }
        response = Client.post(url, payload)

        if response is not None:
            classifier = ClassifierModel(
                id=response['id']
            )

            return classifier
        else:
            return response 