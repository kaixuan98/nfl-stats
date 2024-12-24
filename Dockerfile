# syntax=docker/dockerfile:1

# sets the base image as official python image 
FROM python:3.12
WORKDIR /nfl-stats
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 8000
COPY . .
CMD [ "python", "src/server.py"]



