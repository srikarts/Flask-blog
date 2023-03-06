import os
class Config:
	SECRET_KEY = '5b02f7788cc40655'
	SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
	MAIL_SERVER = 'smtp-mail.outlook.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True 
	MAIL_USERNAME = os.environ.get('EMAIL_USER')
	MAIL_PASSWORD = os.environ.get('EMAIL_PASS')