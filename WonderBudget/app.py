from flask import Flask, render_template, request
#import numpy as np
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# 플라스크 클래스명 지정
app = Flask(__name__)

# 모델 불러오기
h_model = joblib.load(open('/Users/hyunjulee/tp1/WonderBudget_TP1/WonderBudget/data/pkl/hotel_model.pkl', 'rb'))
f_model = joblib.load(open('/Users/hyunjulee/tp1/WonderBudget_TP1/WonderBudget/data/pkl/flight_model.pkl', 'rb'))
c_model = joblib.load(open('/Users/hyunjulee/tp1/WonderBudget_TP1/WonderBudget/data/pkl/car_model.pkl', 'rb'))
h_encoder = joblib.load(open('/Users/hyunjulee/tp1/WonderBudget_TP1/WonderBudget/data/pkl/hotel_encoder.pkl', 'rb'))
f_encoder = joblib.load(open('/Users/hyunjulee/tp1/WonderBudget_TP1/WonderBudget/data/pkl/flight_encoder.pkl', 'rb'))
c_encoder = joblib.load(open('/Users/hyunjulee/tp1/WonderBudget_TP1/WonderBudget/data/pkl/car_encoder.pkl', 'rb'))

# 에러페이지
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# 메인 페이지
@app.route('/', methods = ['GET', 'POST'])
def index():
    # 처음 화면
    if request.method == 'GET':
        return render_template('index.html')
    
    # 값 입력
    if request.method == 'POST':
        try:
            # 호텔 가격 예측
            h_data1 = request.form['h_data1']   # 날짜
            h_data2 = float(request.form['h_data2'])   # 평점
            h_data3 = int(request.form['h_data3'])   # 등급
            h_data4 = request.form['h_data4']   # 지역
            h_data = {
                'Date' : [h_data1],
                'Rating' : [h_data2],
                'Grade' : [h_data3],
                'Address' : [h_data4]
            }
            h_df = pd.DataFrame(h_data, columns=['Date', 'Rating', 'Grade', 'Address'])   # 데이터프레임 형태로 변환
            h_df_encoded = h_encoder.transform(h_df)   # 모델 만들때와 동일한 인코더
            h_pred = int(h_model.predict(h_df_encoded).round(1))

            # 출발 항공권 가격 예측
            f_data1 = request.form['f_data1']   # 항공사
            f_data2 = request.form['f_data2']   # 좌석 종류
            f_data3 = request.form['f_data3']   # 날짜
            f_data4 = request.form['f_data4']   # 공항
            f_data = {
                'name' : [f_data1],
                'seat' : [f_data2],
                'date' : [f_data3],
                'airport' :[f_data4]
            }
            f_df = pd.DataFrame(f_data, columns=['name', 'seat', 'date', 'airport'])   # 데이터프레임 형태로 변환
            f_df_encoded = f_encoder.transform(f_df)   # 모델 만들때와 동일한 인코더
            f_pred = int(f_model.predict(f_df_encoded).round(1))

            # 도착 항공권 가격 예측
            f_data11 = request.form['f_data11']   # 항공사
            f_data12 = request.form['f_data12']   # 좌석 종류
            f_data13 = request.form['f_data13']   # 날짜
            f_data14 = request.form['f_data14']   # 공항
            f_data100 = {
                'name' : [f_data11],
                'seat' : [f_data12],
                'date' : [f_data13],
                'airport' :[f_data14]
            }
            f_df100 = pd.DataFrame(f_data100, columns=['name', 'seat', 'date', 'airport'])   # 데이터프레임 형태로 변환
            f_df_encoded100 = f_encoder.transform(f_df100)   # 모델 만들때와 동일한 인코더
            f_pred100 = int(f_model.predict(f_df_encoded100).round(1))

            # 렌트카 가격 예측
            c_data1 = request.form['c_data1']   # 날짜
            c_data2 = request.form['c_data2']   # 엔진 종류
            c_data3 = int(request.form['c_data3'])   # 좌석 수
            c_data = {
                'date' : [c_data1],
                'engine' : [c_data2],
                'seater' : [c_data3],
            }
            c_df = pd.DataFrame(c_data, columns=['date', 'engine', 'seater'])   # 데이터프레임 형태로 변환
            c_df_encoded = c_encoder.transform(c_df)   # 모델 만들때와 동일한 인코더
            c_pred = int(c_model.predict(c_df_encoded).round(1))

            # 세 예측값 더하기
            pred = h_pred + f_pred + c_pred + f_pred100

            return render_template('index.html', pred = pred)
        
        except Exception as e:
            print(f"예측 도중 오류 발생: {e}")
            return render_template('return.html')

if __name__ == "__main__":
    app.run(debug=True)

