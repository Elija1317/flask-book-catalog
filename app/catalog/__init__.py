# app/catalog/__init__
from flask import Blueprint

# Blue print is the class so create instance for this class Blueprint

main = Blueprint('main', __name__ ,template_folder = 'template')
from app.catalog import routes
