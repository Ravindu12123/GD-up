FROM python:3.10-slim


COPY app/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


CMD gunicorn app:app & python3 bot.py
