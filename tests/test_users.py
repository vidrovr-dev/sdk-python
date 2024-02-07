from base_test import BaseTest

from vidrovr.resources.users import *


class TestUsers(BaseTest):
    def test_user_delete(self):
        result = User.delete(self.user_id)

        assert result is not None, "A valid response object should have been returned."

    def test_user_read(self):
        result = User.read(self.user_id)

        assert result is not None, "A valid UserData object should have been returned."
        assert result.id is not None, "An ID value should have been returned."

    def test_user_update(self):
        data = UserData(email="me@nowhere.com")
        result = User.update(self.user_id, data)

        assert result is not None, "A valid response object should have been returned."

    def test_token_create(self):
        result = Token.create(self.user_id)

        assert result is not None, "A valid TokenData object should have been returned."
        assert (
            result.id is not None
        ), "An ID value for the token should have been returned."

    def test_token_read(self):
        result = Token.read(self.user_id)

        assert (
            result is not None
        ), "A list of valid TokenData objects should have been returned."

    def test_roles_read(self):
        result = Roles.read()

        assert result is not None, "A valid response object should have been returned."
