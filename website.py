from flask import Flask, request, Markup, render_template, flash, Markup import os
import json

@app.route("/")
def render_main():
    return render_template('home.html')
