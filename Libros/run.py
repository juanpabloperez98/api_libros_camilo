# run.py
from app import app,db

if __name__ == '__main__':
    # Crea las tablas en la base de datos antes de iniciar la aplicación
    with app.app_context():
        db.create_all()
    app.run(debug=True)