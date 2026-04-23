print("----UMAMUSUME: PYTHON DERBY!---")

Uma = None
Speed = None
Stamina = None
Power = None
Guts = None
Wit = None

predict_speed = None
predict_stamina = None
predict_power = None
predict_guts = None
predict_wit = None


Intro = True

while Intro:
    UmaSelect = input("\nElije tu Umamusume:\n1: Eishin Flash\n2: Twin Turbo\n3: Agnes Tachyon\n4: Gold City\n5: Matikanetannhauser\n")

    if UmaSelect == "1":
        Decide1 = input(str("\nEishin Flash | Meisterschaft\nSpeed: 122\nStamina: 101\nPower: 113\nGuts: 100\nWit: 114\nEstá seguro? Y/N\n"))
        if Decide1 == "y" or "Y":
            print("Has elegido a Eishin Flash!")
            Uma = "Eishin Flash"
            Speed = 122
            Stamina = 101
            Power = 113
            Guts = 100
            Wit = 114
            break
        elif Decide1 == "n" or "N":
            continue
        else:
            print("\nRespuesta no valida, intente de nuevo.")
    
    elif UmaSelect == "2":
        Decide2 = input(str("\nTwin Turbo | Blast Mode! Turbo Engine\nSpeed: 137\nStamina: 98\nPower: 107\nGuts: 119\nWit: 89\nEstá seguro? Y/N\n"))
        if Decide2 == "y" or "Y":
            print("Has elegido a Twin Turbo!")
            Uma = "Twin Turbo"
            Speed = 137
            Stamina = 98
            Power = 107
            Guts = 119
            Wit = 89
            break
        elif Decide2 == "n" or "N":
            continue
        else:
            print("\nRespuesta no valida, intente de nuevo.")

    elif UmaSelect == "3":
        Decide3 = input(str("\nAgnes Tachyon | Tach-nology\nSpeed: 112\nStamina: 104\nPower: 104\nGuts: 108\nWit: 122\nEstá seguro? Y/N\n"))
        if Decide3 == "y" or "Y":
            print("Has elegido a Agnes Tachyon!")
            Uma = "Agnes Tachyon"
            Speed = 112
            Stamina = 104
            Power = 104
            Guts = 108
            Wit = 122
            break
        elif Decide3 == "n" or "N":
            continue
        else:
            print("\nRespuesta no valida, intente de nuevo.")

    elif UmaSelect == "4":
        Decide4 = input(str("\nGold City | Authentic / 1928\nSpeed: 109\nStamina: 113\nPower: 114\nGuts: 112\nWit: 102\nEstá seguro? Y/N\n"))
        if Decide4 == "y" or "Y":
            print("Has elegido a Gold City!")
            Uma = "Gold City"
            Speed = 109
            Stamina = 113
            Power = 114
            Guts = 112
            Wit = 102
            break
        elif Decide4 == "n" or "N":
            continue
        else:
            print("\nRespuesta no valida, intente de nuevo.")

    elif UmaSelect == "5":
        Decide5 = input(str("\nMatikanetannhauser | Clippety-Tippety-Clop\nSpeed: 103\nStamina: 117\nPower: 106\nGuts: 114\nWit: 110\nEstá seguro? Y/N\n"))
        if Decide5 == "y" or "Y":
            print("Has elegido a Matikanetannhauser!")
            Uma = "Matikanetannhauser"
            Speed = 103
            Stamina = 117
            Power = 106
            Guts = 114
            Wit = 110
            break
        elif Decide5 == "n" or "N":
            continue
        else:
            print("\nRespuesta no valida, intente de nuevo.")
            
    else:
        print("\nNumero no valido, intente de nuevo.")




satsuki = 20
derby = 20
kikuka = 20
jcup = 20
arima = 20
victorias = 0
results = False

energia = 100
energia_max = 100
energia_min = 0

import random
import msvcrt
rest_events = ["Deprived", "Refreshed", "Well-Rested"]


print("\nTienes 100 turnos para entrenar a tu Umamusume para ganar la Triple Corona, el Japan Cup y el Arima Kinen!")

