# syntax=docker/dockerfile:1

# sets the base image as official python image 
FROM python:3.12

# create a working directory for the code
WORKDIR /code/nfl-stats

# install all the packages
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy your application files to the current directory
COPY . .

# expose the port 
EXPOSE 8000

# command to run the startup script
CMD [ "python", "src/server.py"]



