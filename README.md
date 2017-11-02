# raspi_resin

Create a Web Server with Python and Flask
Python Docker image

FROM resin/raspberrypi3-python:2.7
# Enable systemd
ENV INITSYSTEM on
# Your code goes here

You can then build and run the Docker image:

docker build -t my-app .
docker run -it --rm --name my-running-app my-app


