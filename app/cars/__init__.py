from flask import Blueprint

cars = Blueprint('cars', __name__)

from . import carsView