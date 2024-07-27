FROM python:3.11
RUN curl -fsSL https://get.docker.com -o get-docker.sh && bash get-docker.sh
COPY . /opt/pynchon
RUN cd /opt/pynchon && pip install -q . && rm -rf /opt/pynchon
RUN apt-get update && apt-get install -y curl
ENTRYPOINT pynchon