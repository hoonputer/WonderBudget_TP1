import psycopg2
import csv
import sys

host = 'tiny.db.elephantsql.com'
user = 'lpghxeum'
password = '1_lBDFx8EAeNLxViXu-wY84ciSOaMqs-'
database = 'lpghxeum'

def main():
    # postgresql 연결
    try:
        conn = psycopg2.connect(
            host = host,
            user = user,
            password = password,
            database = database
        )
        # 커서 생성
        cur = conn.cursor()
    except:
        sys.exit()

    # 만약 테이블이 이미 있다면 삭제
    cur.execute("DROP TABLE IF EXISTS car;")

    # 테이블 생성
    cur.execute("""CREATE TABLE car(
        date DATE,
        week VARCHAR(50),
        car_name VARCHAR(255),
        price INTEGER,
        engine VARCHAR(50),
        seater INTEGER)
    """)

    # csv 파일 속 데이터 옮기기
    with open ('WonderBudget/data/csv/car.csv', 'r') as c_file :
        c_reader = csv.DictReader(c_file)
        for data in c_reader:
            cur.execute("INSERT INTO car(date, week, car_name, price, engine, seater) VALUES (%s, %s, %s, %s, %s, %s)",
                        (data['date'], data['week'], data['car_name'], data['price'], data['engine'], data['seater']))
            
    conn.commit()

if __name__=='__main__':
    main()
