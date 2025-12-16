from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def weather():
    return render_template("weather.html")

@app.route("/about")
def about():
    return render_template("about.html")

# now creating API:
@app.route("/api/v1/<station>/<date>")
def api_weather(station, date):
    return {
        "station": station,
        "date": date,
        "temperature": "22C",
        "condition": "Sunny"
    }

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)