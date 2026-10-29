from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Cloud DevOps Portfolio Project</h1><p>Deployed with Docker, Terraform, ECS Fargate, and GitHub Actions.</p>"

@app.route("/health")
def health():
    return jsonify(status="healthy"), 200
