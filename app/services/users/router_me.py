from fastapi import APIRouter, HTTPException, Depends
from services.users.shemas import *
from database import db

router = APIRouter()


# регистрация

@router.post("/", response_model=NewObjectId)
async def self_registration(user: UserCreate):
    query = '''
        INSERT INTO users 
        SET 
            email              = :email,
            password           = :password,
            name               = :name, 
            last_language      = :language,

            is_email_verified  = 0,
            is_active          = 1,
            is_superuser       = 0,
            dt_registration    = NOW(),
            progress_dt_start  = NULL, 
            progress_dt_update = NULL
    '''
    values = {
        "email": user.email,
        "password": user.password,
        "name": user.name, 
        "language": user.language,
    }
    try:
        user_id = await db.execute(query=query, values=values)
        #return {**user.dict(), "id": user_id} # Вообще-то тут еще много полей должно вернуться. Селектить их что ли?
        return {"id": user_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to create user")

    
@router.get("/")
async def get_my_profile() -> UserReturnAboutMe:
    query = '''
        SELECT 
            *,
            IF( 
                progress_dt_start IS NULL OR progress_dt_update IS NULL, 
                0, 
                DATE(progress_dt_update) - DATE(progress_dt_start) + 1
            ) AS days_in_progress,
            CASE
                WHEN DATE(progress_dt_update) >= CURDATE() THEN 'active_with_today'
                WHEN DATE(progress_dt_update) =  SUBDATE(CURDATE(), 1) THEN 'active_without_today'
                ELSE 'expired'
            END AS status_progress
        FROM users 
        WHERE id = :user_id
    '''
    values = {"user_id": 1} ##

    try:
        result = await db.fetch_one(query=query, values=values)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to fetch user from database")
    if result:
        #return UserReturnAboutMe(username=result["username"], email=result["email"])
        #return UserReturnAboutMe(**result)
        return result 
    else:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Логика для получения одного элемента по ID
    # Например: item = crud.get_item(item_id)
    #item = {"name": "Item", "id": item_id}  # Пример элемента
    #if item is None:
    #    raise HTTPException(status_code=404, detail="Item not found")
    #return item

@router.put("/")
async def update_my_profile(item_id: int, item: UserUpdateAboutMe):
    # Логика для обновления элемента
    # Например: updated_item = crud.update_item(item_id, item)
    updated_item = {"name": item.name, "id": item_id}  # Пример обновленного элемента
    return updated_item

    query = """
        UPDATE users 
        SET username = :username, email = :email WHERE id = :user_id
    """
    values = {"user_id": user_id, "username": user.username, "email": user.email}
    try:
        await database.execute(query=query, values=values)
        return {**user.dict(), "id": user_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to update user in database")