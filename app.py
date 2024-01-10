from flask import render_template
import connexion

app = connexion.FlaskApp(__name__)
app.add_api("swagger.yml")

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)