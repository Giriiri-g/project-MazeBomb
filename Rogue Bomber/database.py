import mysql.connector
import socket
from datetime import datetime

def load_user_data(username):
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password="qweasd",
            database='rogue'
        )
        
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
        user_data = cursor.fetchone()
        print(user_data)

        cursor.close()
        conn.close()

        return user_data
    
    except mysql.connector.Error as e:
        print("Error connecting to MySQL:", e)
        return None


def get_user_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print(ip_address)
    return ip_address

def insert_user_data(username, ip_address):
    try:
        if socket.inet_aton(ip_address):
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password="qweasd",
                database='rogue'
            )

            cursor = conn.cursor()
            login_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            cursor.execute("INSERT INTO users (username, IP_Address, login_time) VALUES (%s, %s, %s)", (username, ip_address, login_time))
            
            conn.commit()
            cursor.close()
            conn.close()

            print("User data inserted successfully!")
        else:
            print("Invalid IP address format:", ip_address)
    
    except mysql.connector.Error as e:
        print("Error inserting user data:", e)
        


def writeResults(hud_names, hud_values):
	conn = mysql.connector.connect(
			host='localhost',
			user='root',
			password="qweasd",
			database='rogue'
		)
	cursor = conn.cursor()
	cursor.execute("DELETE FROM game_stats")
	for i in range(4):
		cursor.execute("INSERT INTO game_stats VALUES(%s, %s, %s, %s)", (hud_names[i], len(hud_values[i][0]), hud_values[i][1], hud_values[i][2]))
	conn.commit()
	cursor.close()
	conn.close()
        
# Example usage:
# username = input("Enter your username: ")
# ip_address = get_user_ip()
# insert_user_data(username, ip_address)
