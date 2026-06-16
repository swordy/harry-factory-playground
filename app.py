from flask import Flask, jsonify

app = Flask(__name__)

VERSION = "1.0.0"


@app.get("/version")
def get_version():
    return jsonify({"version": VERSION})


if __name__ == "__main__":
    app.run()
