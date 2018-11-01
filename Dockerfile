FROM ubuntu:18.04

RUN apt-get update && apt-get install -y python3 python3-pip

RUN pip3 install numpy matplotlib scipy matplotlib pytest sphinx sphinx_rtd_theme

WORKDIR /app
