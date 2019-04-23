import os

class Config:

     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://tashanah:tash1234@localhost/watchlist'
     UPLOADED_PHOTOS_DEST = 'app/static/photos'
     # email configurations
     MAIL_SERVER = 'smtp.googlemail.com'
     MAIL_PORT = 587
     MAIL_USE_TLS = True
     MAIL_USERNAME = os.environ.get("MAIL_USERNAME")

class prodConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options ={
    'development':DevConfig,
    'production':prodConfig
}


MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")