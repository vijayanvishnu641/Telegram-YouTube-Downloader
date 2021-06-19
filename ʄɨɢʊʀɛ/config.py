import  os
from աɛɮռʀ import *
from . import *

if os.path.exists("dev_var.py") and Kvar.KLOAD in LOADR:
    class Kati:
        TOKEN = ""
        APP_ID = ""
        API_HASH = ""
else:
    class Kati:
        TOKEN = os.environ.get("TOKEN")
        APP_ID = int(os.environ.get("API_ID"))
        API_HASH = os.environ.get("API_HASH")