from flask import Flask,jsonify

app = Flask(__name__)

posts = [
    {"id": 1, "title": "Abohar Clean?", "year": 2015, "likes": 0},
    {"id": 2, "title": "Serdar Burak Guneri", "year": 2015, "likes": 0}
]

@app.route("/post/<id>", methods = ['GET'])
@app.route("/post", methods = ['GET'])
def get_post(id=None):
    if id == None:
        if len(posts) < 10:
            return jsonify({ "posts" : posts[:]})
        else:
            return jsonify({ "posts" : posts[:10]})
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
if __name__ == '__main__':
    app.run(debug=True)