while satsuki > 0:
    print("\nTurnos restantes para el Satsuki Sho: " + str(satsuki))
    print("Energía restante: " + str(energia))
    action = input("\nQué harás?\n1: Entrenar\n2: Descansar\n3: Ver estadísticas\n")
    if action == "1":
        training = input("\nQué deberia entrenar?\n1: Speed\n2: Stamina\n3: Power\n4: Guts\n5: Wit\n")
        if training == "1":
            if random.random() < energia/100:
                print("\nSpeed aumentó en 15 puntos!\nPower aumentó en 6 puntos!\n")
                Speed += 15
                Power += 6
                energia = max(energia - 10, energia_min)
                satsuki -= 1
            else:
                print("\nTu Umamusume falló el entrenamiento.\nSpeed disminuyó en 5 puntos.\nPower disminuyó en 5 puntos.\n")
                Speed -= 5
                Power -= 5
                satsuki -= 1
        elif training == "2":
            if random.random() < energia/100:
                print("\nStamina aumentó en 10 puntos!\nGuts aumentó en 4 puntos!\n")
                Stamina += 10
                Guts += 4
                energia = max(energia - 12, energia_min)
                satsuki -= 1
            else:
                print("\nTu Umamusume falló el entrenamiento.\nStamina disminuyó en 5 puntos.\nGuts disminuyó en 5 puntos.\n")
                Stamina -= 5
                Guts -= 5
                satsuki -= 1
        elif training == "3":
            if random.random() < energia/100:
                print("\nPower aumentó en 20 puntos!\nStamina aumentó en 8 puntos!\n")
                Power += 20
                Stamina += 8
                energia = max(energia - 15, energia_min)
                satsuki -= 1
            else:
                print("\nTu Umamusume falló el entrenamiento.\nPower disminuyó en 5 puntos.\nStamina disminuyó en 5 puntos.\n")
                Power -= 5
                Stamina -= 5
                satsuki -= 1
        elif training == "4":
            if random.random() < energia/100:
                print("\nGuts aumentó en 12 puntos!\nSpeed y Power aumentaron en 4 puntos!\n")
                Guts += 12
                Speed += 4
                Power += 4
                energia = max(energia - 18, energia_min)
                satsuki -= 1
            else:
                print("\nTu Umamusume falló el entrenamiento.\nGuts disminuyó en 5 puntos.\nSpeed y Power disminuyeron en 5 puntos.\n")
                Guts -= 5
                Speed -= 5
                Power -= 5
                satsuki -= 1
        elif training == "5":
            if random.random() < energia/100:
                print("\nWit aumentó en 15 puntos!\nSpeed aumentó en 5 puntos!\n")
                Wit += 15
                Speed += 5
                energia = max(energia + 10, energia_min)
                satsuki -= 1
            else:
                print("\nTu Umamusume falló el entrenamiento.\n")
                energia = max(energia + 10, energia_min)
                satsuki -= 1

        else:
            print("\nNúmero no válido, intente de nuevo.")
    
    elif action == "2":
        rest = random.choice(rest_events)
        if rest == "Deprived":
            print("\nTu Umamusume no parece haber descansado bien.\nEnergía aumentó en 30 puntos.\n")
            energia = min(energia + 30, energia_max)
            satsuki -= 1

        elif rest == "Refreshed":
            print("\nTu Umamusume se siente renovada y lista para entrenar!\nEnergía aumentó en 50 puntos.\n")
            energia = min(energia + 50, energia_max)
            satsuki -= 1

        elif rest == "Well-Rested":
            print("\nTu Umamusume se siente increíblemente descansada y llena de energía!\nEnergía aumentó en 70 puntos.\n")
            energia = min(energia + 70, energia_max)
            satsuki -= 1

    elif action == "3":
        print("\nEstadísticas de " + Uma + ":\nSpeed: " + str(Speed) + "\nStamina: " + str(Stamina) + "\nPower: " + str(Power) + "\nGuts: " + str(Guts) + "\nWit: " + str(Wit))

    else:
        print("\nNúmero no válido, intente de nuevo.")
if satsuki == 0:
    race_satsuki = True

while race_satsuki:
    satsuki_prepare = input("\n¡El Satsuki Sho ha llegado!\n1. Ver predicciones\n2. Ver detalles\n3. Ver resultados\n")
    
    predict_speed = 180
    predict_stamina = 150
    predict_power = 160
    predict_guts = 140
    predict_wit = 125
    speed_prediction = round((Speed / predict_speed) * 100)
    stamina_prediction = round((Stamina / predict_stamina) * 100)
    power_prediction = round((Power / predict_power) * 100)
    guts_prediction = round((Guts / predict_guts) * 100)
    wit_prediction = round((Wit / predict_wit) * 100)
    overall_prediction = round((speed_prediction + stamina_prediction + power_prediction + guts_prediction + wit_prediction) / 5)
    overall_prediction = min(100, overall_prediction)
    
    if satsuki_prepare == "1":
        print("\nPredicciones para el Satsuki Sho:\nSpeed: " + str(speed_prediction) + "%\nStamina: " + str(stamina_prediction) + "%\nPower: " + str(power_prediction) + "%\nGuts: " + str(guts_prediction) + "%\nWit: " + str(wit_prediction) + "%\n")
        if overall_prediction > 80:
            print("\n¡Tu Umamusume no tiene competencia para ganar el Satsuki Sho!")
        elif overall_prediction > 60:
            print("\nTu Umamusume tiene una buena oportunidad de ganar el Satsuki Sho.")
        elif overall_prediction > 40:
            print("\nTu Umamusume puede tener estragos en ganar el Satsuki Sho.")
        else:
            print("\nTu Umamusume puede que no gane el Satsuki Sho.")
    
    elif satsuki_prepare == "2":
        print("\nDetalles del Satsuki Sho:\nDistancia: 2000m (Medium)\nTipo de pista: Césped\n")
    
    elif satsuki_prepare == "3":
        if random.random() < int(overall_prediction) / 100:
            print("\n¡Felicidades! Tu Umamusume ha ganado el Satsuki Sho!")
            victorias += 1
            race_satsuki = False
            break
        else:
            print("\nTu Umamusume no pudo ganar el Satsuki Sho esta vez.")
            race_satsuki = False
            break
    else:
        print("\nNúmero no válido, intente de nuevo.")

