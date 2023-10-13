FROM python:3.10.6

RUN mkdir /tz_bewise

WORKDIR /tz_bewise

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .