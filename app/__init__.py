from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
import psycopg2
from flask_wtf.csrf import CSRFProtect



app = Flask(__name__)
app.config.from_object(Config)
csrf = CSRFProtect(app)
db = SQLAlchemy(app)
migrate =   Migrate(app,db)


load_dotenv()

conn = psycopg2.connect(
    host="localhost",
    database="labfinal",
    user=os.environ.get('DATABASE_USERNAME', 'postgres'),
    password= os.environ.get('DATABASE_PASSWORD')
)

cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS movies(
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    poster_url VARCHAR(255) NOT NULL,
    created_at TIMESTAMP NOT NULL
    );
""")

conn.commit()

cur.close()
conn.close()


from app import views