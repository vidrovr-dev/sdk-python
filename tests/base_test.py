import pytest


class BaseTest:
    def setup_class(cls):
        # initialize shared resources
        cls.asset_id = ""
        cls.project_id = ""
        cls.person_id = ""
        cls.person_name = ""
        cls.person_example_id = ""
        cls.new_label = ""
        cls.classifier_id = ""
        cls.custom_tag_name = ""
        cls.custom_tag_id = ""
        cls.custom_tag_example_id = ""
        cls.custom_tag_label = ""
        cls.feed_id = ""
        cls.feed_status = True  # or False
        cls.feed_schedule_id = ""
        cls.transcript_id = ""
        cls.face_id = ""
        cls.appearance_id = ""
        cls.obj_detection_id = ""
        cls.named_entity_id = ""
        cls.iab_tag_id = ""
        cls.generic_tag_id = ""
        cls.org_id = ""
        cls.org_name = ""
        cls.user_id = ""
        cls.project_name = ""

    def teardown_class(cls):
        # release shared resources
        pass
