Custom Persons
==============

Creating, deleting and reading person data
------------------------------------------

To create a new person in a project, delete a person from a project or retrieve a 
list of persons for a given project or the details of a specific person, you can use 
the vidrovr.resources.Person object along with the PersonModel data object:

.. autopydantic_model:: src.vidrovr.resources.custom_persons.PersonModel

.. autofunction:: src.vidrovr.resources.custom_persons.Person.create

.. autofunction:: src.vidrovr.resources.custom_persons.Person.delete

.. autofunction:: src.vidrovr.resources.custom_persons.Person.read

Creating, reading and updating person examples
----------------------------------------------

To create a new person example in a project, update the example or retrieve a 
list of person examples in the project, you can use the vidrovr.resources.PersonExample 
along with the PersonExampleModel object:

.. autopydantic_model:: src.vidrovr.resources.custom_persons.PersonExampleModel

.. autofunction:: src.vidrovr.resources.custom_persons.PersonExample.create

.. autofunction:: src.vidrovr.resources.custom_persons.PersonExample.read

.. autofunction:: src.vidrovr.resources.custom_persons.PersonExample.update

.. autofunction:: src.vidrovr.resources.custom_persons.PersonExample.search