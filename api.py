# api_basic.py
import json
from flask import Blueprint, jsonify
import os

bp = Blueprint("api", __name__, url_prefix="/api")

DATA_PATH = "data/calculations.json"
VERSION_PATH = "data/metadata_version.txt"

def load_metadata():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def load_version():
    if os.path.exists(VERSION_PATH):
        return open(VERSION_PATH).read().strip()
    return "0.0.0"   


@bp.route("/metadata/version", methods=["GET"])
def metadata_version():
    return jsonify({"version": load_version()})


@bp.route("/metadata", methods=["GET"])
def metadata():
    data = load_metadata()
    return jsonify({
        "version": load_version(),
        "data": data
    })
