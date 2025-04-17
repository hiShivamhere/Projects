from fastapi import FastAPI, HTTPException
from crud import add_product, get_products, get_product, update_product, delete_product
from models import Product

app = FastAPI()

@app.post("/products")
async def create_product(product: Product):
    new_product = await add_product(product)
    return new_product

@app.get("/products")
async def read_products():
    return await get_products()

@app.get("/products/{id}")
async def read_product(id: str):
    product = await get_product(id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.put("/products/{id}")
async def update_product_api(id: str, product: Product):
    updated = await update_product(id, product.dict())
    return updated

@app.delete("/products/{id}")
async def delete_product_api(id: str):
    result = await delete_product(id)
    return {"deleted": result.deleted_count > 0}
