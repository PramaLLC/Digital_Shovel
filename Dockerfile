FROM python:3.9

RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    libglib2.0-0 \
    libnss3 \
    libgconf-2-4 \
    libfontconfig1 \
    libxrender1 \
    libxtst6 \
    xvfb

RUN apt-get update && apt-get install -y wget unzip && \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb && \
    apt-get clean

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 -y

RUN apt-get update && apt-get install libgl1


WORKDIR /app

COPY requirements.txt .

# Install packages using pip
RUN pip install --no-cache-dir -r requirements.txt


# Echo a message to indicate that the base image has finished installing packages
CMD ["echo", "Base image finished installing packages"]


ENV PORT=2000




WORKDIR /app


# Copy the rest of the application code to the working directory
COPY . .


EXPOSE 2000 


# Specify the command to run when the container starts
CMD ["python", "main.py"]