FROM python:latest
ENV VIRTUAL_ENV "/venv"
RUN python -m venv $VIRTUAL_ENV
ENV PATH "$VIRTUAL_ENV/bin:$PATH"
RUN apt-get update && apt-get upgrade -y
RUN python -m pip install --upgrade pip
RUN git clone https://github.com/calitronx/Telegram-YouTube-Downloader.git
RUN cd Telegram-YouTube-Downloader
WORKDIR /Telegram-YouTube-Downloader
CMD python3 boot.py
 