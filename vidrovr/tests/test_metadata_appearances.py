from base_test import BaseTest

from vidrovr.resources.metadata.appearances import *

class TestMetadataAppearances(BaseTest):
    def test_custom_tags_appearances_read(self):
        result = CustomTagsAppearances.read(self.asset_id)

        assert result is not None, "A list of custom tag appearances data should have been returned."

    def test_generic_tags_appearances_read(self):
        result = GenericTagsAppearances.read(self.asset_id)

        assert result is not None, "A list of generic tag appearances data should have been returned."

    def test_iab_tags_appearances_read(self):
        result = IABAppearances.read(self.asset_id)

        assert result is not None, "A list of IAB tag appearances data should have been returned."

    def test_named_entities_appearances_read(self):
        result = NamedEntitiesAppearances.read(self.asset_id)

        assert result is not None, "A list of named entities appearances data should have been returned."

    def test_object_appearances_read(self):
        result = ObjectAppearances.read(self.asset_id)

        assert result is not None, "A list of object appearances data should have been returned."

    def test_ocr_appearances_read(self):
        result = OCRAppearances.read(self.asset_id)

        assert result is not None, "A list of OCR appearances data should have been returned."

    def test_person_appearances_read(self):
        result = PersonAppearances.read(self.asset_id)

        assert result is not None, "A list of person appearances data should have been returned."

    def test_transcript_appearances_read(self):
        result = TranscriptAppearances.read(self.asset_id)

        assert result is not None, "A list of transcript appearances data should have been returned."