import re
# Conjunto de REGEX para validação de entradas.

def validar_email(email):
  # escreva seu código aqui
  padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
  return re.match(padrao, email) is not None
  
def validar_cep(cep):
  # escreva seu código aqui
  cep = re.sub('[^0-9]', '', cep)
  if len(cep) != 8:
    return False
  return True
  
def validar_cpf(cpf):
  # escreva seu código aqui
  return bool(re.match(r'^\d{3}\.\d{3}\.\d{3}\-\d{2}$', cpf) and \
    not re.match(r'^(\d)\1{10}$', cpf.replace('.', '').replace('-', '')) and \
    sum([int(digit) * ((i % 9) + 2) for i, digit in enumerate(re.findall(r'\d', cpf)[0:9])]) % 11 == int(cpf[-2]) and \
    sum([int(digit) * ((i % 9) + 2) for i, digit in enumerate(re.findall(r'\d', cpf)[0:10])]) % 11 == int(cpf[-1]))
  
def validar_telefone(telefone):
  telefone = re.sub('[^0-9]', '', telefone)
  if len(telefone) < 10 or len(telefone) > 11:
    return False
  if len(telefone) == 11 and telefone[0] != '9':
    return False
  return True
  
 
  
