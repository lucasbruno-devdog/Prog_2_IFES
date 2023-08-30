def alarme_despertador(hora_atual, minuto_atual, hora_alarme, minuto_alarme):
    minutos_restantes = 0
    
    tempo_1 = (hora_atual*60) + minuto_atual
    tempo_2 = (hora_alarme*60) + minuto_alarme
    
    if (tempo_1 < tempo_2):
        minutos_restantes = tempo_2 - tempo_1
    elif(hora_atual == hora_alarme ):
        minutos_restantes = (24*60) + (tempo_2 - tempo_1)
    else:
        minutos_restantes = (24*60) + (tempo_2 - tempo_1)
        
        
    return print(minutos_restantes)
        
def main():
    hora_atual = int(input())
    minuto_atual = int(input())
    hora_alarme = int(input())
    minuto_alarme = int(input())
    
    alarme_despertador(hora_atual, minuto_atual, hora_alarme, minuto_alarme)
    
    return 0
if __name__ == "__main__":
  main()        
               
    