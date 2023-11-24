# Feeds

Feeds define ways that Vidrovr's platform ingests video data from different sources.

## Feed Types

### Manual

`user_upload`: The `user_upload` feed type represents video files uploaded directly by a user to an API endpoint.

### Social Media

Social media feeds scrape video and other media from social media on a set schedule.
They come in two general flavors: 
a _profile_ flavor, 
and a _query_ flavor. 
The most common variant of the _query_ flavor is the _hashtag_.

#### Youtube

We provide one feed type for YouTube: `youtube`. 
It is profile-flavored: 
on youtube, uploader profiles are called "channels", 
and Vidrovr's `youtube` feed type will check a provided channel 
for new content periodically.

#### Instagram (IG)

We provide two IG feed types.
`instagram_profile` is profile-flavored and targets a specific IG user's content.
`instagram_hashtag` is query-flavored and targets content across IG users for a specific hashtag.

#### Twitter

We provide two Twitter feed types.
`twitter_profile` is profile-flavored and targets a specific Twitter user's content.
`twitter_hashtag` is query-flavored and targets content across Twitter users for a specific hashtag.
