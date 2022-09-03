from flask import Blueprint, request, Response

from database.database_manager import DatabaseManager


loss_blup = Blueprint("loss",__name__)
@loss_blup.route('/',methods=['GET'])
def teste():
    return "Funciona!"

@loss_blup.route('/create',methods=['POST'])
def create():
    conn = DatabaseManager.connection
    if request.json.get("teste"):
        return "Funciona"
    else:
        return Response("É necessário informar o teste", 400)