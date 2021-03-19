from flask import Flask, request, Markup, render_template, flash, Markup 
app = Flask(_name_)
import os
import json

@app.route("/")
def render_main():
    return render_template('home.html')

def get_state_options
    states = []
    print
