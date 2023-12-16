FROM python:3.11-slim

ENV PYTHONUNBUFFERED 1
ENV LANG ru_RU.UTF-8
ENV TZ Asia/Yekaterinburg

RUN apt-get update &&  \
    apt-get install --no-install-recommends -y \
    libpq-dev \
    binutils \
    gcc \
    git && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /code
COPY . /code

RUN pip install --no-cache-dir -r requirements.txt

RUN python -m spacy download ru_core_news_lg

CMD ["python", "-m", "app"]
