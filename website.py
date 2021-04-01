from flask import Flask, request, Markup, render_template, flash, Markup 
import os
import json

app = Flask(__name__)

@app.route("/")
def render_main():
    print("RunningMain")
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
        
if 'counties' in request.args:
        return render_template('home.html', states = get_state_options(counties), average_age = average_age(get_county_state(request.args['counties'],counties), counties), counties = get_county_options(get_county_state(request.args['counties'],counties),counties), county_age = get_county_age(request.args['counties'],counties))

    if 'states' in request.args:
        return render_template('home.html', states = get_state_options(counties), average_age = average_age(request.args['states'], counties), counties = get_county_options(request.args['states'],counties))
   
elif 'states' not in request.args and 'counties' not in request.args:
        return render_template('home.html', states = get_state_options(counties))

    def get_state_options(counties):
    states = []
    print("RunningOP")
    for data in counties:
        if data["State"] not in states:
            states.append(data["State"])
    options = ""
    for data in states:
        options = options + Markup("<option value="" + data + "">" + data + "</option>")
    return options

