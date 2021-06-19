import asyncio

youtube_next_fetch = 0  # time in minute
EDIT_TIME = 5
users ={}
user_time = {}
DOWNLOAD_LOCATION = "./Downloads"
ytregex = r"^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$"
loop = asyncio.get_event_loop()
HMM = "Better not fuck the code son!"
LOADR =  "kalitron"
TKST = "run"