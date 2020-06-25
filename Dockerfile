FROM python:3.7.7-slim-buster

RUN apt update && \
    apt install -y --no-install-recommends \
        build-essential \
        tini && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install -U pip setuptools wheel && \
    pip install -r requirements.txt

COPY . .

RUN python3 setup.py install

ENTRYPOINT ["tini", "--"]
CMD ["kyoho"]
