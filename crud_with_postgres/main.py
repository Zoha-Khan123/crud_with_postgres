from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import SessionLocal
from models.user_model import User
from pydantic import BaseModel
from typing import List
from sqlalchemy.exc import IntegrityError 
from typing import Optional


app = FastAPI()

# Dependency for DB Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



# Pydantic Model For Validation
class UserCreate(BaseModel):
    name: str
    email: str
    role: str
    skills: str
    course: str
    gender: str
    date_of_birth: str
    phone_no: str
    address: str
    qualification: str
    cnic: str
    password: str                       


class UserResponse(UserCreate):
    id : int             # user create honay ka bad id assign ke jate ha
    class Config:
        orm_mode = True  # orm sql table ke rows ko python code ma convert kar data ha jis say hamay sql quries nahi likhne parhte hum python ka code likh saktay han



# Create a new Users
@app.post("/users", response_model=UserResponse)
def create_user(user:UserCreate, db:Session=Depends(get_db)):

    # Step 1: Pre-check if user already exists
    existing_user = db.query(User).filter( (User.email == user.email) | (User.cnic == user.cnic)).first()

    if existing_user:
        print(f"User with email: {user.email} or CNIC: {user.cnic} already exists.")
        raise HTTPException(status_code=400, detail="User with this email or CNIC already exists")
        
    # Step 2: Try to add new user to the database
    try:
        db_user = User(
            name = user.name ,
            email = user.email ,
            role = user.role,
            skills = user.skills,
            course = user.course,
            gender = user.gender,
            date_of_birth = user.date_of_birth,
            phone_no = user.phone_no,
            address = user.address,
            qualification = user.qualification,
            cnic = user.cnic,
            password = user.password,                       
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except IntegrityError as e:
        db.rollback() 
        print(f"Error: {e.orig}") 
        raise HTTPException(status_code=400, detail="Error: Duplicate email or CNIC constraint violation.")
        


# Get all Users
@app.get("/users", response_model=List[UserResponse])
def get_users(db:Session=Depends(get_db)):
    return db.query(User).all()



# Delete User
@app.delete("/users/{user_id}")
def delete_user(user_id:int, db:Session=Depends(get_db)):

    # Step 1: Find the user
    existing_user = db.query(User).filter(User.id == user_id).first()

     # Step 2: If not found, raise error
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")

    # Step 3: Delete user and commit
    try:
        db.delete(existing_user)
        db.commit()
        return {"message": f"User with ID {user_id} has been deleted successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Deletion failed: {str(e)}")



# Update an existing user

# Yaha pydantic ka dosr model is liya banaya ga ha ka agar user ko koi aik ya do fileds update karne hoto sirf wohe karay ga sub fields ko update karnay ke need nahi hoge

# Step 1: UserUpdate Pydantic model
class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    role: Optional[str] = None
    skills: Optional[str] = None
    course: Optional[str] = None
    gender: Optional[str] = None
    date_of_birth: Optional[str] = None
    phone_no: Optional[str] = None
    address: Optional[str] = None
    qualification: Optional[str] = None
    cnic: Optional[str] = None
    password: Optional[str] = None


@app.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.id == user_id).first()
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    try:
        # yaha sirf wohe fields update honge jo kay user update karna cahay bake wase he same rahange
        update_data = user.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(existing_user, key, value)

        db.commit()
        db.refresh(existing_user)
        return existing_user

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Update failed: {str(e)}")







