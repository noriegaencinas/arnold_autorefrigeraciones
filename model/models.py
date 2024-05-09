from main import app

from flask_login import UserMixin
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_sqlalchemy import SQLAlchemy


# CREATE DATABASE 
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB for sqlalchemy
class Users(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))

# CREATE TABLE IN DB 
with app.app_context():
    db.create_all()

# CREATE TABLE empleados_taller_mecanico (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     nombre_completo VARCHAR(100),
#     cargo VARCHAR(50),
#     fecha_contratacion DATE,
#     numero_empleado VARCHAR(20),
#     horario_trabajo VARCHAR(100),
#     numero_contacto VARCHAR(20),
#     correo_electronico VARCHAR(100),
#     salario DECIMAL(10,2)
# );