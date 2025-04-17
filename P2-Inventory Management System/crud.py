from models import Product
from database import db
from bson import ObjectId

product_collection = db["products"]

def product_helper(product) -> dict:
    return {
        "id": str(product["_id"]),
        "name": product["name"],
        "description": product.get("description"),
        "price": product["price"],
        "in_stock": product["in_stock"]
    }

async def add_product(product: Product):
    result = await product_collection.insert_one(product.dict())
    return await product_collection.find_one({"_id": result.inserted_id})

async def get_products():
    products = []
    async for product in product_collection.find():
        products.append(product_helper(product))
    return products

async def get_product(id: str):
    product = await product_collection.find_one({"_id": ObjectId(id)})
    if product:
        return product_helper(product)

async def update_product(id: str, product_data: dict):
    await product_collection.update_one({"_id": ObjectId(id)}, {"$set": product_data})
    return await get_product(id)

async def delete_product(id: str):
    return await product_collection.delete_one({"_id": ObjectId(id)})
