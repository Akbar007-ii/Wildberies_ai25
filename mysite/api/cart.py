from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from mysite.db.database import SessionLocal
from mysite.db.models import Cart
from mysite.db.schema import CartSchema
from typing import List

cart_router = APIRouter(prefix='/cart',tags=['Cart'])

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@cart_router.post('/create',response_model=CartSchema)
async def create_cart(cart_data: CartSchema, db: Session = Depends(get_db)):
    cart_db = Cart(**cart_data.dict())
    db.add(cart_db)
    db.commit()
    db.refresh(cart_db)
    return cart_db

@cart_router.get('list',response_model=List[CartSchema])
async def list_cart(db: Session = Depends(get_db)):
    cart_db = db.query(Cart).all()
    return cart_db

@cart_router.get('/detail',response_model=CartSchema)
async def detail_cart(cart_id: int, db: Session = Depends(get_db)):
    cart_db = db.query(Cart).filter(Cart.id == cart_id).first()
    if not cart_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Mynday cart jok')
    return cart_db

@cart_router.put('/update', response_model=CartSchema)
async def update_cart(cart_id:int, cart_data: CartSchema, db: Session = Depends(get_db)):
    cart_db = db.query(Cart).filter(Cart.id == cart_id).first()
    if not cart_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Mynday cart jok')
    cart_db.user_id == cart_data.user_id
    db.commit()
    db.refresh(cart_db)
    return cart_db

@cart_router.delete('/delete',response_model=dict)
async def delete_cart(cart_id: int, db: Session = Depends(get_db)):
    cart_db = db.query(Cart).filter(Cart.id == cart_id).first()
    if not cart_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Mynday cart jok')
    db.delete(cart_db)
    db.commit()
    return {'message': 'Success delete'}