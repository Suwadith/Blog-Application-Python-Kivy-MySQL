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
            return False
    else:
        return False


# storing public chat messages using encryption in the DB
def store_blog_post(title, body, visibility, username):
    title = encryption.encrypt_message(title)
    body = encryption.encrypt_message(body)
    sql = "INSERT into blog_posts (title, body, visibility, username) VALUES (%s, %s, %s, %s)"
    val = (title, body, visibility, username)
    cursor.execute(sql, val)
    database.commit()
    if cursor.rowcount > 0:
        return True
    else:
        return False

def delete_blog_post(blog_id):
    sql = "DELETE FROM blog_posts WHERE blog_id='"+str(blog_id)+"'"
    cursor.execute(sql)
    database.commit()

    if cursor.rowcount > 0:
        return True
    else:
        return False


def get_public_blog_post():
    sql = "SELECT * FROM blog_posts WHERE visibility='public' ORDER BY `timestamp` DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    return results

def get_member_blog_post():
    sql = "SELECT * FROM blog_posts WHERE visibility='member' ORDER BY `timestamp` DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    return results

def get_user_blog_posts(username):
    sql = "SELECT * FROM blog_posts WHERE username='"+username+"' ORDER BY `timestamp` DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    return results


# storing public chat messages using encryption in the DB
def store_to_log(username, message):
    print('Test')


# print(check_username("admin"))
# register_user("Suwadith", "wdp3YttyyX/LSQ==*vrQ7f2+vY6pWnj8+h1RRmA==*Bx+z56v6FL+BZD5SVZcU0g==*5GKS7GBWeTkrZbLisz7UZg==", "user")
# store_public_chat("Suwadith", "chat storage check 2")

# print(check_password("suwadith", "cricket")) admin
# print(check_password("charles", "Charles!123")) user
