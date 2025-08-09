from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("teddy_app.py")

if __name__ == "__main__":
    app.run(debug=True)
