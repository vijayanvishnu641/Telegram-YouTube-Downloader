import  os

class Kryogenesis(object):
    TOKEN = os.environ.get("TOKEN", None)
    APP_ID = int(os.environ.get("API_ID", None))
    API_HASH = os.environ.get("API_HASH", None)
    KRYO = os.environ.get("KRYO", None)
    ENV = bool(os.environ.get("HEROKU", False))
class Vrit(Kryogenesis):
    LOGGER = True