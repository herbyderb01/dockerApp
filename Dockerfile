# Use an official Python runtime as our base image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /urs/app/contactsApp

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN apt-get update && apt-get install python3-pip libgl1 libglib2.0-0  -y
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# Copy the backend code
COPY backend /app/backend

# Copy the frontend code
COPY frontend /app/frontend

# Make port 5125 of this container available to the world outside this container
EXPOSE 5125

# Run flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=5125"]

ENTRYPOINT ["bash", "start_docker.sh"]
