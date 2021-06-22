import os
class Kryogenesis(object):
    YOUTUBE_KEY = os.environ.get("YOUTUBE_KEY")
    TOKEN = os.environ.get("TOKEN")
    APP_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")
class Hypotherm(Kryogenesis):
    LOGGER = True