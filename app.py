from logging import error
from flask import Flask,jsonify,request
import json
import logging
from backend import common

app = Flask(__name__)

posts = [
    {"id": 1, "title": "Abohar Clean?", "year": 2015, "likes": 0},
    {"id": 2, "title": "Serdar Burak Guneri", "year": 2015, "likes": 0}
]

@app.route("/post/<id>", methods = ['GET'])
@app.route("/post", methods = ['GET'])
def get_post(id=None):
    if id == None:
        return jsonify({ "posts" : posts[:]})
    else:
        for post in posts:
            if post['id'] == int(id):
                post = {
                    "id": post['id'],
                    "title": post['title'],
                    "year": post['year'],
                    "likes": post['likes']
                }
                return jsonify({ "posts" : [post]})
                break

        return jsonify({ "posts": []})

@app.route("/post", methods = ['POST'])
def create_post():
    _data = request.get_data(cache=False, as_text=True)
    try:
        _data = json.loads(_data)
    except json.decoder.JSONDecodeError as e:
        logging.error(e)
        return jsonify({"error": str(e)}), 400

    _c,_e = common.validate_post(_data)
    if _c:
        return str(common.create_post(_data)), 200
    else:
        return jsonify({"error": _e}), 400

if __name__ == '__main__':
    common.setLoggingFormat(logging.DEBUG)
    app.run(debug=True)