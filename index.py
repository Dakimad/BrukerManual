import pymysql.cursors

# Oppretter en tilkobling til databasen
connection = pymysql.connect(host='172.20.128.84', 
                            user='Daniel',         
                            password='123Akademiet',  
                            database='Users',     
                            charset='utf8mb4',      
                            cursorclass=pymysql.cursors.DictCursor)

def insert_user(username, bruker_id, passord):
    # Setter inn brukernavn, brukerID og passord i databasen
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO Brukere (Navn, BrukerID, Passord) VALUES (%s, %s, %s)", (username, bruker_id, passord))
    connection.commit()
 