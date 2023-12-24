from typing import Optional
from pydantic import BaseModel
from datetime import datetime

# мне кажется, что можно возвращать всегда только id созданного объекта
class NewObjectId(BaseModel):
    id: int

# Регистрация
class UserCreate(BaseModel):
    email: str
    password: str
    name: Optional[str] = None
    language: Optional[str] = "en"

class UserReturnListForAdmin(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool
    
class UserReturnParamsForAdmin(BaseModel):
    id: int
    email: str
    is_email_verified: bool
    name: str
    about_me: Optional[str]
    is_active: bool
    is_superuser: bool
    image: Optional[str]
    last_language: str
    dt_registration: datetime
    progress_dt_start: Optional[datetime]
    progress_dt_update: Optional[datetime]
    hidden_admin_comment: Optional[str]
    
class UserReturnAboutMe(BaseModel):
    id: int
    email: str
    about_me: Optional[str]
    name: str
    image: Optional[str]
    dt_registration: datetime
    progress_dt_start: Optional[datetime]
    progress_dt_update: Optional[datetime]
    days_in_progress: int
    status_progress: str


class UserUpdateAboutMe(BaseModel):
    id: int
    email: Optional[str]
    name: Optional[str]
    about_me: Optional[str]
    image: Optional[str]
    language: Optional[str]