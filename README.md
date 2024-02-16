# Speech-to-Text Service with Flask

## Introduction

This is a simple Flask application that provides a speech-to-text (STT) service using the Google Cloud Speech-to-Text API. Users can upload audio files, and the application will transcribe the speech in the files into text.


## Prerequisites

Before running this application, make sure you have the following:

- Python 3.10 installed on your system
- Google Cloud Platform (GCP) account with Cloud Speech-to-Text API enabled
- Service account key file (JSON format) with necessary permissions for accessing Cloud Speech-to-Text API and Cloud Storage
- Docker installed on your system (optional)


## Installation

1. Clone this repository to your local machine:

```bash
git clone https://github.com/chinghao-tw/simple-flask-google-stt.git
cd simple-flask-google-stt
pip install -r requirements.txt
```

## Configuration

1. Set up the service account key file:  
Place your Google service account key file (JSON format) in the project directory with the name `gcp-service-account.json`.

2. Set the environment variables:  
In `app.py`, replace `your-bucket-name` with the name of your Google Cloud Storage bucket.


## Usage
Run the Flask application using the following command:

```bash
python app.py
```

The application will start and listen on port 8080 by default. You can access the application at `http://localhost:8080` in your web browser.


## Docker
Alternatively, you can run the application using Docker. Build the Docker image using the following command:

```bash
docker build -t your-app-name .
```

Then run the Docker container:

```bash
docker run -p 8080:8080 your-app-name
```

## License
This project is licensed under the [MIT License](LICENSE).

