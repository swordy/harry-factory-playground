from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

VERSION = "1.0.0"
STATUS = "OK"

_STATUS_TEMPLATE = """<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>Service Status</title>
</head>
<body>
  <h1>Service Status</h1>
  <p>Version: {{ version }}</p>
  <p>State: {{ status }}</p>
</body>
</html>"""


@app.get("/version")
def get_version():
    return jsonify({"version": VERSION})


@app.get("/status")
def get_status():
    return render_template_string(_STATUS_TEMPLATE, version=VERSION, status=STATUS)


if __name__ == "__main__":
    app.run()
