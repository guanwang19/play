# try_sqlalchemy.py 
# basics for sqlalchemy
# Session, The Session is responsible for managing the unit of work and 
# tracking changes to the database.
import sqlite3
from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define a simple SQLAlchemy model
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    age = Column(Integer)

############################## use cursor
# Connect to an SQLite database (creates the database file if not exists)
conn = sqlite3.connect('my_database.db')

# Create a cursor object to execute SQL statements
cursor = conn.cursor()

# Execute SQL statement to create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER
    )
''')

# Commit the changes to the database
conn.commit()

# Insert data into the "users" table
cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('John Doe', 25))

# Commit the changes
conn.commit()

############################## use engine
# Create an SQLite in-memory database and bind the engine
engine = create_engine('sqlite:///my_database.db')

# Create a session factory
Session = sessionmaker(bind=engine)

# Create a session instance
session = Session()

# The Session is responsible for managing the unit of work and 
# tracking changes to the database.
# Adding objects to the session
new_user = User(name='John Doe')
session.add(new_user)

# Committing the transaction to persist changes to the database
session.commit()
