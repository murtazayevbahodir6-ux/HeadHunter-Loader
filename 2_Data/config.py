import environs

env = environs.Env()
env.read_env()

HOST = env.str("HOST", "localhost")
USER = env.str("DB_USER")
PASSWORD = env.str("PASSWORD")
DB = env.str("DB")

BASE_URL = "https://api.hh.ru/vacancies"
