# app/schemas.py
from pydantic import BaseModel, EmailStr, constr, conint

class User(BaseModel):
    user_id: int
    name: constr(min_length=2, max_length=50)
    email: EmailStr
    #Using pattern will create a pattern that starts with S (S) followed by seven digit number (\d{7})
    student_id: constr(pattern=r"^S\d{7}$")
    age: conint(gt=18)
