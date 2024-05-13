import datetime
import time
import winsound

def set_alarm():
    print("Configuración de la alarma:")
    hour = int(input("Ingresa la hora (formato de 24 horas): "))
    minute = int(input("Ingresa los minutos: "))

    while True:
        now = datetime.datetime.now()
        current_hour = now.hour
        current_minute = now.minute

        if current_hour == hour and current_minute == minute:
            print("¡¡¡ALARMA!!!")
            winsound.PlaySound("path/to/alarm_sound.wav", winsound.SND_ASYNC)
            break

        time.sleep(1)

set_alarm()
