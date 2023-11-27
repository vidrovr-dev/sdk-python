Custom Tags
===========

Creating, deleting and reading tag data
---------------------------------------

To create a new t inag a project, delete a tag from a project or retrieve a 
list of tags for a given project or the details of a specific tag, you can use 
the vidrovr.resources.CustomTag object along with the CustomTagModel data object:

.. autopydantic_model:: vidrovr.resources.custom_tags.CustomTagModel

.. autofunction:: vidrovr.resources.custom_tags.CustomTag.create

.. autofunction:: vidrovr.resources.custom_tags.CustomTag.delete

.. autofunction:: vidrovr.resources.custom_tags.CustomTag.read

Creating, reading and updating tag examples
----------------------------------------------

To create a new tag example in a project, update the example or retrieve a 
list of tag examples in the project, you can use the vidrovr.resources.CustomTagExample 
along with the CustomTagExampleModel data object:

.. autopydantic_model:: vidrovr.resources.custom_tags.CustomTagExampleModel

.. autofunction:: vidrovr.resources.custom_tags.CustomTagExample.read

.. autofunction:: vidrovr.resources.custom_tags.CustomTagExample.update