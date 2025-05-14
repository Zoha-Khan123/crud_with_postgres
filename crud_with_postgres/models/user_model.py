from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(100), nullable=False)                   # Full name
    email = Column(String(100), unique=True, nullable=False)     # Unique Email
    role = Column(String(50), nullable=False)                   # Role (trustee, admin, etc.)
    skills = Column(String(100), nullable=False)                # Skills (like "Developer")
    course = Column(String(50), nullable=False)                  # Course (like "english")
    gender = Column(String(10), nullable=False)                  # Gender (Male/Female)
    date_of_birth = Column(String(25), nullable=False)           # Date of Birth
    phone_no = Column(String(15), nullable=False)                # Phone Number
    address = Column(Text, nullable=False)                        # Address
    qualification = Column(String(50), nullable=False)           # Qualification (Bachelor, PhD, etc.)
    cnic = Column(String(20), unique=True, nullable=False)       # Unique CNIC
    password = Column(String(100), nullable=True)                 # Password
