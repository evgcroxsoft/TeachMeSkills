import os

class Connector():
    # __instance = None
    # def __new__(cls):
    #     '''Make Class Connector Singletone - for only one object creation'''
    #     if cls.__instance is None:
    #         cls.__instance = super(Connector,cls).__new__(cls)
    #     return cls.__instance

    def __init__(self, POSTGRES_USER, POSTGRES_PW, POSTGRES_URL, POSTGRES_DB):
        self.POSTGRES_USER = POSTGRES_USER
        self.POSTGRES_PW = POSTGRES_PW
        self.POSTGRES_URL = POSTGRES_URL
        self.POSTGRES_DB = POSTGRES_DB

    def get_env_variable(name):
        '''Give message if some of value couln't downloaded'''
        try:
            return os.environ[name]
        except KeyError:
            message = f"Expected environment variable {name} not set."
        raise Exception(message)

    def path_to_PostgreSQL():
        '''Create path to POSGRESQL BD'''
        return f'postgresql+psycopg2://{credentials.POSTGRES_USER}:{credentials.POSTGRES_PW}@{credentials.POSTGRES_URL}/{credentials.POSTGRES_DB}'

URL = Connector.get_env_variable("POSTGRES_URL")
USER = Connector.get_env_variable("POSTGRES_USER")
PW = Connector.get_env_variable("POSTGRES_PW")
DB = Connector.get_env_variable("POSTGRES_DB")

credentials = Connector(USER, PW, URL, DB)
DB_path = Connector.path_to_PostgreSQL()
