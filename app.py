#!/usr/bin/env python3
"""
Simple iCalendar (.ics) file generator
"""
from datetime import datetime, timedelta
from flask import Flask, request, render_template, send_file
from icalendar import Calendar, Event
import os
import uuid

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data
        event_name = request.form.get('event_name')
        event_description = request.form.get('event_description')
        start_date = request.form.get('start_date')
        start_time = request.form.get('start_time')
        duration_hours = int(request.form.get('duration_hours', 1))
        
        # Create calendar event
        cal = Calendar()
        cal.add('prodid', '-//Simple iCal Generator//example.com//')
        cal.add('version', '2.0')
        
        event = Event()
        event.add('summary', event_name)
        event.add('description', event_description)
        
        # Parse start date and time
        start_datetime_str = f"{start_date} {start_time}"
        start_datetime = datetime.strptime(start_datetime_str, '%Y-%m-%d %H:%M')
        end_datetime = start_datetime + timedelta(hours=duration_hours)
        
        event.add('dtstart', start_datetime)
        event.add('dtend', end_datetime)
        
        # Add a unique identifier
        event.add('uid', str(uuid.uuid4()))
        
        cal.add_component(event)
        
        # Save the calendar to a file
        os.makedirs('generated_files', exist_ok=True)
        filename = f"event_{start_datetime.strftime('%Y%m%d_%H%M')}.ics"
        filepath = os.path.join('generated_files', filename)
        
        with open(filepath, 'wb') as f:
            f.write(cal.to_ical())
        
        return send_file(filepath, as_attachment=True, download_name=filename)
    
    return render_template('index.html')

if __name__ == '__main__':
    os.makedirs('templates', exist_ok=True)
    app.run(debug=True, host='0.0.0.0', port=5000) 