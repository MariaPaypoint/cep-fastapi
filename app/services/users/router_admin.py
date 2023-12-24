from fastapi import APIRouter, HTTPException, Depends
from services.users.shemas import *
from database import db

router = APIRouter()

# список пользователей (для админов)

@router.get("/")
async def get_users_list() -> list[UserReturnListForAdmin]:
    # Например: items = crud.get_items()
    query = '''
        SELECT * 
        FROM users 
        WHERE 1
    '''
    values = {}
    try:
        result = await db.fetch_all(query=query, values=values)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to fetch users from database")
    
    #return UserReturnParamsForAdmin(**result)
    return result

# подробности о пользователе (для админа)

@router.get("/{user_id}")
async def get_user_info(user_id: int) -> UserReturnParamsForAdmin:
    ## надо подставить выборку только поля модели? (надеюсь, поля не будут называться иначе)
    query = '''
        SELECT * 
        FROM users 
        WHERE id = :user_id
    '''
    values = {"user_id": user_id}
    try:
        result = await db.fetch_one(query=query, values=values)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to fetch user from database")
    if not result:
        raise HTTPException(status_code=404, detail="User not found")
    
    #return UserReturnParamsForAdmin(**result)
    return result
        
@router.put("/{item_id}")
async def update_user(item_id: int, item: UserUpdateAboutMe):
    # Логика для обновления элемента
    # Например: updated_item = crud.update_item(item_id, item)
    updated_item = {"name": item.name, "id": item_id}  # Пример обновленного элемента
    return updated_item

@router.delete("/{item_id}")
async def delete_user(item_id: int):
    # Логика для удаления элемента
    # Например: crud.delete_item(item_id)
    return {"detail": f"Item {item_id} deleted"}
