from logging import INFO, basicConfig, getLogger
basicConfig(
format="%(levelname)s - %(message)s",
level=INFO)
LOGS = getLogger(__name__)
DOWNLOAD_LOCATION = "/app/downloads/"