# Base Image
FROM python:2.7
# Copy directory
ADD . /code
# set working directory
WORKDIR /code
# .. run these commands
RUN pip install -r requirements.txt
