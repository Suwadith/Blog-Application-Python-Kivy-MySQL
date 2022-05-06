import cryptocode

# https://github.com/gdavid7/cryptocode/blob/main/cryptocode.py
# This library uses a form of AES encryption and decryption methodology

# encrypts password with a secret key
def encrypt_password(password):
    encrypted_password = cryptocode.encrypt(password, "secret_key")
    return encrypted_password


# compares encrypted password with the login password
def decrypt_password(encrypted_password, password):
    decrypted_password = cryptocode.decrypt(encrypted_password, "secret_key")
    if decrypted_password == password:
        return True
    else:
        return False


# encrypts chat messages using secret key
def encrypt_message(message):
    encrypted_message = cryptocode.encrypt(message, "secret_message")
    return encrypted_message



# print(encrypt_password("cricket"))
#
# print(decrypt_password("r43cKlA7*RRmYmaI2uN0TmNlwH+3htw==*Jt03qXXqYj5vPQHbENTOzw==*yaXFD4gZllcq3RE5SJ32KA==", "killme"))