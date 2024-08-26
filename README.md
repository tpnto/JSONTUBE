# JSONTUBE

<div id="header">

**Summer** project dedicated to expanding my knowledge on **JS, HTML and CSS**. The purpose of this program was to automate the process of looking up unlisted/private videos that are sitting in Discord chat logs, making the process of archiving much easier and faster.

</div>
  
<div align="center">
  
![image_demo](https://github.com/user-attachments/assets/1e17ecaf-a095-49fb-961a-c8ad74889e2e)

</div>

# How It Works
All you need to do is set-up the API key into the program and then run **host.py**, everything should be hosted locally. Once you select a JSON file, the program will automatically start collecting each YouTube URL and check if they are unlisted/private. As soon as that's done, it will redirect you to a page that has all of the collected url's. The JSON file will be completely removed and the only thing left will be the HTML page containing all the videos found.

# Features
Good thing about JSON's is that they store metadata for a video that's completely lost, with this data I was able to include things such as:
+ Video Description
+ Channel URL
+ Video ID
+ Archive.org URL

The additional Archive.org link will redirect you to: 
```https://web.archive.org/web/2oe_/http://wayback-fakeurl.archive.org/yt/<videoID>```
Which is where the video should be hosted, if not, it's not on archive.org, I suggest using [TheTechRobo's YouTube video finder](https://github.com/TheTechRobo/youtubevideofinder/) if you really want to check if a video has been archived or not.

If you would like to see a video's metadata, just click where the title and status is at.

# Requirements
This program depends on two things for it to work:
+ [YouTube API](https://console.cloud.google.com/marketplace/product/google/youtube.googleapis.com)
+ [Discord Chatlog in JSON format](https://github.com/Tyrrrz/DiscordChatExporter)

If for some reason you are having trouble outputting the collected videos, try making a new folder under the name of "uploads".
##
Don't mind the Spanish, I will update that soon. Maybe.

