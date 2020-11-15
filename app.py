from flask import Flask,jsonify
from flask.wrappers import Request
import json

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
def create_post(request):
    try:
        data = json.loads(request.args.get_data(as_text=True))
    except ValueError:
        return jsonify({"Error": "Error Decoding JSON"}), 400
    except TypeError as e:
        print(e)
        return jsonify({"Error": "Malformed JSON"}), 400

if __name__ == '__main__':
    app.run(debug=True)