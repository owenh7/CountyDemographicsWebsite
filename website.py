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
        return render_template('index.html', states = get_state_options(counties), average_age = average_age(get_county_state(request.args['counties'],counties), counties), counties = get_county_options(get_county_state(request.args['counties'],counties),counties), county_age = get_county_age(request.args['counties'],counties))
    if 'states' in request.args:
        return render_template('index.html', states = get_state_options(counties), average_age = average_age(request.args['states'], counties), counties = get_county_options(request.args['states'],counties))
   
    elif 'states' not in request.args and 'counties' not in request.args:
        return render_template('index.html', states = get_state_options(counties))
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

def average_age(state, counties):
    print("RunningAge")
    points = float(0)
    total = float(0)
    for county in counties:
        if county["State"] == state:
            total = total + county["Age"]["Percent Under 18 Years"]
            points=points + 1
    avg = float(total//points)
    return avg

def get_county_options(states,counties):
    countylist = []
    print("RunningCOP")
    for county in counties:
        if county["State"] == states :
            countylist.append(county["County"])
    options = ""
    for data in countylist:
        options = options + Markup("<option value="" + data + "">" + data + "</option>")
    return options

def get_county_age(county, counties):
    print("RunningCAge")
    for county1 in counties:
        if county1["County"] == county:
            return county1["Age"]["Percent Under 18 Years"]
 
def get_county_state(county, counties):
    print("RunningState")
    state = ""
    for data in counties:
        if data["County"] == county:
            state = data["State"]
    return state

if name == "main":
    app.run(debug=True)

