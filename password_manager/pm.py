from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os
import base64

def write_salt():
    salt = os.urandom(16)
    with open("salt.salt","wb") as k:
        k.write(salt)

## needs to run only once
if not os.path.exists("salt.salt"):
    write_salt()

def load_salt():
    file = open("salt.salt","rb")
    salt = file.read()
    file.close()
    return salt


# Ensuring that the same master password has to be entered while adding and viewing the passwords is not so straightforward as one might think
def generate_key_from_master_password(password: str) -> bytes:
    salt = load_salt()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=1_200_000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key

# def setup_auth_token():
#     token = fer.encrypt(b"auth")
#     with open("auth.token", "wb") as f:
#         f.write(token)
# if not os.path.exists("auth.token"):
#     setup_auth_token()


def view():
    with open("passwords.txt","r") as f:
        for line in f.readlines():
            data = line.rstrip()
            name , pssw = data.split("|")
            try:
                decrypted = fer.decrypt(pssw.encode()).decode()
                print(f"User: {name} | Password: {decrypted}")
            except Exception as e:
                print("Failed to decrypt. Possibly wrong master password")
                break
def add():
    account = input("Enter account name: ")
    psswd = input("Enter password: ")
    with open("passwords.txt",'a') as p:
        p.write(account + "|" + fer.encrypt(psswd.encode()).decode() + "\n")

# login into your password manager app only then you can view or add passwords in the storage else not. only once and then there should be a logout on quit() the app.  
def login():
    global fer
    master_pwd = input("What is the master password? ")
    try:
        key = generate_key_from_master_password(master_pwd) # encode converts the string to bytes. We are converting to bytes because key.key file contains byte format.
        fer = Fernet(key)

        if not os.path.exists("auth.token"):
            token = fer.encrypt(b"auth")
            with open("auth.token","wb") as f:
                f.write(token)
            print(" Auth token created. Login Successful.")
            return True

        # Try to decrypt the auth token 
        with open("auth.token", "rb") as f:
            token = f.read()
            decrypted = fer.decrypt(token).decode()
            if decrypted != "auth":
                raise ValueError("Invalid Token Content")
            print("Login Successful.")
            return True
    except Exception as e:
        print("Invalid Master Password!")
        return False
    
logged_in = False
if __name__ == "__main__":
    while True:
        if not logged_in:
            logged_in = login()
            continue

        mode = input("Would you like to add anew password, view existing ones. Enter q to logout and quit the app.")
        if mode == "q":
            print("Logged Out. GoodBye!")
            logged_in = False
            quit()
        elif mode == "view":
            view()
        elif mode == "add":
            add()
        else:
            print("Invalid Mode.")
