from dotenv import load_dotenv
import os
from pathlib import Path


# Project root directory
BASE_DIR = Path(__file__).resolve().parents[2]

# Load .env from project root
load_dotenv(BASE_DIR / ".env")

 
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")