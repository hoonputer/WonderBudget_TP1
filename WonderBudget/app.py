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

# 예산이 정해져 있다면?
@app.route('/yes_budget', methods = ['GET', 'POST'])
def yes_budget():
    # '예산이 정해져 있다'를 선택했을 때 보이는 창
    if request.method == 'GET':
        return render_template('-.html')
    
    # 단순 추천 시스템을 활용해 추천 호텔, 항공권, 렌터카 보여주기
    if request.methodn == 'POST':

        return render_template('-.html')

# 예산이 정해져 있지 않다면?
@app.route('/no_budget', methods = ['GET', 'POST'])
def no_budget():
    # '정해진 예산이 없다'를 선택했을 때 보이는 창
    if request.method == 'GET':
        return render_template('-.html')

    # 머신러닝을 활용하여 대략적인 총 비용 보여주기
    if request.methodn == 'POST':

        return render_template('-.html')

if __name__ == "__main__":
    app.run(debug=True)
