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
    cur.execute("DROP TABLE IF EXISTS flight;")

    # 테이블 생성
    cur.execute("""CREATE TABLE flight(
        name VARCHAR(255),
        leavetime INTEGER,
        reachtime INTEGER,
        seat VARCHAR(50),
        charge INTEGER,
        date DATE,
        day VARCHAR(10),
        airport VARCHAR(100),
        leavehour INTEGER)
    """)

    # csv 파일 속 데이터 옮기기 
    with open ('WonderBudget/data/csv/flight.csv', 'r') as f_file :
        f_reader = csv.DictReader(f_file)
        for data in f_reader:
            cur.execute("INSERT INTO flight(name, leavetime, reachtime, seat, charge, date, day, airport, leavehour) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                        (data['name'], data['leavetime'], data['reachtime'], data['seat'], data['charge'], data['date'], data['day'], data['airport'], data['leavehour']))
            
    conn.commit()

if __name__=='__main__':
    main()
