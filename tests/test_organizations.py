from base_test import BaseTest

from vidrovr.resources.organizations import *


class TestOrganizations(BaseTest):
    def test_org_read(self):
        result = Organization.read(self.org_id)

        assert (
            result is not None
        ), "A valid OrganizationData object should have been returned."

    def test_org_update(self):
        result = Organization.update(self.org_id, self.org_name)

        assert result is not None, "A valid response object should have been returned."

    def test_org_user_read(self):
        result = OrganizationUser.read(self.org_id)

        assert (
            result is not None
        ), "A list of org user ID values should have been returned."

    def test_org_user_update(self):
        data = OrganizationNewUserData(
            email="me@nowhere.com", role_id="", project_ids=self.project_id
        )
        result = OrganizationUser.update(self.org_id, data)

        assert result is not None, "A valid response object should have been returned."
