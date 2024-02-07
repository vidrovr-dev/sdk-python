from base_test import BaseTest

from vidrovr.resources.feeds import *

class TestFeeds(BaseTest):
    def test_feed_create(self):
        data = FeedItem(
            feed_type='',
            name='',
            media_type='',
            hls_link='',
            project_uids=''
        )
        feed = Feed.create(data)

        assert feed is not None, "A valid response should have been returned from feed create."

    def test_feed_delete(self):
        feed = Feed.delete(self.feed_id, self.project_id)

        assert feed is not None, "A valid response should have been returned from feed delete."

    def test_feed_read(self):
        feed = Feed.read(self.project_id)

        assert feed is not None, "A feed or a list of feeds should have been returned from feed read."

    def test_feed_update(self):
        feed = Feed.update(self.feed_id, self.project_id, self.feed_status)

        assert feed is not None, "A valid response should have been returned from feed update."

    def test_feed_detail_read(self):
        feed = FeedDetail.read(self.feed_id, self.project_id)

        assert feed is not None, "A valid feed object should have been returned from detail read."
        assert feed.id is not None, "An ID value should have been returned from detail read."

    def test_feed_schedule_create(self):
        data = FeedScheduleData(
            id=self.feed_id,
            day_of_week='',
            start_time='',
            end_time=''
        )
        feed_schedule = FeedSchedule.create(self.feed_id, self.project_id, data)

        assert feed_schedule is not None, "A valid response should have been returned from feed schedule create."

    def test_feed_schedule_read(self):
        feed_schedule = FeedSchedule.read(self.project_id, self.feed_id)

        assert feed_schedule is not None, "A list of FeedSchedule objects should have been returned from read."

    def test_feed_schedule_detail_read(self):
        feed_schedule = FeedSchedule.read(self.project_id, self.feed_id, self.feed_schedule_id)

        assert feed_schedule is not None, "A feed schedule should have been returned from detail read."
        assert feed_schedule.id is not None, "An ID value should have been returned from detail read."