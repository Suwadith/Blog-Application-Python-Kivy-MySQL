import httpagentparser as httpagentparser
import mysql.connector
import geocoder

import StaticPages
import encryption

database = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="admin",
    database="blog"
)

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


def store_blog_post_with_file(title, body, visibility, username, file_path):
    title = encryption.encrypt_message(title)
    body = encryption.encrypt_message(body)
    sql = "INSERT into blog_posts (title, body, visibility, username, file_path) VALUES (%s, %s, %s, %s, %s)"
    val = (title, body, visibility, username, file_path)
    cursor.execute(sql, val)
    database.commit()
    if cursor.rowcount > 0:
        return True
    else:
        return False

# delete a specific post using blog_id
def delete_blog_post(blog_id):
    sql = "DELETE FROM blog_posts WHERE blog_id='" + str(blog_id) + "'"
    cursor.execute(sql)
    database.commit()

    if cursor.rowcount > 0:
        return True
    else:
        return False

# retrieve blog post using blog_id
def get_post_by_id(blog_id):
    sql = "SELECT * FROM blog_posts WHERE blog_id='" + str(blog_id) + "'"
    cursor.execute(sql)
    result = cursor.fetchone()
    return result

# fetch all the non-restricted posts
def get_public_blog_post():
    sql = "SELECT * FROM blog_posts WHERE visibility='public' ORDER BY `timestamp` DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    return results

# fetch all members-only restricted posts
def get_member_blog_post():
    sql = "SELECT * FROM blog_posts WHERE visibility='member' ORDER BY `timestamp` DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    return results

# fetch all posts made by a specific user
def get_user_blog_posts(username):
    sql = "SELECT * FROM blog_posts WHERE username='" + username + "' ORDER BY `timestamp` DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    return results

# edit/update a specific blog post
def update_post(title, body, blog_id):
    title = encryption.encrypt_message(title)
    body = encryption.encrypt_message(body)
    sql = "UPDATE blog_posts SET title='" + title + "', body='" + body + "' WHERE blog_id='" + str(blog_id) + "'"
    cursor.execute(sql)
    database.commit()

    if cursor.rowcount > 0:
        return True
    else:
        return False


# store activities into logs table
def store_to_log(activity):
    gc = geocoder.ip("me")
    http_user_agent = "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.9 (KHTML, like Gecko) \
                Chrome/5.0.307.11 Safari/532.9"

    ip_address = gc.ip
    location = gc.city
    device = str(httpagentparser.simple_detect(http_user_agent))
    username = StaticPages.username if StaticPages.username != '' else "Guest"

    sql = "INSERT into logs (activity, username, ip_address, location, device) VALUES (%s, %s, %s, %s, %s)"
    val = (activity, username, ip_address, location, device)
    cursor.execute(sql, val)
    database.commit()
    if cursor.rowcount > 0:
        return True
    else:
        return False


# fetch all logs
def retrieve_logs():
    sql = "SELECT * FROM logs ORDER BY `timestamp` DESC"
    cursor.execute(sql)
    results = cursor.fetchall()
    return results



# store_to_log('a','b','c')

# print(StaticPages.username if StaticPages.username != '' else "Guest")
# print(check_username("admin"))
# register_user("Suwadith", "wdp3YttyyX/LSQ==*vrQ7f2+vY6pWnj8+h1RRmA==*Bx+z56v6FL+BZD5SVZcU0g==*5GKS7GBWeTkrZbLisz7UZg==", "user")
# store_public_chat("Suwadith", "chat storage check 2")

# print(check_password("admin", "Admin$123")) admin
# print(check_password("charles", "Charles$123")) user


