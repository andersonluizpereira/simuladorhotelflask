import sqlite3

connection = sqlite3.connect('banco.db')
cursor = connection.cursor()

cria_tabela = "CREATE TABLE IF NOT EXISTS Hoteis (hotel_id Text PRIMARY KEY, nome text, estrelas real, diaria real, cidade text)"

#cria_hotel = "insert into hoteis values ('alpha','Alpha Hotel',4.3,345.30,'Rio de Janeiro')"
#cria_hotel = "insert into hoteis values ('bravo','bravo Hotel',3.3,200,'São Paulo')"
cria_hotel = "insert into hoteis values ('charlie','Charlie Hotel',2,100,'Porto Alegre')"

cursor.execute(cria_hotel)

connection.commit()
connection.close()