from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from mysite.db.database import SessionLocal
from mysite.db.models import FavoriteItem
from mysite.db.schema import FavoriteItemSchema
from typing import List

favorite_item_router = APIRouter(prefix='/favorite_item',tags=['Favorite_item'])

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@favorite_item_router.post('/create',response_model=FavoriteItemSchema)
async def create_favorite_item(favorite_item_data: FavoriteItemSchema,db: Session = Depends(get_db)):
    favorite_item_db = FavoriteItem(**favorite_item_data.dict())
    db.add(favorite_item_db)
    db.commit()
    db.refresh(favorite_item_db)
    return favorite_item_db

@favorite_item_router.get('/list',response_model=List[FavoriteItemSchema])
async def list_favorite_item(db: Session = Depends(get_db)):
    favorite_item_db = db.query(FavoriteItem).all()
    return favorite_item_db

@favorite_item_router.get('/detail', response_model= FavoriteItemSchema)
async def detail_favorite_item(favorite_item_id:int , db: Session = Depends(get_db)):
    favorite_item_db = db.query(FavoriteItem).filter(FavoriteItem.id == favorite_item_id).first()
    if not favorite_item_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Mynday item jok')
    return favorite_item_db

@favorite_item_router.put('/update',response_model= FavoriteItemSchema)
async def update_favorite_item(favorite_item_id: int, favorite_item_data: FavoriteItemSchema, db: Session = Depends(get_db)):
    favorite_item_db = db.query(FavoriteItem).filter(FavoriteItem.id == favorite_item_id)
    if not favorite_item_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Mynday item jok')
    favorite_item_db.product_id == favorite_item_data.product_id
    db.commit()
    db.refresh(favorite_item_db)
    return favorite_item_db

@favorite_item_router.delete('/delete',response_model=dict)
async def delete_favorite_item(favorite_item_id: int, db: Session = Depends(get_db)):
    favorite_item_db = db.query(FavoriteItem).filter(FavoriteItem.id == favorite_item_id).first()
    if not favorite_item_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Mynday item jok')
    db.delete(favorite_item_db)
    db.commit()
    return {'message': 'Success delete'}

