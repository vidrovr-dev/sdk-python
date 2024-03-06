Usage
=====

.. _installation:

Installation
------------

To use Vidrovr, first install it using pip:

.. code-block:: console

   (.venv) $ pip install vidrovr

Before you are able to use the SDK, you will need to create two environment variables on your system. If you
are a bash shell user, these would go into your .bash_profile file. If you use zsh, they would go into your 
.zprofile.

Open your profile in your text editor of choice.

.. code-block:: console

   $ nano .zprofile

In your profile, add the following lines. Replace 'your api key' with your actual key. You can generate a key
from your profile section of the Vidrovr platform.

.. code-block:: console

   export VIDROVR_API_KEY='your api key'
   export VIDROVR_API_VERSION='v2'

Save the file and restart your shell. In this example, the shell is zsh.

.. code-block:: console

   $ source .zshrc

Example
-------

Here's a small example for retrieving metadata of an asset in the platform.

.. code-block:: python

   from vidrovr.resources.metadata import AssetItem

   def main():
     asset_id  = 'id_of_asset'
     feed_item = FeedItem.read(asset_id)

     print(feed_item.title)
     print(feed_item.asset_id)

   if __name__ == "__main__":
      main() 