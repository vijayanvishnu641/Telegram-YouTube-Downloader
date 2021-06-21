import os
class Kryogenesis(object):
    # API_HASH = '4b7731b0a6d8e15bef82863887feb293'
    # APP_ID = 6372795
    # TOKEN = '1869507072:AAFzDcb5uwVwO7a59vlrf0H9e5crSh_lZM4'
    YOUTUBE_KEY = os.environ.get("YOUTUBE_KEY")
    TOKEN = os.environ.get("TOKEN")
    APP_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")
class Hypotherm(Kryogenesis):
    LOGGER = True