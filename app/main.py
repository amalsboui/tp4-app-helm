from flask import Flask, jsonify
from flask_wtf.csrf import CSRFProtect          
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
CSRFProtect(app)                               
PrometheusMetrics(app)


@app.route("/")
def home():
    return jsonify(message="Hello TP4")


@app.route("/health")
def health():
    return jsonify(status="ok")


@app.route("/error")
def error():
    return jsonify(error="boom"), 500