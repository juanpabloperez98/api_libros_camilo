# app/routes.py
from flask import jsonify, request
from app import app, db
from app.models import Libro

# Endpoint para obtener todos los libros
@app.route('/libros', methods=['GET'])
def obtener_libros():
    libros = Libro.query.all()
    return jsonify({'libros': [libro.titulo for libro in libros]})

# Endpoint para obtener un libro por ID
@app.route('/libros/<int:libro_id>', methods=['GET'])
def obtener_libro(libro_id):
    libro = Libro.query.get(libro_id)
    if libro:
        return jsonify({'libro': libro.titulo})
    return jsonify({'mensaje': 'Libro no encontrado'}), 404

# Endpoint para agregar un nuevo libro
@app.route('/libros', methods=['POST'])
def agregar_libro():
    data = request.get_json()
    if 'titulo' in data:
        nuevo_libro = Libro(titulo=data['titulo'])
        db.session.add(nuevo_libro)
        db.session.commit()
        return jsonify({'mensaje': 'Libro agregado correctamente'})
    return jsonify({'mensaje': 'Falta el título del libro'}), 400

# Endpoint para actualizar un libro por ID
@app.route('/libros/<int:libro_id>', methods=['PUT'])
def actualizar_libro(libro_id):
    libro = Libro.query.get(libro_id)
    if libro:
        data = request.get_json()
        if 'titulo' in data:
            libro.titulo = data['titulo']
            db.session.commit()
            return jsonify({'mensaje': 'Libro actualizado correctamente'})
        return jsonify({'mensaje': 'Falta el título del libro'}), 400
    return jsonify({'mensaje': 'Libro no encontrado'}), 404

# Endpoint para eliminar un libro por ID
@app.route('/libros/<int:libro_id>', methods=['DELETE'])
def eliminar_libro(libro_id):
    libro = Libro.query.get(libro_id)
    if libro:
        db.session.delete(libro)
        db.session.commit()
        return jsonify({'mensaje': 'Libro eliminado correctamente'})
    return jsonify({'mensaje': 'Libro no encontrado'}), 404
