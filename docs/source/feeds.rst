Feeds
=====

Creating, deleting and reading feeds
------------------------------------

To create a new feed in a project, delete a feed from a project or retrieve a 
list of feeds for a given project or the details of a specific feed, you can use 
the vidrovr.resources.feeds.Feed object:

.. autofunction:: vidrovr.resources.feeds.Feed.create

.. autofunction:: vidrovr.resources.feeds.Feed.delete

.. autofunction:: vidrovr.resources.feeds.Feed.read

.. autofunction:: vidrovr.resources.feeds.Feed.update

Creating and reading feed schedules
-----------------------------------

To create a new schedule, or retrieve scheudle details, for a feed, you can
use the vidrovr.resources.feeds.FeedSchedule object:

.. autofunction:: vidrovr.resources.feeds.FeedSchedule.read

.. autofunction:: vidrovr.resources.feeds.FeedSchedule.update

Reading feed details
--------------------

To retrieve details for a specific feed in a project, you can use the
vidrovr.resources.feeds.FeedDetails object:

.. autofunction:: vidrovr.resources.feeds.FeedDetails.read