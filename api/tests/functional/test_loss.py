import json



def test_clear_table_bf(test_client):
    response = test_client.delete('loss/clear')
    assert response.status_code == 200

# Cria perda
def test_create_loss_1(test_client):
    global LOSS_1_ID
    body = {
        "producer_name":"Silvana Mariah",
        "producer_email":"teste@teste.com.br",
        "producer_cpf":"60339999837",
        "crop_local":"-71.5938,-109.0872",
        "crop_type":"MILHO",
        "harvest_date":"2022-09-05T00:00:00",
        "event_type":"GEADA"
    }

    response = test_client.post('loss/create',json=body)
    assert response.status_code == 201
    LOSS_1_ID = int(response.data)
    assert LOSS_1_ID > 0

# def test_create_loss_4(test_client):

# Verifica se existe no banco
def test_get_loss_1(test_client):
    response = test_client.get(f'loss/{LOSS_1_ID}')

    assert response.status_code == 200
    data = json.loads(response.data.decode('utf-8'))
    assert data.get("producer_name") == "Silvana Mariah"
    assert data.get("producer_email") == "teste@teste.com.br"
    assert data.get("producer_cpf") == "60339999837"
    assert data.get("crop_local") == "-71.5938,-109.0872"
    assert data.get("crop_type") == "MILHO"
    assert data.get("harvest_date") == "2022-09-05T00:00:00"
    assert data.get("event_type") == "GEADA"


# Edita primeira entrada
def test_edit_loss(test_client):
    body = {
        "producer_name":"Silvana Mariah Lemos",
        "producer_email":"teste@teste.com.br",
        "producer_cpf":"60339999837",
        "crop_local":"-71.5938,-109.0872",
        "crop_type":"MILHO",
        "harvest_date":"2022-09-05T00:00:00",
        "event_type":"GEADA"
    }
    response = test_client.put(f'loss/edit/{LOSS_1_ID}',json=body)
    assert response.status_code == 200

# Verifica se foi alterado
def test_get_loss_3(test_client):
    response = test_client.get(f'loss/{LOSS_1_ID}')

    assert response.status_code == 200
    data = json.loads(response.data.decode('utf-8'))
    assert data.get("producer_name") == "Silvana Mariah Lemos"
    assert data.get("producer_email") == "teste@teste.com.br"
    assert data.get("producer_cpf") == "60339999837"
    assert data.get("crop_local") == "-71.5938,-109.0872"
    assert data.get("crop_type") == "MILHO"
    assert data.get("harvest_date") == "2022-09-05T00:00:00"
    assert data.get("event_type") == "GEADA"

# Deleta primeira perda
def test_delete_entry(test_client):
    response = test_client.delete(f'loss/delete/{LOSS_1_ID}')
    assert response.status_code == 200

# Cria com email inválido
def test_create_loss_2(test_client):
    body = {
        "producer_name":"Márcia Helena Sandra Ramos",
        "producer_email":"aaaaaaaaaaaaa",
        "producer_cpf":"97565567493",
        "crop_local":"-12.6313, 8.0031",
        "crop_type":"MILHO",
        "harvest_date":"2020-09-15T00:00:00",
        "event_type":"GEADA"
    }
    response = test_client.post('loss/create',json=body)
    assert response.status_code == 400
    assert response.data.decode("utf-8") == "Email inválido"

# Cria com cpf inválido
def test_create_loss_3(test_client):
    body = {
        "producer_name":"Márcia Helena Sandra Ramos",
        "producer_email":"marcia_helena_ramos@dc4.com.br",
        "producer_cpf":"9756556749345454",
        "crop_local":"-12.6313, 8.0031",
        "crop_type":"MILHO",
        "harvest_date":"2020-09-15T00:00:00",
        "event_type":"GEADA"
    }
    response = test_client.post('loss/create',json=body)
    assert response.status_code == 400
    assert response.data.decode("utf-8") == "CPF inválido"

#Cria outra perda
def test_create_loss_4(test_client):
    body = {
        "producer_name":"Márcia Helena Sandra Ramos",
        "producer_email":"marcia_helena_ramos@dc4.com.br",
        "producer_cpf":"97565567493",
        "crop_local":"-12.6313, 8.0031",
        "crop_type":"MILHO",
        "harvest_date":"2020-09-15T00:00:00",
        "event_type":"GEADA"
    }
    response = test_client.post('loss/create',json=body)
    assert response.status_code == 201


# Procura por uma perda que não existe no banco
def test_get_loss_2(test_client):
    response = test_client.get('loss/9999')

    assert response.status_code == 400
    assert response.data.decode("utf-8") == "Perda não encontrada!"


# Lista perdas
def test_list_loss_1(test_client):
    response = test_client.get('loss')
    assert response.status_code == 200
    data = json.loads(response.data.decode('utf-8'))
    assert len(data) == 1
    item = data.get('entries')[0]
    assert item.get('producer_name') == "Márcia Helena Sandra Ramos"


# Lista perdas por CPF
def test_list_loss_by_cpf_1(test_client):
    response = test_client.get('loss/cpf/97565567493')
    assert response.status_code == 200
    data = json.loads(response.data.decode('utf-8'))
    assert len(data) == 1
    item = data.get('entries')[0]
    assert item.get('producer_name') == "Márcia Helena Sandra Ramos"

# Lista perdas com CPF inexistente
def test_list_loss_by_cpf_2(test_client):
    response = test_client.get('loss/cpf/0000')
    data = json.loads(response.data.decode('utf-8'))
    assert len(data.get('entries')) == 0
    assert response.status_code == 200


# Lista perdas e verifica se apenas uma é retornada
def test_list_loss_2(test_client):
    response = test_client.get('loss')
    assert response.status_code == 200
    data = json.loads(response.data.decode('utf-8'))
    assert len(data) == 1
    assert response.status_code == 200
    
def test_clear_table_aft(test_client):
    response = test_client.delete('loss/clear')
    assert response.status_code == 200
