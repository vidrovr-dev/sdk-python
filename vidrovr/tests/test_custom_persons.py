from base_test import BaseTest

from vidrovr.resources.custom_persons import *

class TestCustomPersons(BaseTest):
    def test_person_create(self):
        person = Person.create(
            project_id=self.project_id,
            name=self.person_name
        )

        assert person is not None, "Valid Person object should have been returned from create."
        assert person.id is not None, "An ID value should have been returned when creating a new Person."

    def test_person_delete(self):
        person = Person.delete(
            person_id=self.person_id,
            project_id=self.project_id
        )

        assert person is not None, "A valid response object should have been returned from delete."

    def test_person_read(self):
        person = Person.read(
            project_id=self.project_id
        )

        assert person is not None, "A list of Person objects should be returned from read on a project."

    def test_person_details_read(self):
        person_details = Person.read(
            project_id=self.project_id,
            person_id=self.person_id
        )

        assert person_details is not None, "A valid Person object should be returned from read using a person ID."
        assert person_details.id is not None, "An ID value should have been returned when requesting details for a specific person."

    def test_person_example_read(self):
        person_example = PersonExample.read(
            project_id=self.project_id,
            person_id=self.person_id
        )

        assert person_example is not None, "A list of person examples should have been returned."

    def test_person_example_details_read(self):
        person_example_details = PersonExample.read(
            project_id=self.project_id,
            person_id=self.person_id,
            example_id=self.example_id
        )

        assert person_example_details is not None, "A valie PersonExapmle object should be returned from read when using an example ID."
        assert person_example_details.id is not None, "An ID value should have been returned when requesting details for a specific example."

    def test_person_example_update(self):
        person_example = PersonExample.update(
            person_id=self.person_id,
            example_id=self.example_id,
            project_id=self.project_id,
            new_label=self.new_label
        )
        
        assert person_example is not None, "A valid response should have been returned when updating an example."