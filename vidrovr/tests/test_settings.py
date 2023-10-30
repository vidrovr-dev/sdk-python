from base_test import BaseTest

from vidrovr.resources.settings import *

class TestSettings(BaseTest):
    def test_settings_read(self):
        result = Language.read(self.project_id)

        assert result is not None, "A valid LanguageData object should have been returned."

    def test_settings_update(self):
        data = LanguageData(
            output='de'
        )
        result = Language.update(self.project_id, data)

        assert result is not None, "A valid response object should have been returned."