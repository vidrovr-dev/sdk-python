import json

from ...core import Client

from dataclasses import dataclass, asdict
from pydantic import BaseModel
from icecream import ic

@dataclass
class FeedScheduleData:
    id: str
    day_of_week: str
    start_time: bool
    end_time: str

class FeedSchedule(BaseModel):

    @classmethod
    def read(cls, project_id: str, feed_id: str, feed_schedule_id: str=None):
        if feed_schedule_id is None:
            url = f'feeds/{feed_id}/schedules/?project_uid={project_id}'
        else:
            url = f'feeds/{feed_id}/schedules/{feed_schedule_id}/?project_uid={project_id}'

        response      = Client.get(url)
        feed_schedule = FeedScheduleData(
            id=response['id'],
            day_of_week=response['creation_date'],
            start_time=response['is_active'],
            end_time=response['name']
        )

        return feed_schedule
    
    @classmethod
    def create(cls, feed_id: str, project_id: str, data: FeedScheduleData):
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