while derby > 0:
    print("\nTurnos restantes para el Tokyo Yushun (Derby): " + str(derby))
    print("Energía restante: " + str(energia))
    action = input("\nQué harás?\n1: Entrenar\n2: Descansar\n3: Ver estadísticas\n")
    if action == "1":
        training = input("\nQué deberia entrenar?\n1: Speed\n2: Stamina\n3: Power\n4: Guts\n5: Wit\n")
        if training == "1":
            if random.random() < energia/100:
                print("\nSpeed aumentó en 15 puntos!\nPower aumentó en 6 puntos!\n")
                Speed += 18
                Power += 6
                energia = max(energia - 10, energia_min)
                derby -= 1
            else:
                print("\nTu Umamusume falló el entrenamiento.\nSpeed disminuyó en 5 puntos.\nPower disminuyó en 5 puntos.\n")
                Speed -= 5
                Power -= 5
                derby -= 1
        elif training == "2":
            if random.random() < energia/100:
                print("\nStamina aumentó en 10 puntos!\nGuts aumentó en 4 puntos!\n")
                Stamina += 12
                Guts += 4
                energia = max(energia - 12, energia_min)
                derby -= 1
            else:
                print("\nTu Umamusume falló el entrenamiento.\nStamina disminuyó en 5 puntos.\nGuts disminuyó en 5 puntos.\n")
                Stamina -= 5
                Guts -= 5
                derby -= 1
        elif training == "3":
            if random.random() < energia/100:
                print("\nPower aumentó en 20 puntos!\nStamina aumentó en 8 puntos!\n")
                Power += 25
                Stamina += 8
                energia = max(energia - 15, energia_min)
                derby -= 1
            else:
                print("\nTu Umamusume falló el entrenamiento.\nPower disminuyó en 5 puntos.\nStamina disminuyó en 5 puntos.\n")
                Power -= 5
                Stamina -= 5
                derby -= 1
        elif training == "4":
            if random.random() < energia/100:
                print("\nGuts aumentó en 12 puntos!\nSpeed y Power aumentaron en 4 puntos!\n")
                Guts += 15
                Speed += 4
                Power += 4
                energia = max(energia - 18, energia_min)
                derby -= 1
            else:
                print("\nTu Umamusume falló el entrenamiento.\nGuts disminuyó en 5 puntos.\nSpeed y Power disminuyeron en 5 puntos.\n")
                Guts -= 5
                Speed -= 5
                Power -= 5
                derby -= 1
        elif training == "5":
            if random.random() < energia/100:
                print("\nWit aumentó en 15 puntos!\nSpeed aumentó en 5 puntos!\n")
                Wit += 18
                Speed += 5
                energia = max(energia + 10, energia_min)
                derby -= 1
            else:
                print("\nTu Umamusume falló el entrenamiento.\nWit disminuyó en 5 puntos.\nSpeed disminuyó en 5 puntos.\n")
                energia = max(energia + 10, energia_min)
                derby -= 1
        else:
            print("\nNúmero no válido, intente de nuevo.")
    elif action == "2":
        rest = random.choice(rest_events)
        if rest == "Deprived":
            print("\nTu Umamusume no parece haber descansado bien.\nEnergía aumentó en 30 puntos.\n")
            energia = min(energia + 30, energia_max)
            derby -= 1

        elif rest == "Refreshed":
            print("\nTu Umamusume se siente renovada y lista para entrenar!\nEnergía aumentó en 50 puntos.\n")
            energia = min(energia + 50, energia_max)
            derby -= 1

        elif rest == "Well-Rested":
            print("\nTu Umamusume se siente increíblemente descansada y llena de energía!\nEnergía aumentó en 70 puntos.\n")
            energia = min(energia + 70, energia_max)
            derby -= 1
    elif action == "3":
        print("\nEstadísticas de " + Uma + ":\nSpeed: " + str(Speed) + "\nStamina: " + str(Stamina) + "\nPower: " + str(Power) + "\nGuts: " + str(Guts) + "\nWit: " + str(Wit))
    else:
        print("\nNúmero no válido, intente de nuevo.")
