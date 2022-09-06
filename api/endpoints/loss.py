from flask import Blueprint, Response
from api_models.loss_model import PostLossResponseBody
from controller.loss_controller import LossManager
from flask_pydantic import validate


loss_blup = Blueprint("loss",__name__)

@loss_blup.route('/clear',methods=['DELETE'])
@validate()
def clear_loss_table():
    LossManager.clear_table()
    return '',200

@loss_blup.route('/create',methods=['POST'])
@validate()
def create(body:PostLossResponseBody):
    resp,status = LossManager.new_loss(body.producer_name,
                         body.producer_email,
                         body.producer_cpf,
                         body.crop_local,
                         body.crop_type,
                         body.harvest_date,
                         body.event_type)
    return str(resp),status

@loss_blup.route('/edit/<id>',methods=['PUT'])
@validate()
def edit(id: int,body:PostLossResponseBody):
    resp,status = LossManager.edit_loss(id,
                         body.producer_name,
                         body.producer_email,
                         body.producer_CPF,
                         body.crop_local,
                         body.crop_type,
                         body.harvest_date,
                         body.event_type)
    return str(resp),status


@loss_blup.route('/delete/<id>',methods=['DELETE'])
@validate()
def delete(id):
    resp,status = LossManager.delete_loss(id)
    return str(resp),status



@loss_blup.route('/<cpf>',methods=['GET'])
@validate()
def list_by_cpf(cpf):
    loss = LossManager.list_loss_by_cpf(cpf)
    return loss

@loss_blup.route('/<cpf>',methods=['GET'])
@validate()
def get_loss(id):
    loss,status = LossManager.get_loss(id)
    return loss,status


@loss_blup.route('/',methods=['GET'])
@validate()
def list_all():
    loss = LossManager.list_loss()
    return loss