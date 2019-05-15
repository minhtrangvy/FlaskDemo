import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'fun-gaproject-no-need'
    MOVIE_DB_KEY = 'e8dde08f9b59d0ec23beda6b2b925cfc'
    ACCOUNT_SID = 'AC5959e59b79617a793b481397e6c26134'
    AUTH_TOKEN = os.environ.get('AUTH_TOKEN')
    print(AUTH_TOKEN)
