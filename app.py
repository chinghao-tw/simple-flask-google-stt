import os
from flask import Flask, request, render_template
from google.cloud import storage, speech

app = Flask(__name__)

# Set Google Cloud Storage Bucket name
BUCKET_NAME = os.getenv('BUCKET_NAME', "your-bucket-name")
PORT = os.getenv('PORT', 8080)

# Initialize Google Cloud Storage and Speech clients
storage_client = storage.Client()
speech_client = speech.SpeechClient()

# Define function to transcribe audio file
def transcribe_audio(file_uri):
    audio = speech.RecognitionAudio(uri=file_uri)
    config = speech.RecognitionConfig(language_code='en-US')
    response = speech_client.recognize(config=config, audio=audio)
    transcription = ""
    for result in response.results:
        transcription += result.alternatives[0].transcript + "\n"
    return transcription

# Define route to handle file upload
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    transcription = None
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file:
            # Check if BUCKET_NAME is set
            if BUCKET_NAME:
                # Upload the file to Google Cloud Storage
                bucket = storage_client.bucket(BUCKET_NAME)
                blob = bucket.blob(uploaded_file.filename)
                blob.upload_from_file(uploaded_file)
                
                # Get the GCS URI of the uploaded file
                file_uri = f'gs://{BUCKET_NAME}/{uploaded_file.filename}'

                # Transcribe the audio file
                transcription = transcribe_audio(file_uri)
            else:
                return "Error: Bucket name is not set. Please set the BUCKET_NAME environment variable."
    return render_template('upload.html', transcription=transcription)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=PORT)
