from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
PrometheusMetrics(app)  # adds /metrics automatically (for Prometheus)


@app.route("/")
def home():
    return jsonify(message="Hello TP4")


@app.route("/health")          # Kubernetes checks this to know the app is ready
def health():
    return jsonify(status="ok")


@app.route("/error")           # returns an error on purpose (for the Grafana 5xx graph)
def error():
    return jsonify(error="boom"), 500