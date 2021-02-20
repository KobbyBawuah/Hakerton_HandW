from flask import Flask, render_template, url_for, request, redirect
from datetime import datetime
from operator import itemgetter, attrgetter
import csv

# PROGRAMMED BY KWABENA GYASI BAWUAH

app = Flask(__name__)       # Use the flask Python web framework


# Renders the home web page
@app.route('/')
def home():
    return render_template('home.html')


# Renders the AboutUs web page
@app.route('/about')
def about():
    return render_template('about.html')


# Run the main program
if __name__ == "__main__":
    
    app.run(debug=True) # Add Port 8080 to run virtualenv on the Google Cloud App platform