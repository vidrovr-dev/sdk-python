import json

from vidrovr.core import Client

from pydantic import BaseModel

class FeedScheduleModel(BaseModel):
    """
    Model of feed schedule

    :param id: ID of the schedule
    :type id: str
    :param day_of_week: The day of the week that the feed polls
    :type day_of_week: str
    :param start_time: Start time for polling
    :type start_time: str
    :param end_time: End time for polling
    :type end_time: str
    """
    id: str = None
    day_of_week: str = None
    start_time: str = None
    end_time: str = None

class FeedSchedule:

    @classmethod
    def read(cls, project_id: str, feed_id: str, feed_schedule_id: str=None):
        """
        Returns data for all schedules in a given project or details on specific schedule.

        :param project_id: ID of the project containing the scheudles
        :type project_id: str
        :param feed_id: ID of the feed
        :type feed_id: str
        :param feed_schedule_id: ID of the schedule or None
        :type feed_schedule_id: str
        :return: List of all schedules or a single schedule
        :rtype: list[FeedScheduleData] or FeedScheduleData
        """
        if feed_schedule_id is None:
            url = f'feeds/{feed_id}/schedules/?project_uid={project_id}'
        else:
            url = f'feeds/{feed_id}/schedules/{feed_schedule_id}/?project_uid={project_id}'

        response = Client.get(url)

        if response is not None:
            feed_schedule = FeedScheduleModel(
                id=response['id'],
                day_of_week=response['creation_date'],
                start_time=response['is_active'],
                end_time=response['name']
            )

            return feed_schedule
        else:
            return response
    
    @classmethod
    def create(cls, feed_id: str, project_id: str, data: FeedScheduleModel):
        """
        Create a schedule for a feed. For HLS Feeds, a specified schedule is needed. 
        You can provide as many as you need. If you'd like to poll the feed always, 
        you'd need to create 7 schedules, one for each day, with start and end times 
        to cover the whole day.

        :param feed_id: ID of the feed for the schedule
        :type feed_id: str
        :param project_id: ID of the project containing the feed
        :type project_id: str
        :param data: Object containing the schedule data
        :type: FeedScheduleData
        :return: JSON string containing the HTTP response
        :rtype: str
        """
        url     = f'feeds/{feed_id}/schedules'
        payload = {
            'data': {
                'start_time': data.start_time,
                'end_time': data.end_time,
                'day_of_week': data.day_of_week,
                'project_uid': project_id
            }
        }
        response = Client.post(url, data=payload)

        return response
