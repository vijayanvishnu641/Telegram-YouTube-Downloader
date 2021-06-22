import os
class Kryogenesis(object):
    # YOUGENIS_KEY = ("TIMXRCTC0RSPYKAEVRTNITVERLER")
    # TOKEN = ("1701848148:AAHguzmA7FKmAqOFob_ZzaGif6F1v3jKl5s")
    # APP_ID = int(("6372795"))
    # API_HASH = ("4b7731b0a6d8e15bef82863887feb293")
    YOUGENIS_KEY = os.environ.get("YOUGENIS_KEY")
    TOKEN = os.environ.get("TOKEN")
    APP_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")
class Hypotherm(Kryogenesis):
    LOGGER = True