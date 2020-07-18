from models.User import User
import bcrypt

class UserService():
    @staticmethod
    def insertUser(user):
        salt = b'$2b$12$ge7ZjwywBd5r5KG.tcznne'
        user['password'] = bcrypt.hashpw(user['password'].encode('utf-8'), salt)
        User.insert_one(user)

    @staticmethod
    def verifyUser(user):
        salt = b'$2b$12$ge7ZjwywBd5r5KG.tcznne'
        passwordHashed = bcrypt.hashpw(user['password'].encode('utf-8'), salt)
        userFound = User.find_one({'email': user['email']})
        if userFound != None:
            if passwordHashed == userFound['password'].split("'")[1].encode('utf-8'):
                return True
        return False