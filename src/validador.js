function validar_email(email){
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}
  
function validar_cep(cep){
  return /^[0-9]{8}$/.test(cep);
}


function validar_cpf(cpf){
  return /^\d{3}\.\d{3}\.\d{3}-\d{2}$/.test(cpf);
}

function validar_telefone(telefone){
  /^\(\d{2}\)\s?\d{4,5}-?\d{4}$/.test(telefone);
}
