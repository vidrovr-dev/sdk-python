Search
======

Creating, deleting, reading and updating search data
----------------------------------------------------

To create a new search in a project, delete a search from a project or retrieve a 
list of saved searches for a given project, you can use the vidrovr.resources.search.Search 
object along with the SavedSearch data object:

.. autopydantic_model:: vidrovr.resources.search.SavedSearch

.. autofunction:: vidrovr.resources.search.Search.create

.. autofunction:: vidrovr.resources.search.Search.delete

.. autofunction:: vidrovr.resources.search.Search.read

.. autofunction:: vidrovr.resources.search.Search.update

Additional data models
----------------------

These are additional data models used in building a SavedSearch object:

.. autopydantic_model:: vidrovr.resources.search.SearchFeedItems

.. autopydantic_model:: vidrovr.resources.search.SearchFacet

.. autopydantic_model:: vidrovr.resources.search.SearchQuery

.. autopydantic_model:: vidrovr.resources.search.SearchData