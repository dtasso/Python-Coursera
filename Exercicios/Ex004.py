valorseg = int(input('Por favor, entre com o número de segundos que deseja converter: '))
valordia = valorseg // 86400
valorhora_rest = valorseg % 86400
valorhora = valorhora_rest // 3600
valorseg_rest = valorhora_rest % 3600
valormin_rest = valorseg_rest // 60
valorseg_final =  valorseg_rest % 60

print(valordia,'dias,',valorhora,'horas,',valormin_rest,'minutos e',valorseg_final,'segundos.')