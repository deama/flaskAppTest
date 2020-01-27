from flask import request
from application import app
import requests
import random
import string




@app.route("/getPrize", methods=["POST"])
def getPrize():
    sequence = request.json["sequence"]
    if len(sequence) == 20:
        try:
            if int(sequence[0]) == int(sequence[0]):
                try:
                    if int(sequence[2]) == int(sequence[2]):
                        try:
                            if int(sequence[7]) == int(sequence[7]):
                                return {"prize":"100,000"}
                        except ValueError:
                            return {"prize":"10,000"}
                except ValueError: 
                    return {"prize":"1,000"}
        except ValueError:
            pass

    return {"prize":"0"}
