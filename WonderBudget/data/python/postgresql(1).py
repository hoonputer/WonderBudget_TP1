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
    cur.execute("DROP TABLE IF EXISTS hotel;")
    cur.execute("DROP TABLE IF EXISTS flight;")
    cur.execute("DROP TABLE IF EXISTS car;")

    # 테이블 생성
    cur.execute("""CREATE TABLE hotel(
        Hotel_name VARCHAR(255),
        Date DATE,
        Price INTEGER,
        Client INTEGER,
        Rating FLOAT,
        Grade INTEGER,
        Address VARCHAR(255),
        Day VARCHAR(10))
    """)
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
    cur.execute("""CREATE TABLE car(
        date DATE,
        week INTEGER,
        car_name VARCHAR(255),
        price INTEGER,
        engine VARCHAR(50),
        seater INTEGER)
    """)

    # csv 파일 속 데이터 옮기기
    with open ('WonderBudget/data/csv/hotel.csv', 'r') as h_file :
        h_reader = csv.DictReader(h_file)
        for data in h_reader:
            cur.execute("INSERT INTO hotel(Hotel_name, Date, Price, Client, Rating, Grade, Address, Day) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                        (data['Hotel_name'], data['Date'], data['Price'], data['Client'], data['Rating'], data['Grade'], data['Address'], data['Day']))
            
    with open ('WonderBudget/data/csv/flight.csv', 'r') as f_file :
        f_reader = csv.DictReader(f_file)
        for data in f_reader:
            cur.execute("INSERT INTO flight(name, leavetime, reachtime, seat, charge, date, day, airport, leavehour) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                        (data['name'], data['leavetime'], data['reachtime'], data['seat'], data['charge'], data['date'], data['day'], data['airport'], data['leavehour']))
            
    with open ('WonderBudget/data/csv/car.csv', 'r') as c_file :
        c_reader = csv.DictReader(c_file)
        for data in c_reader:
            cur.execute("INSERT INTO car(date, week, car_name, price, engine, seater) VALUES (%s, %s, %s, %s, %s, %s)",
                        (data['date'], data['week'], data['car_name'], data['price'], data['engine'], data['seater']))

    conn.commit()

if __name__=='__main__':
    main()
