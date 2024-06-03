# Use an official node image as our base image
FROM node:slim

# Set the working directory to /app
WORKDIR /urs/app/contacts_app

# Make port ${PORT} from .env of this container available to the world outside this container
EXPOSE ${PORT}

# Which mode are we working in (comment out for production mode)
ENV FLASK_ENV=development

# Copy the requirements file
COPY ./requirements.txt .

# Allow pip to install packages for apt
ENV PIP_BREAK_SYSTEM_PACKAGES 1 

# Install dependencies
# RUN apt-get update && apt-get install python3-pip libgl1 libglib2.0-0  -y
RUN apt-get update && apt-get install python3-pip -y
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# Copy in the rest of the files
COPY . .

RUN cd webapp && yarn install && cd ..

ENTRYPOINT ["bash", "start_docker.sh"]
