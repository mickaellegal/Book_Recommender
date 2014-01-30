from flask import Flask, request, render_template, jsonify
from yhat import Yhat
import os


app = Flask(__name__)
yh = Yhat(os.environ.get("YHAT_USERNAME"), os.environ.get("YHAT_APIKEY"))


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method=="GET":
        return render_template("home.html")
    else:
        data = request.form
    
        data = {
            "title": data['book'],
        }
        
    results = yh.predict("BookReco", 3, data['title'])

    return jsonify({"results": results})
  

if __name__ == '__main__':
    app.run(port=int(os.environ.get('PORT', 5000)))

