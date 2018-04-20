FROM debian:stretch

WORKDIR /home/bagoftasks

ADD . /home/bagoftasks

RUN apt-get update && apt-get install -y \
    git \
    vim \
    python3 \
    python3-pip \
    libpq-dev \
    postgresql \
    postgresql-contrib \
    pwgen && rm -rf /var/lib/apt/lists/*

RUN pip3 install .

EXPOSE 8000
