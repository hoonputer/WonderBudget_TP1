from flask import Flask, render_template, request
import numpy as np
import joblib

# 플라스크 클래스명 지정
app = Flask(__name__)

# 모델 불러오기
h_model = joblib.load(open('WonderBudget/data/pkl/hotel_model.pkl', 'rb'))
f_model = joblib.load(open('WonderBudget/data/pkl/flight_model.pkl', 'rb'))
c_model = joblib.load(open('WonderBudget/data/pkl/car_model.pkl', 'rb'))

# 에러페이지
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# 메인 페이지
@app.route('/', methods = ['GET', 'POST'])
def index():
    # 처음 화면
    if request.method == 'GET':
        return render_template('index.heml')
    
    # 값 입력
    if request.method == 'POST':
        try:
            # 호텔 가격 예측
            h_data1 = float(request.form['h_data1'])   # 별점
            h_data2 = object(request.form['h_data2'])   # 지역
            h_data3 = object(request.form['h_data3'])   # 날짜
            h_array = np.array([[h_data3, h_data1, h_data2]])   # csv 순서와 동일하게 삽입
            h_pred = int(h_model.predict(h_array).round(1))

            # 항공권 가격 예측
            f_data1 = object(request.form['f_data1'])   # 항공사
            f_data2 = object(request.form['f_data2'])   # 좌석 등급
            f_data3 = object(request.form['f_data3'])   # 날짜
            f_array = np.array([[f_data1, f_data2, f_data3]])   # csv 순서와 동일하게 삽입
            f_pred = int(h_model.predict(f_array).round(1))

            # 렌트카 가격 예측
            c_data1 = int(request.form['c_data1'])   # 좌석 수
            c_data2 = object(request.form['c_data2'])   # 엔진 종류
            c_data3 = object(request.form['c_data3'])   # 날짜
            c_array = np.array([[c_data3, c_data2, c_data1]])   # csv 순서와 동일하게 삽입
            c_pred = int(h_model.predict(c_array).round(1))

            # 세 예측값 더하기
            pred = h_pred + f_pred + c_pred

            return render_template('index.html', pred = pred)
        
        except:
            return render_template('return.index')

if __name__ == "__main__":
    app.run(debug=True)
