from base_test import BaseTest

from vidrovr.resources.projects import *


class TestProjects(BaseTest):
    def test_project_create(self):
        result = Project.create(self.user_id, self.project_name)

        assert result is not None, "A valid response should have been returned."
        assert result.id is not None, "An ID value should have been returned."

    def test_project_delete(self):
        result = Project.delete(self.project_id)

        assert result is not None, "A valid response object should have been returned."

    def test_project_read(self):
        result = Project.read()

        assert result is not None, "A list of Projects should have been returned."

    def test_projec_detail_read(self):
        result = Project.read(self.project_id)

        assert result is not None, "A ProjectData object should have been returned."
        assert result.id is not None, "An ID value should have been returned."

    def test_project_update(self):
        result = Project.update(self.project_id, self.project_name)

        assert result is not None, "A valid response object should have been returned."
