import os
class Kryogenesis(object):
    # API_HASH = '4b7731b0a6d8e15bef82863887feb293'
    # APP_ID = 6372795
    # TOKEN = '1834680052:AAF0esEckEAujn87y4U3ezCSyIS-x9Dik7E'
    # YOUTUBE_KEY = "TIMXRCTC0RSPYKAEVRTNITVERLER"
    YOUTUBE_KEY = os.environ.get("YOUGENIS_KEY")
    TOKEN = os.environ.get("TOKEN")
    APP_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")
class Hypotherm(Kryogenesis):
    LOGGER = True