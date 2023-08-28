FROM python:3.11-slim-buster


WORKDIR .
RUN apt -qq update && apt -qq install -y git wget pv jq python3-dev ffmpeg mediainfo aria2 curl
COPY . .
RUN pip3 install -r requirements.txt
RUN apt install ffmpeg aria2

CMD ["python3", "main.py"]
