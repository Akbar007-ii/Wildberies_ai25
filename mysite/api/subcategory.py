from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from mysite.db.database import SessionLocal
from mysite.db.models import SubCategory
from mysite.db.schema import SubCategorySchema
from typing import List


subcategory_router = APIRouter(prefix='/subcategory',tags=['SubCategory'])

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@subcategory_router.post('/create',response_model= SubCategorySchema)
async def create_subcategory(subcategory_data: SubCategorySchema, db: Session = Depends(get_db)):
    subcategory_db = SubCategory(**subcategory_data.dict())
    db.add(subcategory_db)
    db.commit()
    db.refresh(subcategory_db)
    return subcategory_db

@subcategory_router.get('/list',response_model=List[SubCategorySchema])
async def get_subcategory(db: Session = Depends(get_db)):
    subcategory_db = db.query(SubCategory).all()
    return subcategory_db

@subcategory_router.get('/detail',response_model=SubCategorySchema)
async def subcategory_detail(subcategory_id: int, db: Session = Depends(get_db)):
    subcategory_db = db.query(SubCategory).filter(SubCategory.id == subcategory_id).first()
    if not subcategory_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Mynday subcategory jok')
    return subcategory_db

@subcategory_router.put('/update', response_model= SubCategorySchema)
async def subcategory_update(subcategory_id: int, subcategory_data: SubCategorySchema,db: Session = Depends(get_db)):
    subcategory_db = db.query(SubCategory).filter(SubCategory.id == subcategory_id).first()
    if not subcategory_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Mynday subcategory jok')
    subcategory_db.subcategory_name == subcategory_data.subcategory_name
    db.commit()
    db.refresh(subcategory_db)
    return subcategory_db

@subcategory_router.delete('/delete',response_model= dict)
async def subcategory_delete(subcategory_id: int, db: Session = Depends(get_db)):
    subcategory_db = db.query(SubCategory).filter(SubCategory.id == subcategory_id).first()
    if not subcategory_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Mynday subcategory jok')
    db.delete(subcategory_db)
    db.commit()
    return {'message': 'Success delete'}





