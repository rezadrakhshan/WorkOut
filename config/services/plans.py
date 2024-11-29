from db.models import Category
from fastapi import HTTPException


def create_category_service(category, db):
    new_category = Category(title=category.title)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return {"msg": "Category was create"}


def remove_category_service(category, db):
    category_object = db.query(Category).filter(Category.id == category.id).first()
    if category_object is None:
        raise HTTPException(status_code=404, detail="Category does not exists")
    db.delete(category_object)
    db.commit()
    return {"msg": "Category was deleted"}


def update_category_service(category, db):
    object = db.query(Category).filter(Category.id == category.id).first()
    if object is None:
        raise HTTPException(status_code=404, detail="Category does not exists")
    object.title = category.title
    db.commit()
    return {"msg": "Category Updated"}
