from flask_scrypt import generate_random_salt, generate_password_hash, check_password_hash

def generate(userid, password):
    credentials = userid + password
    salt = generate_random_salt(64)
    salt = salt.decode('utf-8')
    hashed_credentials = generate_password_hash(credentials,salt)



    hashed_credentials = hashed_credentials.decode('utf-8')

    lines = [salt, hashed_credentials]
    with open("server_adm.txt", "w") as file:
        for line in lines:
            file.write(line)
            file.write('\n')
        file.close()


userid = input('UserID: ')
password = input('Password: ')

generate(userid,password)