if derby == 0:
    race_derby = True

while race_derby:
    derby_prepare = input("\n¡El Tokyo Yushun (Derby) ha llegado!\n1. Ver predicciones\n2. Ver detalles\n3. Ver resultados\n")
    
    if derby_prepare == "1":
        predict_speed = 190
        predict_stamina = 160
        predict_power = 170
        predict_guts = 150
        predict_wit = 130
        speed_prediction = round((Speed / predict_speed) * 100)
        stamina_prediction = round((Stamina / predict_stamina) * 100)
        power_prediction = round((Power / predict_power) * 100)
        guts_prediction = round((Guts / predict_guts) * 100)
        wit_prediction = round((Wit / predict_wit) * 100)
        overall_prediction = round((speed_prediction + stamina_prediction + power_prediction + guts_prediction + wit_prediction) / 5)
        overall_prediction = min(100, overall_prediction)
        print("\nPredicciones para el Tokyo Yushun (Derby):\nSpeed: " + str(speed_prediction) + "%\nStamina: " + str(stamina_prediction) + "%\nPower: " + str(power_prediction) + "%\nGuts: " + str(guts_prediction) + "%\nWit: " + str(wit_prediction) + "%\n")
        if overall_prediction > 80:
            print("\n¡Tu Umamusume no tiene competencia para ganar el Tokyo Yushun (Derby)!")
        elif overall_prediction > 60:
            print("\nTu Umamusume tiene una buena oportunidad de ganar el Tokyo Yushun (Derby).")
        elif overall_prediction > 40:
            print("\nTu Umamusume puede tener estragos en ganar el Tokyo Yushun (Derby).")
        else:
            print("\nTu Umamusume puede que no gane el Tokyo Yushun (Derby).")
    
    elif derby_prepare == "2":
        print("\nDetalles del Tokyo Yushun (Derby):\nDistancia: 2400m (Medium)\nTipo de pista: Césped\n")
    
    elif derby_prepare == "3":
        if random.random() < int(overall_prediction) / 100:
            print("\n¡Felicidades! Tu Umamusume ha ganado el Tokyo Yushun (Derby)!")
            victorias += 1
            race_derby = False
            break
        else:
            print("\nTu Umamusume no pudo ganar el Tokyo Yushun (Derby) esta vez.")
            race_derby = False
            break

while kikuka > 0:
    print("\nTurnos restantes para el Kikuka Sho: " + str(kikuka))
    print("Energía restante: " + str(energia))
    action = input("\nQué harás?\n1: Entrenar\n2: Descansar\n3: Ver estadísticas\n")
    if action == "1":
        training = input("\nQué deberia entrenar?\n1: Speed\n2: Stamina\n3: Power\n4: Guts\n5: Wit\n")
        if training == "1":
            if random.random() < energia/100:
                print("\nSpeed aumentó en 15 puntos!\nPower aumentó en 6 puntos!\n")
                Speed += 22
                Power += 6
                energia = max(energia - 10, energia_min)
                kikuka -= 1
            else:
                print("\nTu Umamusume falló el entrenamiento.\nSpeed disminuyó en 5 puntos.\nPower disminuyó en 5 puntos.\n")
                Speed -= 5
                Power -= 5
                kikuka -= 1
        elif training == "2":
            if random.random() < energia/100:
                print("\nStamina aumentó en 10 puntos!\nGuts aumentó en 4 puntos!\n")
                Stamina += 15
                Guts += 4
                energia = max(energia - 12, energia_min)
                kikuka -= 1
            else:
                print("\nTu Umamusume falló el entrenamiento.\nStamina disminuyó en 5 puntos.\nGuts disminuyó en 5 puntos.\n")
                Stamina -= 5
                Guts -= 5
                kikuka -= 1
        elif training == "3":
            if random.random() < energia/100:
                print("\nPower aumentó en 20 puntos!\nStamina aumentó en 8 puntos!\n")
                Power += 30
                Stamina += 8
                energia = max(energia - 15, energia_min)
                kikuka -= 1
            else:
                print("\nTu Umamusume falló el entrenamiento.\nPower disminuyó en 5 puntos.\nStamina disminuyó en 5 puntos.\n")
                Power -= 5
                Stamina -= 5
                kikuka -= 1
        elif training == "4":
            if random.random() < energia/100:
                print("\nGuts aumentó en 12 puntos!\nSpeed y Power aumentaron en 4 puntos!\n")
                Guts += 18
                Speed += 4
                Power += 4
                energia = max(energia - 18, energia_min)
                kikuka -= 1
            else:
                print("\nTu Umamusume falló el entrenamiento.\nGuts disminuyó en 5 puntos.\nSpeed y Power disminuyeron en 5 puntos.\n")
                Guts -= 5
                Speed -= 5
                Power -= 5
                kikuka -= 1
        elif training == "5":
            if random.random() < energia/100:
                print("\nWit aumentó en 15 puntos!\nSpeed aumentó en 5 puntos!\n")
                Wit += 22
                Speed += 5
                energia = max(energia + 10, energia_min)
                kikuka -= 1
            else:
                print("\nTu Umamusume falló el entrenamiento.\n")
                energia = max(energia + 10, energia_min)
                kikuka -= 1
        else:
            print("\nNúmero no válido, intente de nuevo.")
    elif action == "2":
        rest = random.choice(rest_events)
        if rest == "Deprived":
            print("\nTu Umamusume no parece haber descansado bien.\nEnergía aumentó en 30 puntos.\n")
            energia = min(energia + 30, energia_max)
            kikuka -= 1

        elif rest == "Refreshed":
            print("\nTu Umamusume se siente renovada y lista para entrenar!\nEnergía aumentó en 50 puntos.\n")
            energia = min(energia + 50, energia_max)
            kikuka -= 1

        elif rest == "Well-Rested":
            print("\nTu Umamusume se siente increíblemente descansada y llena de energía!\nEnergía aumentó en 70 puntos.\n")
            energia = min(energia + 70, energia_max)
            kikuka -= 1
    elif action == "3":
        print("\nEstadísticas de " + Uma + ":\nSpeed: " + str(Speed) + "\nStamina: " + str(Stamina) + "\nPower: " + str(Power) + "\nGuts: " + str(Guts) + "\nWit: " + str(Wit))
    else:
        print("\nNúmero no válido, intente de nuevo.")
