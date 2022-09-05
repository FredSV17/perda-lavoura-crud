from flask import Blueprint, request, Response
from api_models.loss_model import PostLossResponseBody
from controller.loss_controller import LossManager
from flask_pydantic import validate
from database.database_manager import DatabaseManager


loss_blup = Blueprint("loss",__name__)

@loss_blup.route('/create',methods=['POST'])
@validate
def create(loss:PostLossResponseBody):
    LossManager.new_loss(loss.producer_name,
                         loss.producer_email,
                         loss.producer_CPF,
                         loss.crop_local,
                         loss.crop_type,
                         loss.harvest_date,
                         loss.event_type)
    return 200
    # if request.json.get("teste"):
    #     return "Funciona"
    # else:
    #     return Response("É necessário informar o teste", 400)

@loss_blup.route('/edit/<id>',methods=['PUT'])
def edit(id: int,loss:PostLossResponseBody):
    data = request.json
    LossManager.edit_loss(id,
                         loss.producer_name,
                         loss.producer_email,
                         loss.producer_CPF,
                         loss.crop_local,
                         loss.crop_type,
                         loss.harvest_date,
                         loss.event_type)
    return 200


@loss_blup.route('/delete/<id>',methods=['DELETE'])
def delete(id):
    LossManager.delete_loss(id)
    return 200



@loss_blup.route('/<cpf>',methods=['GET'])
def list_by_cpf(cpf):
    LossManager.list_loss_by_cpf(cpf)

@loss_blup.route('/',methods=['GET'])
def list_all():
    LossManager.list_loss()