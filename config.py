class BaseConfig(object):
    SQLALCHEMY_DATABASE_URI = (
        'mysql://ezarco00:'
        'database1'
        '@ezarco00.mysql.pythonanywhere-services.com/'
        'ezarco00$mysitedb')
    SQLALCHEMY_TRACK_MODIFICATIONS = False