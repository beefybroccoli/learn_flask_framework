import os

class Config (object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "(Secret Phrase)"

    MONGODB_SETTINGS = {
        'db' : 'UTA_Enrollment',
        'host':'mongodb://localhost:27017/UTA_Enrollment'
    }