if kikuka == 0:
    kikuka_race = True

while kikuka_race:
    kikuka_prepare = input("\n¡El Kikuka Sho ha llegado!\n1. Ver predicciones\n2. Ver detalles\n3. Ver resultados\n")

    predict_speed = 170
    predict_stamina = 170
    predict_power = 160
    predict_guts = 150
    predict_wit = 120
    speed_prediction = round((Speed / predict_speed) * 100)
    stamina_prediction = round((Stamina / predict_stamina) * 100)
    power_prediction = round((Power / predict_power) * 100)
    guts_prediction = round((Guts / predict_guts) * 100)
    wit_prediction = round((Wit / predict_wit) * 100)
    overall_prediction = round((speed_prediction + stamina_prediction + power_prediction + guts_prediction + wit_prediction) / 5)
    overall_prediction = min(100, overall_prediction)
    
    if kikuka_prepare == "1":
        print("\nPredicciones para el Kikuka Sho:\nSpeed: " + str(speed_prediction) + "%\nStamina: " + str(stamina_prediction) + "%\nPower: " + str(power_prediction) + "%\nGuts: " + str(guts_prediction) + "%\nWit: " + str(wit_prediction) + "%\n")
        if overall_prediction > 80:
            print("\n¡Tu Umamusume no tiene competencia para ganar el Kikuka Sho!")
        elif overall_prediction > 60:
            print("\nTu Umamusume tiene una buena oportunidad de ganar el Kikuka Sho.")
        elif overall_prediction > 40:
            print("\nTu Umamusume puede tener estragos en ganar el Kikuka Sho.")
        else:
            print("\nTu Umamusume puede que no gane el Kikuka Sho.")
    
    elif kikuka_prepare == "2":
        print("\nDetalles del Kikuka Sho:\nDistancia: 3000m (Long)\nTipo de pista: Césped\n")
    
    elif kikuka_prepare == "3":
        if random.random() < int(overall_prediction) / 100:
            print("\n¡Felicidades! Tu Umamusume ha ganado el Kikuka Sho!")
            victorias += 1
            if victorias == 3:
                print("\n¡Felicidades! Has ganado la Triple Corona con " + Uma + "!")
            kikuka_race = False
            break
        else:
            print("\nTu Umamusume no pudo ganar el Kikuka Sho esta vez.")
            kikuka_race = False
            break

