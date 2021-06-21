from .exfile import Kryogenesis

if Kryogenesis.ENV == "HEROKU":
    from .exfile import Vrit as Kryogenesis
else:
    from .config import Kryogenesis