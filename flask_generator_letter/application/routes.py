from flask import request
from application import app
import requests
import random
import string

@app.route("/getRandomLetter", methods=["POST"])
def getLetter():
    return {"letter":random.choice(string.ascii_letters)}