while jcup > 0:
    print("\nTurnos restantes para el Japan Cup: " + str(jcup))
    print("Energía restante: " + str(energia))
    action = input("\nQué harás?\n1: Entrenar\n2: Descansar\n3: Ver estadísticas\n")
    if action == "1":
        training = input("\nQué deberia entrenar?\n1: Speed\n2: Stamina\n3: Power\n4: Guts\n5: Wit\n")
        if training == "1":
            if random.random() < energia/100:
                print("\nSpeed aumentó en 26 puntos!\nPower aumentó en 7 puntos!\n")
                Speed += 26
                Power += 7
                energia = max(energia - 10, energia_min)
                jcup -= 1
            else:
                print("\nTu Umamusume falló el entrenamiento.\nSpeed disminuyó en 5 puntos.\nPower disminuyó en 5 puntos.\n")
                Speed -= 5
                Power -= 5
                jcup -= 1
        elif training == "2":
            if random.random() < energia/100:
                print("\nStamina aumentó en 17 puntos!\nGuts aumentó en 5 puntos!\n")
                Stamina += 17
                Guts += 5
                energia = max(energia - 12, energia_min)
                jcup -= 1
            else:
                print("\nTu Umamusume falló el entrenamiento.\nStamina disminuyó en 5 puntos.\nGuts disminuyó en 5 puntos.\n")
                Stamina -= 5
                Guts -= 5
                jcup -= 1
        elif training == "3":
            if random.random() < energia/100:
                print("\nPower aumentó en 35 puntos!\nStamina aumentó en 9 puntos!\n")
                Power += 35
                Stamina += 9
                energia = max(energia - 15, energia_min)
                jcup -= 1
            else:
                print("\nTu Umamusume falló el entrenamiento.\nPower disminuyó en 5 puntos.\nStamina disminuyó en 5 puntos.\n")
                Power -= 5
                Stamina -= 5
                jcup -= 1
        elif training == "4":
            if random.random() < energia/100:
                print("\nGuts aumentó en 21 puntos!\nSpeed y Power aumentaron en 5 puntos!\n")
                Guts += 21
                Speed += 5
                Power += 5
                energia = max(energia - 18, energia_min)
                jcup -= 1
            else:
                print("\nTu Umamusume falló el entrenamiento.\nGuts disminuyó en 5 puntos.\nSpeed y Power disminuyeron en 5 puntos.\n")
                Guts -= 5
                Speed -= 5
                Power -= 5
                jcup -= 1
        elif training == "5":
            if random.random() < energia/100:
                print("\nWit aumentó en 15 puntos!\nSpeed aumentó en 5 puntos!\n")
                Wit += 26
                Speed += 6
                energia = max(energia + 10, energia_min)
                jcup -= 1
            else:
                print("\nTu Umamusume falló el entrenamiento.\n")
                energia = max(energia + 10, energia_min)
                jcup -= 1
        else:
            print("\nNúmero no válido, intente de nuevo.")
    elif action == "2":
        rest = random.choice(rest_events)
        if rest == "Deprived":
            print("\nTu Umamusume no parece haber descansado bien.\nEnergía aumentó en 30 puntos.\n")
            energia = min(energia + 30, energia_max)
            jcup -= 1

        elif rest == "Refreshed":
            print("\nTu Umamusume se siente renovada y lista para entrenar!\nEnergía aumentó en 50 puntos.\n")
            energia = min(energia + 50, energia_max)
            jcup -= 1

        elif rest == "Well-Rested":
            print("\nTu Umamusume se siente increíblemente descansada y llena de energía!\nEnergía aumentó en 70 puntos.\n")
            energia = min(energia + 70, energia_max)
            jcup -= 1
    elif action == "3":
        print("\nEstadísticas de " + Uma + ":\nSpeed: " + str(Speed) + "\nStamina: " + str(Stamina) + "\nPower: " + str(Power) + "\nGuts: " + str(Guts) + "\nWit: " + str(Wit))
    else:
        print("\nNúmero no válido, intente de nuevo.")

if jcup == 0:
    jcup_race = True

while jcup_race:
    jcup_prepare = input("\n¡El Japan Cup ha llegado!\n1. Ver predicciones\n2. Ver detalles\n3. Ver resultados\n")
    predict_speed = 190
    predict_stamina = 170
    predict_power = 180
    predict_guts = 160
    predict_wit = 130
    speed_prediction = round((Speed / predict_speed) * 100)
    stamina_prediction = round((Stamina / predict_stamina) * 100)
    power_prediction = round((Power / predict_power) * 100)
    guts_prediction = round((Guts / predict_guts) * 100)
    wit_prediction = round((Wit / predict_wit) * 100)
    overall_prediction = round((speed_prediction + stamina_prediction + power_prediction + guts_prediction + wit_prediction) / 5)
    overall_prediction = min(100, overall_prediction)
    if jcup_prepare == "1":
        print("\nPredicciones para el Japan Cup:\nSpeed: " + str(speed_prediction) + "%\nStamina: " + str(stamina_prediction) + "%\nPower: " + str(power_prediction) + "%\nGuts: " + str(guts_prediction) + "%\nWit: " + str(wit_prediction) + "%\n")
        if overall_prediction > 80:
            print("\n¡Tu Umamusume no tiene competencia para ganar el Japan Cup!")
        elif overall_prediction > 60:
            print("\nTu Umamusume tiene una buena oportunidad de ganar el Japan Cup.")
        elif overall_prediction > 40:
            print("\nTu Umamusume puede tener estragos en ganar el Japan Cup.")
        else:
            print("\nTu Umamusume puede que no gane el Japan Cup.")
    
    elif jcup_prepare == "2":
        print("\nDetalles del Japan Cup:\nDistancia: 2400m (Medium)\nTipo de pista: Césped\n")
    
    elif jcup_prepare == "3":
        if random.random() < int(overall_prediction) / 100:
            print("\n¡Felicidades! Tu Umamusume ha ganado el Japan Cup!")
            victorias += 1
            jcup_race = False
            break
        else:
            print("\nTu Umamusume no pudo ganar el Japan Cup esta vez.")
            jcup_race = False
            break

