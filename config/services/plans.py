from db.models import Category
from schemas.plans import CreateCategory


def create_category_service(category, db):
    new_category = Category(title=category.title)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return {"msg": "Category was create"}
