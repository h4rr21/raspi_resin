FROM resin/raspberrypi3-python:2.7
# Enable systemd
ENV INITSYSTEM on
# Defines our working directory in container
WORKDIR /usr/src/app
#Copy project apps
COPY . /usr/src/app
# install deps
RUN pip install -r requirements.txt
# run strip to start everything
CMD ["sh","start.sh"]