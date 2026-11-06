from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.product import Product
from app.schemas.product import ProductCreate

def create_product(db: Session, data: ProductCreate) -> Product:
    product = Product(**data.model_dump())
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def list_products(db: Session) -> list[Product]:
    query = select(Product).where(Product.is_active == (True)).order_by(Product.id)
    return list(db.scalars(query).all())

def get_product(db: Session, product_id: int) -> Product | None:
    product = db.get(Product, product_id)
    if product is None or not product.is_active:
        return None
    return product

def update_product(db: Session, product: Product, data: dict) -> Product:
    for key, value in data.items():
        setattr(product, key, value)
        db.commit()
        db.refresh(product)
        return product
def deactivate_product(db: Session, product: Product) -> None:
    product.is_active = False
    db.commit()