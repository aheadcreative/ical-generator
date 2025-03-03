# Simple iCalendar Generator

A simple web application to generate .ics (iCalendar) files for events.

## Features

- Create events with name, description, start date/time, and duration
- Download generated .ics files that can be imported into calendar applications
- Simple, user-friendly web interface

## Local Setup

1. Clone this repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the application:
   ```
   python app.py
   ```
4. Open your browser and navigate to `http://localhost:5000`

## Deployment Options

### Option 1: Deploy to Render (Simplest)

1. Create a free account on [Render](https://render.com/)
2. Create a new Web Service
3. Connect your GitHub repository (or upload the code)
4. Set the following:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
5. Click "Create Web Service"

### Option 2: Deploy to PythonAnywhere

1. Create a free account on [PythonAnywhere](https://www.pythonanywhere.com/)
2. Upload your files or clone your repository
3. Create a new web app with Flask
4. Configure the WSGI file to point to your app
5. Set up a virtual environment with your requirements

### Option 3: Deploy to Heroku

1. Create a Procfile with the content: `web: gunicorn app:app`
2. Create a free Heroku account
3. Install the Heroku CLI
4. Run:
   ```
   heroku login
   heroku create
   git push heroku main
   ```

## Usage

1. Fill in the event details in the web form
2. Click "Generate iCalendar File"
3. The .ics file will be downloaded automatically
4. Import the .ics file into your calendar application (Google Calendar, Outlook, Apple Calendar, etc.) 