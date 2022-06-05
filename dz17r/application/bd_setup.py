import os

class Connector():
    default_env_list = ['POSTGRES_URL','POSTGRES_USER','POSTGRES_PW','POSTGRES_DB']
    def __init__(self, POSTGRES_URL, POSTGRES_USER, POSTGRES_PW, POSTGRES_DB):
        self.POSTGRES_URL = POSTGRES_URL
        self.POSTGRES_USER = POSTGRES_USER
        self.POSTGRES_PW = POSTGRES_PW
        self.POSTGRES_DB = POSTGRES_DB

    @staticmethod
    def get_env_variable():
        '''Give message if some of value couldn't downloaded'''
        try:  
            env_list = [os.environ[f'{value}'] for value in Connect_to_Postgres.default_env_list]
            return env_list
        except KeyError:
                message = f'Expected environment variable not set!'
        raise Exception(message)

    def path_to_PostgreSQL():
        '''Create path to POSGRESQL BD'''
        list = Connect_to_Postgres.get_env_variable()
        return f'postgresql+psycopg2://{list[1]}:{list[2]}@{list[0]}/{list[3]}'

    @classmethod
    def change_default_env_list(cls, url, user, password, database):
        '''Change default env database list'''
        list = [url, user, password, database]
        cls.default_env_list = list