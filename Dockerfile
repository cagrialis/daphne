FROM ubuntu:kinetic

RUN  apt-get update -y \
     && apt install curl -y \
     && apt install software-properties-common -y \
     && add-apt-repository ppa:deadsnakes/ppa -y \
     && apt install python3.8 -y \
     && apt install python3-pip

RUN  apt-get install nmap -y \
     && apt-get install git -y \
     && git clone https://github.com/cagrialis/daphne.git \
     && cd daphne 
     && pip3 install -r requirements.txt

RUN  add-apt-repository ppa:longsleep/golang-backports \
     && apt update \
     && apt install golang-go -y

RUN  cd opt\
     && git clone https://github.com/projectdiscovery/nuclei.git \
     && cd nuclei/v2/cmd/nuclei/ \
     && go build . \
     && mv nuclei /usr/local/bin/