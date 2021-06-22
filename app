{
    "name": "YoutubeDownloader",
    "description": "Download any Youtube Audio/Video at full quality",
    "repository": "https://github.com/calitronx/Telegram-YouTube-Downloader.git",
    "logo": "https://telegra.ph/file/3f50d5aefad4cab71e754.jpg",
    "success_url": "https://t.me/tronxli",
    "website": "https://github.com/calitronx/Telegram-YouTube-Downloader.git", 
    "keywords": [
      "Youtube",
      "YoutubeDownloader",
      "YoutubeMusic",
      "Audio",
      "Music",
      "Video",
      "Premium"
    ],  
    "env": {
        "API_ID": {
                "description": "api_id part of your Telegram API Key from my.telegram.org/apps",
                "required": true
        },
        "API_HASH": {
                "description": "api_hash part of your Telegram API Key from my.telegram.org/apps",
                "required": true
        },
        "TOKEN": {
                "description": "Your telegram bot token.Get from Botfather",
                "required": true
        }
        },
        "YOUTUBE_KEY": {
                "description": "Put your Setrix-Kryo-Key from @kryli_bot",
                "required": true
      },
      "buildpacks": [
        {
          "url": "https://github.com/calitronx/heroku-buildpack-ffmpeg.git"
        },
        {
          "url": "heroku/python"
        }
      ]
    }