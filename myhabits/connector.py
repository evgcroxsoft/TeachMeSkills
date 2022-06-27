import os

class PostgreConnector():
    def __init__(self, POSTGRES_USER, POSTGRES_PW, POSTGRES_URL, POSTGRES_DB):
        self.POSTGRES_USER = POSTGRES_USER
        self.POSTGRES_PW = POSTGRES_PW
        self.POSTGRES_URL = POSTGRES_URL
        self.POSTGRES_DB = POSTGRES_DB

    def get_env_variable(name):
        env_var = os.environ.get(name)
        if not env_var:
            raise Exception(f'Expected environment variable {name} not set.')
        return env_var

    def path_to_PostgreSQL():
        '''Create path to POSGRESQL BD'''
        return f'postgresql+psycopg2://{credentials.POSTGRES_USER}:{credentials.POSTGRES_PW}@{credentials.POSTGRES_URL}/{credentials.POSTGRES_DB}'

credentials =  PostgreConnector(
    POSTGRES_USER= PostgreConnector.get_env_variable("POSTGRES_USER"),
    POSTGRES_PW= PostgreConnector.get_env_variable("POSTGRES_PW"),
    POSTGRES_URL= PostgreConnector.get_env_variable("POSTGRES_URL"),
    POSTGRES_DB= PostgreConnector.get_env_variable("POSTGRES_DB")
)
DB_path = PostgreConnector.path_to_PostgreSQL()
