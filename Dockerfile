FROM python:3.8-slim-buster

RUN apt-get update && apt-get install -y \
    curl \
    git \
    jq \
    libgl1-mesa-glx \
    libglib2.0-0

RUN python3 -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /app

RUN useradd -ms /bin/bash msam

RUN chown -R msam:msam /app

RUN chown -R msam:msam /opt/venv

RUN chmod 700 /app

USER msam

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["fastapi", "run", "main.py"]