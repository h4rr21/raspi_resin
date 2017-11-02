FROM resin/raspberrypi3-python:2.7
# Enable systemd
ENV INITSYSTEM on
# install deps
COPY . .
RUN pip install -r requirements.txt
# run flask app
EXPOSE 5000
CMD ["python", "hello.py"]