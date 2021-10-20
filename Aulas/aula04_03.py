valorseg = int(input('Por favor, digite o número de segundos que deseja converter: '))
valordia = valorseg // 86400
valorhora_rest = valorseg % 86400
valorhora = valorhora_rest // 3600
valorseg_rest = valorhora_rest % 3600
valormin_rest = valorseg_rest // 60
valorseg_final =  valorseg_rest % 60

print('{} Dias, {} Horas, {} Minutos, {} segundos.'.format(valordia, valorhora, valormin_rest, valorseg_final))