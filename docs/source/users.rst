Users
=====

Creating, deleting, reading and updating user data
--------------------------------------------------

To interact with user information, you can use the vidrovr.resources.users.User 
along with the UserModel data object.

.. autopydantic_model:: vidrovr.resources.users.UserModel

.. autofunction:: vidrovr.resources.users.User.delete

.. autofunction:: vidrovr.resources.users.User.read

.. autofunction:: vidrovr.resources.users.User.update

Creating and reading user token data
------------------------------------

To create or retrieve data about user tokens, you can use the vidrovr.resources.users.Token 
along with the TokenModel data object.

.. autopydantic_model:: vidrovr.resources.users.TokenModel

.. autofunction:: vidrovr.resources.users.Token.create

.. autofunction:: vidrovr.resources.users.Token.read

Reading user role data
----------------------

To retrieve information about available user roles, you can use the vidrovr.resources.users.Roles 
along with the RolesModel data object.

.. autopydantic_model:: vidrovr.resources.users.RolesModel

.. autofunction:: vidrovr.resources.users.Roles.read