while arima > 0:
    print("\nTurnos restantes para el Arima Kinen: " + str(arima))
    print("Energía restante: " + str(energia))
    action = input("\nQué harás?\n1: Entrenar\n2: Descansar\n3: Ver estadísticas\n")
    if action == "1":
        training = input("\nQué deberia entrenar?\n1: Speed\n2: Stamina\n3: Power\n4: Guts\n5: Wit\n")
        if training == "1":
            if random.random() < energia/100:
                print("\nSpeed aumentó en 30 puntos!\nPower aumentó en 8 puntos!\n")
                Speed += 30
                Power += 8
                energia = max(energia - 10, energia_min)
                arima -= 1
            else:
                print("\nTu Umamusume falló el entrenamiento.\nSpeed disminuyó en 5 puntos.\nPower disminuyó en 5 puntos.\n")
                Speed -= 5
                Power -= 5
                arima -= 1
        elif training == "2":
            if random.random() < energia/100:
                print("\nStamina aumentó en 20 puntos!\nGuts aumentó en 6 puntos!\n")
                Stamina += 20
                Guts += 6
                energia = max(energia - 12, energia_min)
                arima -= 1
            else:
                print("\nTu Umamusume falló el entrenamiento.\nStamina disminuyó en 5 puntos.\nGuts disminuyó en 5 puntos.\n")
                Stamina -= 5
                Guts -= 5
                arima -= 1
        elif training == "3":
            if random.random() < energia/100:
                print("\nPower aumentó en 40 puntos!\nStamina aumentó en 10 puntos!\n")
                Power += 40
                Stamina += 10
                energia = max(energia - 15, energia_min)
                arima -= 1
            else:
                print("\nTu Umamusume falló el entrenamiento.\nPower disminuyó en 5 puntos.\nStamina disminuyó en 5 puntos.\n")
                Power -= 5
                Stamina -= 5
                arima -= 1
        elif training == "4":
            if random.random() < energia/100:
                print("\nGuts aumentó en 24 puntos!\nSpeed y Power aumentaron en 6 puntos!\n")
                Guts += 24
                Speed += 6
                Power += 6
                energia = max(energia - 18, energia_min)
                arima -= 1
            else:
                print("\nTu Umamusume falló el entrenamiento.\nGuts disminuyó en 5 puntos.\nSpeed y Power disminuyeron en 5 puntos.\n")
                Guts -= 5
                Speed -= 5
                Power -= 5
                arima -= 1
        elif training == "5":
            if random.random() < energia/100:
                print("\nWit aumentó en 30 puntos!\nSpeed aumentó en 7 puntos!\n")
                Wit += 30
                Speed += 7
                energia = max(energia + 10, energia_min)
                arima -= 1
            else:
                print("\nTu Umamusume falló el entrenamiento.\n")
                energia = max(energia + 10, energia_min)
                arima -= 1
        else:
            print("\nNúmero no válido, intente de nuevo.")
    elif action == "2":
        rest = random.choice(rest_events)
        if rest == "Deprived":
            print("\nTu Umamusume no parece haber descansado bien.\nEnergía aumentó en 30 puntos.\n")
            energia = min(energia + 30, energia_max)
            arima -= 1

        elif rest == "Refreshed":
            print("\nTu Umamusume se siente renovada y lista para entrenar!\nEnergía aumentó en 50 puntos.\n")
            energia = min(energia + 50, energia_max)
            arima -= 1

        elif rest == "Well-Rested":
            print("\nTu Umamusume se siente increíblemente descansada y llena de energía!\nEnergía aumentó en 70 puntos.\n")
            energia = min(energia + 70, energia_max)
            arima -= 1
    elif action == "3":
        print("\nEstadísticas de " + Uma + ":\nSpeed: " + str(Speed) + "\nStamina: " + str(Stamina) + "\nPower: " + str(Power) + "\nGuts: " + str(Guts) + "\nWit: " + str(Wit))
    else:
        print("\nNúmero no válido, intente de nuevo.")
