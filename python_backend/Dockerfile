# Use an official node image as our base image
FROM python:3.8-slim

# Set the working directory to /contacts_app
WORKDIR ${WORKDIR_BACKEND}

# Make back end of this container available to the world outside this container
EXPOSE ${BACKEND_PORT}

# Which mode are we working in
# ENV FLASK_ENV=development
ENV FLASK_ENV=production

# Copy the requirements file
COPY ./requirements.txt .

# Allow pip to install packages for apt
ENV PIP_BREAK_SYSTEM_PACKAGES 1 

# Install dependencies
# RUN apt-get update && apt-get install python3-pip libgl1 libglib2.0-0  -y
RUN apt-get update && apt-get install python3-pip -y
RUN pip3 install --upgrade pip
# use .env vars
RUN pip install python-dotenv 
RUN pip3 install -r requirements.txt

# Copy in the rest of the files
# COPY ./python_backend .
COPY . .

CMD ["python3", "main.py"]
