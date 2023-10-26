import pytest

class BaseTest:

    def setup_class(cls):
        # initialize shared resources
        cls.project_id  = ''
        cls.person_id   = ''
        cls.person_name = ''
        cls.example_id  = ''
        cls.new_label   = ''

    def teardown_class(cls):
        # release shared resources
        pass