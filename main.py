from flask import Flask, render_template
import requests

app = Flask(__name__)

# creating web pages:
@app.route("/")
def weather():
    return render_template("weather.html")

@app.route("/about")
def about():
    return render_template("about.html", data="api data to display")

@app.route("/word")
def wird_definition():
    return render_template("word.html")

# now creating API:
@app.route("/api/v1/weather/<station>/<date>")
def api_weather(station, date):
    return {
        "station": station,
        "date": date,
        "temperature": "22C",
        "condition": "Sunny"
    }

@app.route("/api/v1/weather/<station>")
def api_weather_station(station):
    """
    Function will only return raw json format response. 
    In reality this should be processing some DB stored data and return proper response.
    :param: station: weather station id
    """
    return {
        "station": station,
        "temperature": "22C",
        "condition": "Sunny"
    }

@app.route("/api/v1/definition/<word>")
def api_definition(word):
    """
    Method will trigger dictionary API to fetch definition for a given word.
    
    :param word: word to fetch definition for
    """
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}",
                            timeout=10)
    data = response.json()
    if data:
        definition = data[0]['meanings'][0]['definitions'][0]['definition']
    else:
        definition = "No definition found"
    return {
        "definition": definition,
        "word": word
    }

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=False)