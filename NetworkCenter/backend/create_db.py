from app.routes.models import db, User
from app import app

db.create_all(app=app)
