from base_test import BaseTest

from vidrovr.resources.metadata import *

class TestMetadata(BaseTest):
    def test_custom_tags_read(self):
        result = CustomTag.read(self.asset_id)

        assert result is not None, "A list of CustomTagData objects should have been returned."

    def test_custom_tags_detail_read(self):
        result = CustomTag.read(self.asset_id, self.custom_tag_id)

        assert result is not None, "A valid CustomTagData object should have been returned."
        assert result.id is not None, "An ID value should have been returned."

    def test_feed_item_read(self):
        result = FeedItem.read(self.asset_id)

        assert result is not None, "A valid FeedItem object should have been returned."
        assert result.id is not None, "An ID value should have been returned."

    def test_generic_tags_read(self):
        result = GenericTag.read(self.asset_id)

        assert result is not None, "A list of GenericTagData objects should have been returned."

    def test_generic_tags_detail_read(self):
        result = GenericTag.read(self.asset_id, self.generic_tag_id)

        assert result is not None, "A valid GenericTagData object should have been returned."
        assert result.id is not None, "An ID value should have been returned."

    def test_iab_tags_read(self):
        result = IABTag.read(self.asset_id)

        assert result is not None, "A list of IABTagData objects should have been returned,"

    def test_iab_tags_detail_read(self):
        result = IABTag.read(self.asset_id, self.iab_tag_id)

        assert result is not None, "A valid IABTagData object should have been returned."
        assert result.id is not None, "An ID value should have been returned."

    def test_keyphrases_read(self):
        result = Keyphrase.read(self.asset_id)

        assert result is not None, "A list of KeyphraseData objects should have been returned."

    def test_named_entities_read(self):
        result = NamedEntities.read(self.asset_id)

        assert result is not None, "A list of NamedEntityData objects should have been returned."

    def test_named_entities_detail_read(self):
        result = NamedEntities.read(self.asset_id, self.named_entity_id)

        assert result is not None, "A valid NamedEntityObject should have been returned."
        assert result.id is not None, "An ID value should have been returned."

    def test_object_read(self):
        result = Object.read(self.asset_id)

        assert result is not None, "A list of ObjectData objects should have been returned."

    def test_object_detail_read(self):
        result = Object.read(self.asset_id, self.obj_detection_id)

        assert result is not None, "A valid ObjectData object should have been returned."
        assert result.id is not None, "An ID value should have been returned."

    def test_ocr_read(self):
        result = OCR.read(self.asset_id)

        assert result is not None, "A list of OCRData objects should have been returned."

    def test_ocr_detail_read(self):
        result = OCR.read(self.asset_id, self.appearance_id)

        assert result is not None, "A valid OCRData object should have been returned."
        assert result.id is not None, "An ID value should have been returned."

    def test_person_read(self):
        result = Person.read(self.asset_id)

        assert result is not None, "A list of PersonData objects should have been returned."

    def test_person_detail_read(self):
        result = Person.read(self.asset_id, self.face_id)

        assert result is not None, "A valid PersonData object should have been returned."
        assert result.id is not None, "An ID value should have been returned."

    def test_transcript_read(self):
        result = Transcript.read(self.asset_id, self.transcript_id)

        assert result is not None, "A valid TranscriptData object should have been returned."