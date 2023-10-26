Usage
=====

.. _installation:

Installation
------------

To use Vidrovr, first install it using pip:

.. code-block:: console

   (.venv) $ pip install vidrovr

Example
-------

Here's a small example for retrieving metadata of an asset in the platform.

.. code-block:: python

   from vidrovr.resources.metadata import FeedItem

   def main():
     asset_id  = 'id_of_asset'
     feed_item = FeedItem.read(asset_id)

     print(feed_item.title)
     print(feed_item.asset_id)

   if __name__ == "__main__":
      main() 