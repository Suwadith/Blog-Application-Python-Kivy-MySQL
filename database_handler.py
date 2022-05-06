import mysql.connector

import encryption

database = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="admin",
    database="blog"
)

# print(mydb)

cursor = database.cursor()


# check if username already registered
def check_username(username):
    sql = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(sql)
    result = cursor.fetchone()
    return result


# validates login password
def check_password(username, password):
    result = check_username(username)
    if result is None:
        return False
    else:
        if encryption.decrypt_password(result[2], password):
            return True
        else:
            return False


# register a new user
def register_user(username, password, user_type):
    if check_username(username) is None:
        password = encryption.encrypt_password(password)
        sql = "INSERT into users (username, password, user_type) VALUES (%s, %s, %s)"
        val = (username, password, user_type)
        cursor.execute(sql, val)
        database.commit()
        if cursor.rowcount > 0:
            return True
        else:
            print("something happened")
    else:
        return False


# storing public chat messages using encryption in the DB
def store_blog_post(title, body, file, visibility, username, user_id):
    title = encryption.encrypt_message(title)
    # sql = "INSERT into chat_history (username, message) VALUES (%s, %s)"
    # val = (username, message)
    # cursor.execute(sql, val)
    # database.commit()
    # if cursor.rowcount > 0:
    #     pass
    # else:
    #     print("Unable to store public chats")


def get_public_blog_post():
    sql = "SELECT * FROM blog_posts WHERE visibility='public'"
    cursor.execute(sql)
    results = cursor.fetchall()
    return results

def get_member_blog_post():
    sql = "SELECT * FROM blog_posts WHERE visibility='member'"
    cursor.execute(sql)
    results = cursor.fetchall()
    return results


# storing public chat messages using encryption in the DB
def store_to_log(username, message):
    print('Test')


# print(check_username("admin"))
# register_user("Suwadith", "wdp3YttyyX/LSQ==*vrQ7f2+vY6pWnj8+h1RRmA==*Bx+z56v6FL+BZD5SVZcU0g==*5GKS7GBWeTkrZbLisz7UZg==", "user")
# store_public_chat("Suwadith", "chat storage check 2")

# print(check_password("admin", "admin"))
