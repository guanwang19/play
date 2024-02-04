from sqlalchemy import create_engine
import pprint
engine = create_engine('sqlite:///my_database.db')  # Replace with your database URL

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)


session = Session()

from try_sqlalchemy import User  # Assuming User is a SQLAlchemy model

# Query all users
users = session.query(User).all()

# Add a new user
new_user = User(name='John Doe', age=25)
session.add(new_user)

all_users = session.query(User).all()
for user in all_users:
    print(f"User ID: {user.id}, Name: {user.name}, Age: {user.age}")
#     pp= pprint.PrettyPrinter(indent=4)
#     pp.pprint(user)
# print(type(all_users))
# print(all_users)
# Commit the changes to the database
session.commit()

session.close()
