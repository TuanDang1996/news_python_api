from flask import Flask, request
from flask_jsonpify import jsonify
from Source_Main.Main import SourceMain
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = SourceMain()
app.config['JSON_AS_ASCII'] = False

@app.route('/python_api/category/favorite/<userId>', methods=['GET'])
def favorite_category(userId):
    result = api.sortFavoriteTopic(userId)
    return jsonify(result)

@app.route('/python_api/category/<userId>', methods=['GET'])
def category(userId):
    result = api.sortAllTopic(userId)
    return jsonify(result)

@app.route('/python_api/article/<articleId>', methods=['GET'])
def getTopicOfArticle(articleId):
    result = api.findTopicByArticleId(articleId)
    return jsonify(result)

@app.route('/python_api/recomendArticles/<articleId>', methods=['GET'])
def getRelatedArticles(articleId):
    startIndex = int(request.args.get("startIndex")) if request.args.get("startIndex") != None else 0
    quantity = int(request.args.get("quantity"))
    print("Find "  + str(quantity) + " articles has id smaller than " + str(startIndex) + " relate on article has articleId is " + str(articleId))
    result = api.recomendRelatedArticles(articleId, quantity, startIndex)
    return jsonify(result)

if __name__ == '__main__':
    app.run(port=8181, debug=False, host='0.0.0.0')
