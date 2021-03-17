from flask import Flask, request, render_template, jsonify
from functools import lru_cache
import overpass
api = overpass.API()
import sqlite3
app = Flask(__name__)

@app.after_request
def add_cors_headers(response):
    r = request.referrer[:-1]
    response.headers.add('Access-Control-Allow-Origin', r)
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Headers', 'Cache-Control')
    response.headers.add('Access-Control-Allow-Headers', 'X-Requested-With')
    response.headers.add('Access-Control-Allow-Headers', 'Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, DELETE')
    return response

@app.route("/api")
def api_root():
    return jsonify({"restos": "/api/restos/"})


@app.route('/api/restos/')
def restos():
    return 'Hello!'

@lru_cache()
def getCity(city):
    response = api.get (f"""area[name="{city}"]; node[amenity=restaurant](area);""")
    return response

@app.route("/api/restos/<city>", methods=["GET", "PUT"])
def store(city):
    if request.method == "GET":
        response = getCity(city)
        return response





#     memory = {}

# @app.route("/api/restos/<key>", methods=["GET", "PUT"])
# def stoaare(key):
#     if request.method == "GET":
#         return memory.get(key, "aa")
#     else:
#         memory[key] = request.get_data()
#         return ""
    