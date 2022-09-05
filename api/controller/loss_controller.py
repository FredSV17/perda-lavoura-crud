from flask import abort
from api_models.loss_model import GetLossResponseBody, ListLossResponseBody
from data_access.loss_DA import DALoss
from services.validation import Validation

class LossManager():
    def new_loss(producer_name, producer_email, producer_CPF, crop_local, crop_type, harvest_date, event_type):
        same_date_events = DALoss.list_by_date(harvest_date)
        if Validation.check_if_similar(crop_local,same_date_events):
            abort(400, {"message":"Eventos similares existem no sistema!"})
        else:
            error_msg = Validation.validate(producer_CPF,producer_email)
            if error_msg == None:
                DALoss.new_loss(producer_name, producer_email, producer_CPF, crop_local, crop_type, harvest_date, event_type)
            else:
                abort(400, {"message": error_msg})



    def edit_loss(id,producer_name, producer_email, producer_CPF, crop_local, crop_type, harvest_date, event_type):
        loss = LossManager.get_loss(id)
        if loss:
            same_date_events = DALoss.list_by_date(harvest_date)
            if Validation.check_if_similar(crop_local,same_date_events):
                abort(400, {"message":"Eventos similares existem no sistema!"})
            else:
                error_msg = Validation.validate(producer_CPF,producer_email)
                if error_msg == None:
                    DALoss.edit_loss(id,producer_name, producer_email, producer_CPF, crop_local, crop_type, harvest_date, event_type)
                else:
                    abort(400, {"message": error_msg})
        else:
            abort(400, {"message":"Perda não encontrada!"})

    def delete_loss(id):
        loss = LossManager.get_loss(id)
        if loss:
            DALoss.delete_loss(id)
        else:
            abort(400, {"message":"Perda não encontrada!"})

    def list_loss():
        loss = DALoss.list_loss()
        return ListLossResponseBody(entries=[LossManager._build_response(item) for item in loss])

    def list_loss_by_cpf(cpf):
        loss = DALoss.list_loss_by_cpf(cpf)
        return ListLossResponseBody(entries=[LossManager._build_response(item) for item in loss])

    def _build_response(data:tuple):
        return GetLossResponseBody(
            id = data[0],
            producer_name= data[1],
            producer_email= data[2],
            producer_cpf= data[3],
            crop_local= data[4],
            harvest_date= data[5],
            crop_type= data[6],
            event_type= data[7]
        )