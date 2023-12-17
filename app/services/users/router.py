from fastapi import APIRouter, HTTPException, Depends
# Импортируйте здесь необходимые модули, например модели, схемы и функции CRUD
from services.users.shemas import *

router = APIRouter()

@router.get("/users")
async def get_users() -> list[ItemBaseSchema]:
    # Логика для получения элементов
    # Например: items = crud.get_items()
    items = [{"name": "Item 1"}, {"name": "Item 2"}]  # Пример данных
    return items

@router.post("/users")
async def create_user(item: ItemCreateSchema):
    # Логика для создания нового элемента
    # Например: new_item = crud.create_item(item)
    new_item = {"name": item.name}  # Пример создания элемента
    return new_item

@router.get("/users/{item_id}")
async def get_user(item_id: int) -> ItemBaseSchema:
    # Логика для получения одного элемента по ID
    # Например: item = crud.get_item(item_id)
    item = {"name": "Item", "id": item_id}  # Пример элемента
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.put("/users/{item_id}")
async def update_user(item_id: int, item: ItemUpdateSchema):
    # Логика для обновления элемента
    # Например: updated_item = crud.update_item(item_id, item)
    updated_item = {"name": item.name, "id": item_id}  # Пример обновленного элемента
    return updated_item

@router.delete("/users/{item_id}")
async def delete_user(item_id: int):
    # Логика для удаления элемента
    # Например: crud.delete_item(item_id)
    return {"detail": f"Item {item_id} deleted"}
