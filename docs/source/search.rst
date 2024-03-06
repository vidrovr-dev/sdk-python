Search
======

Creating, deleting, reading and updating search data
----------------------------------------------------

To create a new search in a project, delete a search from a project or retrieve a 
list of saved searches for a given project, you can use the vidrovr.resources.search.Search 
object along with the SavedSearch data object:

.. autopydantic_model:: src.vidrovr.resources.search.SavedSearch

.. autofunction:: src.vidrovr.resources.search.Search.create

.. autofunction:: src.vidrovr.resources.search.Search.delete

.. autofunction:: src.vidrovr.resources.search.Search.read

.. autofunction:: src.vidrovr.resources.search.Search.update

Additional data models
----------------------

These are additional data models used in building a SavedSearch object:

.. autopydantic_model:: src.vidrovr.resources.search.SearchFeedItems

.. autopydantic_model:: src.vidrovr.resources.search.SearchFacet

.. autopydantic_model:: src.vidrovr.resources.search.SearchQuery

.. autopydantic_model:: src.vidrovr.resources.search.SearchData