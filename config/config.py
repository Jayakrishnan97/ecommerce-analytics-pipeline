import os
from dotenv import load_dotenv

load_dotenv()
#SQL
DB_CONFIG = {
    "host":os.getenv("DB_HOST"),
    "port":int(os.getenv("DB_PORT", 5432)),
    "user": os.getenv("DB_USER"),
    "db_name":os.getenv("DB_NAME"),
    "password":os.getenv("DB_PASSWORD"),
}
#SAFETY CHECK

missing = [k for k,v in DB_CONFIG.items()if not v]

if missing:
    raise ValueError(F"missing: {missing}")
