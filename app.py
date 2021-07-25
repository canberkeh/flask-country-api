from os import name
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

api_url = "https://restcountries.eu/rest/v2/name/"


@app.route('/',methods = ["GET","POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        response_country = requests.get(api_url + name)

        country_info = response_country.json()

        if "message" in country_info:   # Error Case  ---> {"status":404,"message":"Not Found"}
           return render_template("index.html", error = "Country not found !") 

        else:
            return render_template("index.html", country = country_info)
    else:
        return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)