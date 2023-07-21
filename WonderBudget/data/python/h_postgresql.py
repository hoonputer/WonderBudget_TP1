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

    # csv 파일 속 데이터 옮기기
    with open ('WonderBudget/data/csv/hotel.csv', 'r') as h_file :
        h_reader = csv.DictReader(h_file)
        for data in h_reader:
            cur.execute("INSERT INTO hotel(Hotel_name, Date, Price, Client, Rating, Grade, Address, Day) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                        (data['Hotel_name'], data['Date'], data['Price'], data['Client'], data['Rating'], data['Grade'], data['Address'], data['Day']))
            
    conn.commit()

if __name__=='__main__':
    main()
