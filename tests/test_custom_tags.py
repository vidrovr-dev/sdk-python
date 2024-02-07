from base_test import BaseTest

from vidrovr.resources.custom_tags import *

class TestCustomTags(BaseTest):
    def test_classifier_create(self):
        classifier = Classifier.create(self.project_id)
        
        assert classifier is not None, "A valid response should have been returned from classifier create."

    def test_classifier_read(self):
        classifier = Classifier.read(self.project_id)

        assert classifier is not None, "A list of classifiers for the project should have been returned."

    def test_classifier_detail_read(self):
        classifier = Classifier.read(self.project_id, self.classifier_id)

        assert classifier is not None, "A valid Classifier should have been returned from the read."
        assert classifier.id is not None, "An ID value should have been returned from a detail read."

    def test_tag_create(self):
        custom_tag = CustomTag.create(self.project_id, self.custom_tag_name)

        assert custom_tag is not None, "A valid response should have been returned from custom tag create."

    def test_tag_delete(self):
        custom_tag = CustomTag.delete(self.custom_tag_id, self.project_id)

        assert custom_tag is not None, "A valid response should have been returned from custom tag delete."

    def test_tag_read(self):
        custom_tag = CustomTag.read(self.project_id)

        assert custom_tag is not None, "A list of custom tag objects should have been returned."

    def test_tag_detail_read(self):
        custom_tag = CustomTag.read(self.project_id, self.custom_tag_id)

        assert custom_tag is not None, "A valid CustomTag should have been returned from the read."
        assert custom_tag.id is not None, "An ID value should have been returned from a detail read."

    def test_tag_example_read(self):
        tag_example = CustomTagExample.read(self.project_id)

        assert tag_example is not None, "A list of custom tag example object should have been returned."

    def test_tag_example_detail_read(self):
        tag_example = CustomTagExample.read(
            self.project_id, 
            self.custom_tag_id, 
            self.custom_tag_example_id
        )

        assert tag_example is not None, "A valid CustomTagExample should have been returned from the read."
        assert tag_example.id is not None, "An ID value should have been returned from a detail read."

    def test_tag_example_update(self):
        tag_example = CustomTagExample.update(
            self.custom_tag_id, 
            self.custom_tag_example_id, 
            self.project_id, 
            self.custom_tag_label
        )

        assert tag_example is not None, "A valid response should have been returned from custom tag example update."