if arima == 0:
    arima_race = True

while arima_race:
    arima_prepare = input("\n¡El Arima Kinen ha llegado!\n1. Ver predicciones\n2. Ver detalles\n3. Ver resultados\n")
    predict_speed = 190
    predict_stamina = 170
    predict_power = 180
    predict_guts = 160
    predict_wit = 130
    speed_prediction = round((Speed / predict_speed) * 100)
    stamina_prediction = round((Stamina / predict_stamina) * 100)
    power_prediction = round((Power / predict_power) * 100)
    guts_prediction = round((Guts / predict_guts) * 100)
    wit_prediction = round((Wit / predict_wit) * 100)
    overall_prediction = round((speed_prediction + stamina_prediction + power_prediction + guts_prediction + wit_prediction) / 5)
    overall_prediction = min(100, overall_prediction)
    if arima_prepare == "1":

        print("\nPredicciones para el Arima Kinen:\nSpeed: " + str(speed_prediction) + "%\nStamina: " + str(stamina_prediction) + "%\nPower: " + str(power_prediction) + "%\nGuts: " + str(guts_prediction) + "%\nWit: " + str(wit_prediction) + "%\n")
        if overall_prediction > 80:
            print("\n¡Tu Umamusume no tiene competencia para ganar el Arima Kinen!")
        elif overall_prediction > 60:
            print("\nTu Umamusume tiene una buena oportunidad de ganar el Arima Kinen.")
        elif overall_prediction > 40:
            print("\nTu Umamusume puede tener estragos en ganar el Arima Kinen.")
        else:
            print("\nTu Umamusume puede que no gane el Arima Kinen.")
    
    elif arima_prepare == "2":
        print("\nDetalles del Arima Kinen:\nDistancia: 2500m (Medium)\nTipo de pista: Césped\n")
    
    elif arima_prepare == "3":
        if random.random() < int(overall_prediction) / 100:
            print("\n¡Felicidades! Tu Umamusume ha ganado el Arima Kinen!")
            victorias += 1
            arima_race = False
            break
        else:
            print("\nTu Umamusume no pudo ganar el Arima Kinen esta vez.")
            arima_race = False
            break

results = True

if results:
    if victorias == 0:
        print("\nTu Umamusume no pudo ganar ninguna carrera importante esta temporada.\n")
        print("Estadisticas finales de " + Uma + ":\nSpeed: " + str(Speed) + "\nStamina: " + str(Stamina) + "\nPower: " + str(Power) + "\nGuts: " + str(Guts) + "\nWit: " + str(Wit))

    elif victorias == 1:
        print("\nTu Umamusume ganó una carrera importante esta temporada.\n")
        print("Estadisticas finales de " + Uma + ":\nSpeed: " + str(Speed) + "\nStamina: " + str(Stamina) + "\nPower: " + str(Power) + "\nGuts: " + str(Guts) + "\nWit: " + str(Wit))

    elif victorias == 2:
        print("\nTu Umamusume ganó dos carreras importantes esta temporada.\n")
        print("Estadisticas finales de " + Uma + ":\nSpeed: " + str(Speed) + "\nStamina: " + str(Stamina) + "\nPower: " + str(Power) + "\nGuts: " + str(Guts) + "\nWit: " + str(Wit))

    elif victorias == 3:
        print("\nTu Umamusume ganó tres carreras importantes esta temporada.\n")
        print("Estadisticas finales de " + Uma + ":\nSpeed: " + str(Speed) + "\nStamina: " + str(Stamina) + "\nPower: " + str(Power) + "\nGuts: " + str(Guts) + "\nWit: " + str(Wit))

    elif victorias == 4:
        print("\nTu Umamusume ganó cuatro carreras importantes esta temporada.\n")
        print("Estadisticas finales de " + Uma + ":\nSpeed: " + str(Speed) + "\nStamina: " + str(Stamina) + "\nPower: " + str(Power) + "\nGuts: " + str(Guts) + "\nWit: " + str(Wit))

    elif victorias == 5:
        print("\nTu Umamusume ganó cinco carreras importantes esta temporada.\n")
        print("Estadisticas finales de " + Uma + ":\nSpeed: " + str(Speed) + "\nStamina: " + str(Stamina) + "\nPower: " + str(Power) + "\nGuts: " + str(Guts) + "\nWit: " + str(Wit))
        print("\n             ___________\n            '._==_==_=_.'\n            .-\\:      /-.\n           | (|:.     |) |\n            '-|:.     |-'\n              \\::.    /\n               '::. .'\n                 ) (\n               _.' '._\n              '-------'\n")