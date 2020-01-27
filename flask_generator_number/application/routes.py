from flask import request, render_template
from application import app
import requests
import random

@app.route("/getRandomNumber", methods=["POST"])
def getNumber():
    return {"number":random.randint(0, 9)}
