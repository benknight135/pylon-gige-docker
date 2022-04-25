FROM ubuntu:20.04

WORKDIR /usr/src/app

# Install packages
RUN apt update && \
    apt install -y \
    sudo \
    curl \
    python3 \
    python3-distutils && \
    rm -rf /var/lib/apt/lists/*

# Install pip
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
    python3 get-pip.py && \
    rm -rf get-pip.py

# Install OpenCV dependencies
RUN apt update && \
    TZ=Europe/London \
    DEBIAN_FRONTEND=noninteractive \
    apt install -y python3-opencv && \
    rm -rf /var/lib/apt/lists/*

# Install python requirements
COPY app/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt && \
    rm -rf ./requirements.txt

RUN apt update && \
    apt install -y \
    net-tools telnet iputils-ping iproute2 && \
    rm -rf /var/lib/apt/lists/*

# Add app data
COPY app/. ./

CMD [ "python3", "./run.py" ]