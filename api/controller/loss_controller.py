from data_access.loss_DA import DALoss


class LossManager():
    def new_loss(producer_name, producer_email, producer_CPF, crop_local, crop_type, harvest_date, event_type):
        product = DALoss.new_loss(producer_name, producer_email, producer_CPF, crop_local, crop_type, harvest_date, event_type)


    def edit_loss(id,producer_name, producer_email, producer_CPF, crop_local, crop_type, harvest_date, event_type):
        product = DALoss.edit_loss(id,producer_name, producer_email, producer_CPF, crop_local, crop_type, harvest_date, event_type)


    def delete_loss(id):
        product = DALoss.delete_loss(id)

    def list_loss():
        DALoss.list_loss()

    def list_loss_by_cpf(cpf):
        DALoss.list_loss_by_cpf(cpf)