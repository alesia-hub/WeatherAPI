from flask import Flask, render_template
import requests

app = Flask(__name__)

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
@app.route("/api/v1/<station>/<date>")
def api_weather(station, date):
    return {
        "station": station,
        "date": date,
        "temperature": "22C",
        "condition": "Sunny"
    }

@app.route("/api/v1/<word>")
def api_definition(word):
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
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
    app.run(host='0.0.0.0', port=5001, debug=True)