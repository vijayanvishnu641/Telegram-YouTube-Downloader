import asyncio

users ={}
user_time = {}
DOWNLOAD_LOCATION = "./Downloads"
ytregex = r"^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$"
loop = asyncio.get_event_loop()