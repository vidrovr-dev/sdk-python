from base_test import BaseTest

from vidrovr.resources.custom_persons import Person, PersonData, PersonExample, PersonExampleData

class TestCustomPersons(BaseTest):
    def test_person_create(self):
        person = Person.create(
            project_id=self.project_id,
            name=self.person_name
        )

        pass

    def test_person_delete(self):
        person = Person.delete(
            person_id=self.person_id,
            project_id=self.project_id
        )

        pass

    def test_person_read(self):
        person = Person.read(
            project_id=self.project_id
        )

        assert person

    def test_person_details_read(self):
        person_details = Person.read(
            project_id=self.project_id,
            person_id=self.person_id
        )

        pass

    def test_person_example_read(self):
        person_example = PersonExample.read(
            project_id=self.project_id,
            person_id=self.person_id
        )

        pass

    def test_person_example_details_read(self):
        person_example_details = PersonExample.read(
            project_id=self.project_id,
            person_id=self.person_id,
            example_id=self.example_id
        )

        pass

    def test_person_example_update(self):
        person_example = PersonExample.update(
            person_id=self.person_id,
            example_id=self.example_id,
            project_id=self.project_id,
            new_label=self.new_label
        )
        
        pass