from fastapi import FastAPI, HTTPException, Depends
from auth import get_current_user, require_role
from users import router as user_router
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


app.include_router(user_router)

@app.get("/profile")
async def read_profile(current_user=Depends(get_current_user)):
    return {"user": current_user["email"]}

@app.get("/admin-only")
async def admin_dashboard(current_user=Depends(require_role(["admin"]))):
    return {"message": f"Welcome admin {current_user['email']}"}

@app.get("/edit-content")
async def edit_content(current_user=Depends(require_role(["admin", "editor"]))):
    return {"message": f"Welcome {current_user['role']}, you can edit content!"}

