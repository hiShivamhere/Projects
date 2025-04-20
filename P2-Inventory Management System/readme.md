# 🧰 FastAPI + MongoDB CRUD API

A simple, production-ready RESTful API using **FastAPI** and **MongoDB** (via async Motor driver) to manage product inventory.

---

## 🚀 Features

- Create, Read, Update, Delete products
- MongoDB async integration via `motor`
- Auto-generated Swagger UI docs
- Modular project structure
- Environment variable support using `.env`

---

## 📁 Project Structure

```
inventory_api/
├── auth.py             # JWT logic, user authentication
├── users.py            # Routes for login/register
├── models.py           # User model definition
├── crud.py             # User handling logic
├── main.py             # Entry point, includes auth routes
```

---

## 🛠️ Tech Stack

- **FastAPI**: Web framework
- **Motor**: Async MongoDB driver
- **Pydantic**: Data validation
- **Uvicorn**: ASGI server
- **Dotenv**: For managing secrets/configs

---

### 1. Clone the Repo

```bash
git clone https://github.com/hishivamhere/Projects.git
cd ./Projects/P2-Inventory Management System/
```

### 2. Install Dependencies

```bash

python -m venv venv
source venv/bin/activate        # or venv\\Scripts\\activate on Windows
pip install -r requirements.txt

```

### 3. Set up Environment Variables
Create a .env file:

```env

MONGODB_URL="mongodb://localhost:27017"
DATABASE_NAME="inventory_db"

```

### 4. Run the Server

``` bash

uvicorn main:app --reload

```

Visit: http://127.0.0.1:8000/docs for the UI



