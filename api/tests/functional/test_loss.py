import json
from time import sleep

def test_clear_table(test_client):
    response = test_client.delete('loss/clear')
    assert response.status_code == 200

# Cria perda
def test_create_patient_1(test_client):
    body = {
        "producer_name":"Silvana Mariah",
        "producer_email":"vinicius_andre_aragao@predialnet.com.br",
        "producer_cpf":"60339999837",
        "crop_local":"-71.5938,-109.0872",
        "crop_type":"MILHO",
        "harvest_date":"2022-09-05T00:00:00",
        "event_type":"GEADA"
    }

    body_json = json.dumps(body)
    response = test_client.post('loss/create',json=body)

    assert response.status_code == 201
    assert response.data != None

# Verifica se existe no banco
def test_get_patient_1(test_client):
    response = test_client.get('loss/1')

    assert response.status_code == 200

# Cria com email inválido
def test_create_patient_2(test_client):
    body = {
        "producer_name":"Márcia Helena Sandra Ramos",
        "producer_email":"aaaaaaaaaaaaa",
        "producer_cpf":"97565567493",
        "crop_local":"-12.6313, 8.0031",
        "crop_type":"MILHO",
        "harvest_date":"2020-19-05T00:00:00",
        "event_type":"GEADA"
    }
    response = test_client.post('loss/create',json=body)
    assert response.status_code == 400

# Cria com cpf inválido
def test_create_patient_3(test_client):
    body = {
        "producer_name":"Márcia Helena Sandra Ramos",
        "producer_email":"marcia_helena_ramos@dc4.com.br",
        "producer_cpf":"9756556749345454",
        "crop_local":"-12.6313, 8.0031",
        "crop_type":"MILHO",
        "harvest_date":"2020-19-05T00:00:00",
        "event_type":"GEADA"
    }
    response = test_client.post('loss/create',json=body)
    assert response.status_code == 400

#Cria outra perda
def test_create_patient_4(test_client):
    body = {
        "producer_name":"Márcia Helena Sandra Ramos",
        "producer_email":"marcia_helena_ramos@dc4.com.br",
        "producer_cpf":"97565567493",
        "crop_local":"-12.6313, 8.0031",
        "crop_type":"MILHO",
        "harvest_date":"2020-19-05T00:00:00",
        "event_type":"GEADA"
    }
    response = test_client.post('loss/create',json=body)
    assert response.status_code == 201

# Cria perda com data e localização semelhantes a um registro que existe no banco
def test_create_patient_4(test_client):
    body = {
        "producer_name":"Francisca Nina Ayla da Rocha",
        "producer_email":"marcia_helena_ramos@dc4.com.br",
        "producer_cpf":"02636011021",
        "crop_local":"-12.6313, 8.0031",
        "crop_type":"MILHO",
        "harvest_date":"2020-19-05T00:00:00",
        "event_type":"GEADA"
    }
    response = test_client.post('loss/create',json=body)
    assert response.status_code == 400

# Procura por uma perda que não existe no banco
def test_get_patient_1(test_client):
    response = test_client.get('loss/9999')

    assert response.status_code == 200


# Lista perdas
# Lista perdas por CPF
# Lista perdas com CPF inexistente

# Deleta primeira perda
# Lista perdas e verifica se apenas uma é retornada

# def test_home_page_with_fixture_2(test_client):
#     """
#     GIVEN a Flask application configured for testing
#     WHEN the '/' page is requested (GET)
#     THEN check that the response is valid
#     """
#     body = {
#         "producer_name":"Silvana Mariah",
#         "producer_email":"vinicius_andre_aragao@predialnet.com.br",
#         "producer_cpf":"60339999837",
#         "crop_local":"-71.5938,-109.0872",
#         "crop_type":"MILHO",
#         "harvest_date":"2022-09-05T00:00:00",
#         "event_type":"GEADA"
#     }
#     response = test_client.post('/create',json = json.dumps(body))
#     assert response.status_code == 200
# Cria perda
# Verifica se existe no banco
# Cria com cpf inválido
# Cria com email inválido
# Cria outra perda
# Verifica se existe no banco
# Cria perda com data e localização semelhantes a um registro que existe no banco


