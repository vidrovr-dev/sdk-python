# Usage

## Work in Progress

:warning: This SDK is currently in progress and still evolving. :warning:

## Installation

To use Vidrovr, first install it using pip:

```
   (.venv) $ pip install vidrovr
```

Before you are able to use the SDK, you will need to create two environment variables on your system. If you
are a bash shell user, these would go into your .bash_profile file. If you use zsh, they would go into your 
.zprofile.

Open your profile in your text editor of choice.

```
   $ nano .zprofile
```

In your profile, add the following lines. Replace 'your api key' with your actual key. You can generate a key
from your profile section of the Vidrovr platform.

```
   export VIDROVR_API_KEY='your api key'
   export VIDROVR_API_VERSION='v2'
```

Save the file and restart your shell. In this example, the shell is zsh.

```
   $ source .zshrc
```

## Example

Here's a small example for retrieving metadata of an asset in the platform.

```python
   import vidrovr.resources.metadata as metadata

   def main():
     asset_id = 'id_of_asset'
     asset_item = metadata.AssetItem.read(asset_id)

     print(asset_item.title)
     print(asset_item.asset_id)

   if __name__ == "__main__":
      main() 
```