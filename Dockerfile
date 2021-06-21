FROM jrottenberg/ffmpeg:4.0-alpine
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python3 python3-pip python3-dev
RUN python -m pip install --upgrade pip
RUN git clone https://github.com/calitronx/Telegram-YouTube-Downloader.git
RUN cd Telegram-YouTube-Downloader
WORKDIR /Telegram-YouTube-Downloader
CMD python3 boot.py
 