import pymysql.cursors
import random

# Oppretter en tilkobling til databasen
connection = pymysql.connect(host='172.20.128.84', 
                            user='Daniel',         
                            password='123Akademiet',  
                            database='Users',     
                            charset='utf8mb4',      
                            cursorclass=pymysql.cursors.DictCursor)

def generate_unique_number():
    # Genererer et unikt 10-sifret tall
    while True:
        random_number = random.randint(1000000000, 9999999999)  
        if not check_duplicate(random_number):
            return random_number

def check_duplicate(number):
    # Sjekker om tallet allerede eksisterer i databasen
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) AS count FROM Brukere WHERE BrukerID = %s", (number))
        result = cursor.fetchone()
        if result['count'] > 0:
            return True
        else:
            return False

def insert_user(username, bruker_id, passord):
    # Setter inn brukernavn, brukerID og passord i databasen
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO Brukere (Navn, BrukerID, Passord) VALUES (%s, %s, %s)", (username, bruker_id, passord))
    connection.commit()
    