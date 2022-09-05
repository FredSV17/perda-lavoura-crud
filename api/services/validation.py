import re
from geopy import distance
from flask import Response
class Validation():
    def validate_cpf(cpf):
        # Verifica a formatação do CPF
        if not len(cpf) == 11:
            return False

        # Obtém apenas os números do CPF, ignorando pontuações
        numbers = [int(digit) for digit in cpf if digit.isdigit()]
    
        # Verifica se o CPF possui 11 números ou se todos são iguais:
        if len(numbers) != 11 or len(set(numbers)) == 1:
            return False
    
        # Validação do primeiro dígito verificador:
        sum_of_products = sum(a*b for a, b in zip(numbers[0:9], range(10, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[9] != expected_digit:
            return False
    
        # Validação do segundo dígito verificador:
        sum_of_products = sum(a*b for a, b in zip(numbers[0:10], range(11, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[10] != expected_digit:
            return False
    
        return True

    def validate_email(cpf):
        pattern = "[^@]+@[^@]+\.[^@]+"
        if re.match(pattern,cpf):
            return True
        else:
            return False

    def validate(cpf, email):
        if not Validation.validate_cpf(cpf):
            return "CPF inválido"
        if not Validation.validate_email(email):
            return "Email inválido"

    def check_if_similar(local,events):
        local_regex = re.match('(.*),(.*)',local)
        local_tuple = (local_regex.group(1),local_regex.group(2))
        for event in events:
            event_regex = re.match('(.*),(.*)',event[4])
            event_tuple = (event_regex.group(1),event_regex.group(2))
            distance_km = distance.distance(local_tuple,event_tuple).km
            if distance_km < 10:
                return True
        return False


