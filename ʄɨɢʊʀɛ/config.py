import  os
from աɛɮռʀ import *
from .dev_var import *

if Kvar.KLOAD in LOADR:
    class Kati:
        TOKEN = "1869507072:AAFzDcb5uwVwO7a59vlrf0H9e5crSh_lZM4"
        APP_ID = 6372795
        API_HASH = "4b7731b0a6d8e15bef82863887feb293"
else:
    class Kati:
        TOKEN = os.environ.get("TOKEN")
        APP_ID = int(os.environ.get("API_ID"))
        API_HASH = os.environ.get("API_HASH")