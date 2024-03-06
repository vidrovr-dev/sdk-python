Organizations
=============

Creating, deleting, reading and updating organization data
----------------------------------------------------------

To retrieve a list of user IDs for an organization or to create a new user
in an organization, you can use the objects in vidrovr.resources.organization.

Organization
------------

.. autopydantic_model:: src.vidrovr.resources.organizations.OrganizationModel

.. autofunction:: src.vidrovr.resources.organizations.Organization.read

.. autofunction:: src.vidrovr.resources.organizations.Organization.update

Organization Users
------------------

.. autopydantic_model:: src.vidrovr.resources.organizations.OrganizationUserModel

.. autofunction:: src.vidrovr.resources.organizations.OrganizationUser.read

.. autofunction:: src.vidrovr.resources.organizations.OrganizationUser.update