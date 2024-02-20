import mysql.connector

def load_user_data(username):
    try:
        # Connect to the MySQL database
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password="asdfghjkl;'",
            database='rogue'
        )
        
        cursor = conn.cursor()

        # Execute a query to retrieve the row corresponding to the username
        cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
        user_data = cursor.fetchone()
        print(user_data)

        cursor.execute("SELECT * FROM maps")
        map_data = cursor.fetchone()
        data = map_data[4]
        data = data.replace("n", "\n")
        data = data.replace("a", "╔")
        data = data.replace("b", "║")
        data = data.replace("c", "╩")
        data = data.replace("d", "═")
        data = data.replace("e", "╚")
        data = data.replace("f", "∙")
        data = data.replace("t", "▒")
        data = data.replace("g", "╣")
        data = data.replace("h", "╠")
        data = data.replace("i", "╗")
        data = data.replace("j", "╝")
        data = data.replace("k", "╦")
        data = data.replace("o", " ")
        print(data)
        # Close the cursor and connection to the database
        cursor.close()
        conn.close()

        return user_data
    
    except mysql.connector.Error as e:
        print("Error connecting to MySQL:", e)
        return None

# Example usage:
# username = input("Enter your username: ")
# user_data = load_user_data(username)

