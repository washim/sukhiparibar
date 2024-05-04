FROM python:latest
RUN useradd ec2-user
EXPOSE 8001
ENV PYTHONUNBUFFERED=1 \
    PORT=8001

RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    libpq-dev \
    default-libmysqlclient-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
    ffmpeg libsm6 libxext6 \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /
RUN pip install -r /requirements.txt
WORKDIR /app
RUN chown ec2-user:ec2-user /app
COPY --chown=ec2-user:ec2-user . .
USER ec2-user
CMD python manage.py runserver 0.0.0.0:8001