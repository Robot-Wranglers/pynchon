# NB: oldest theoretically supported is python:3.9, per setup.cfg
FROM python:3.11
RUN apt-get update && apt-get install -y python3-dev curl make procps libsqlite3-dev
RUN curl -fsSL https://get.docker.com -o get-docker.sh && bash get-docker.sh
COPY . /opt/pynchon
RUN pip install cython 
RUN cd /opt/pynchon && pip install -q . && rm -rf /opt/pynchon
RUN pip freeze > pip.freeze.txt
RUN pynchon plugins list > pynchon.plugins.txt
RUN apt-get install -y -qq jq
ENTRYPOINT ['pynchon']