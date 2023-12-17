from pydantic import BaseModel

class ItemBaseSchema(BaseModel):
    name: str
    description: str = None  # Опциональное поле

class ItemCreateSchema(ItemBaseSchema):
    # Здесь можно добавить поля, специфичные только для создания элемента
    pass

class ItemUpdateSchema(ItemBaseSchema):
    # Здесь можно добавить поля, специфичные только для обновления элемента
    pass

class User(BaseModel):
    id: int
    email: str
    is_email_verified: bool
    name: str
    password: str
    is_active: bool
    is_superuser: bool
    about_me: str
    image: str
    last_language: str
    dt_registration: str
    progress_dt_start: str
    progress_dt_update: str
    hidden_admin_comment: str