from flask import Flask, render_template, request
import numpy as np
import joblib

# 플라스크 클래스명 지정
app = Flask(__name__)

# 모델 불러오기

# 에러페이지
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# 메인 페이지
@app.route('/', methods = ['GET'])
def index():
    return render_template('index.heml')



if __name__ == "__main__":
    app.run(debug=True)