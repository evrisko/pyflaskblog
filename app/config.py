class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:12345678@localhost/blog'
    SECRET_KEY = 'something very secret key'

# Flask security
    SECURITY_PASSWORD_SALT = 'slat'
    SECURITY_PASSWORD_HASH = 'bcrypt' #sha512_crypt
