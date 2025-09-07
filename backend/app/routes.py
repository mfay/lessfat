from fastapi import APIRouter, Depends, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.db import SessionLocal, engine
from app.models import Base, Meal
from app.embeddings import get_embedding

Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/log-meal")
def log_meal_form(request: Request):
    flash = request.session.pop("flash", None)
    return templates.TemplateResponse("log_meal_form.html", {"request": request, "flash": flash})

@router.post("/add-meal")
def log_meal(request: Request, name:str = Form(...), calories: int = Form(...), db: Session = Depends(get_db)):
    embedding = get_embedding(name)
    meal = Meal(
        name=name,
        calories=calories,
        embedding=embedding
    )
    db.add(meal)
    db.commit()
    request.session["flash"] = "Meal logged successfully!"
    return RedirectResponse(url="/log-meal", status_code=303)
    

@router.get("/meals")
def list_meals(db: Session = Depends(get_db)):
    meals = db.query(Meal).all()
    return [{"name": m.name, "calories": m.calories} for m in meals]

