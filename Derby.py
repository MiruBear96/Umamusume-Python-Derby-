print("----UMAMUSUME: PYTHON DERBY!---")

Uma = None
Speed = None
Stamina = None
Power = None
Guts = None
Wit = None




Intro = True

while Intro:
    UmaSelect = input("\nElije tu Umamusume:\n1: Eishin Flash\n2: Twin Turbo\n3: Agnes Tachyon\n4: Gold City\n5: Matikanetannhauser\n")

    if UmaSelect == "1":
        Decide1 = input(str("\nEishin Flash | Meisterschaft\nSpeed: 122\nStamina: 101\nPower: 113\nGuts: 100\nWit: 114\nEstá seguro? Y/N\n"))
        if Decide1 == "y":
            print("Has elegido a Eishin Flash!")
            Uma = "Eishin Flash"
            Speed = 122
            Stamina = 101
            Power = 113
            Guts = 100
            Wit = 114
            break
        elif Decide1 == "n":
            continue
        else:
            print("\nRespuesta no valida, intente de nuevo.")
    
    elif UmaSelect == "2":
        Decide2 = input(str("\nTwin Turbo | Blast Mode! Turbo Engine\nSpeed: 137\nStamina: 98\nPower: 107\nGuts: 119\nWit: 89\nEstá seguro? Y/N\n"))
        if Decide2 == "y":
            print("Has elegido a Twin Turbo!")
            Uma = "Twin Turbo"
            Speed = 137
            Stamina = 98
            Power = 107
            Guts = 119
            Wit = 89
            break
        elif Decide2 == "n":
            continue
        else:
            print("\nRespuesta no valida, intente de nuevo.")

    elif UmaSelect == "3":
        Decide3 = input(str("\nAgnes Tachyon | Tach-nology\nSpeed: 112\nStamina: 104\nPower: 104\nGuts: 108\nWit: 122\nEstá seguro? Y/N\n"))
        if Decide3 == "y":
            print("Has elegido a Agnes Tachyon!")
            Uma = "Agnes Tachyon"
            Speed = 112
            Stamina = 104
            Power = 104
            Guts = 108
            Wit = 122
            break
        elif Decide3 == "n":
            continue
        else:
            print("\nRespuesta no valida, intente de nuevo.")

    elif UmaSelect == "4":
        Decide4 = input(str("\nGold City | Authentic / 1928\nSpeed: 109\nStamina: 113\nPower: 114\nGuts: 112\nWit: 102\nEstá seguro? Y/N\n"))
        if Decide4 == "y":
            print("Has elegido a Gold City!")
            Uma = "Gold City"
            Speed = 109
            Stamina = 113
            Power = 114
            Guts = 112
            Wit = 102
            break
        elif Decide4 == "n":
            continue
        else:
            print("\nRespuesta no valida, intente de nuevo.")

    elif UmaSelect == "5":
        Decide5 = input(str("\nMatikanetannhauser | Clippety-Tippety-Clop\nSpeed: 103\nStamina: 117\nPower: 106\nGuts: 114\nWit: 110\nEstá seguro? Y/N\n"))
        if Decide5 == "y":
            print("Has elegido a Matikanetannhauser!")
            Uma = "Matikanetannhauser"
            break
        elif Decide5 == "n":
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

energia = 100
energia_max = 100
energia_min = 0

import random
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
                print("\nSpeed aumentó en 15 puntos!")
                Speed += 15
                energia = max(energia - 10, energia_min)
                satsuki -= 1
            else:
                print("\nTu Umamusume falló el entrenamiento.\nSpeed disminuyó en 5 puntos.\n")
                Speed -= 5
                satsuki -= 1
        elif training == "2":
            if random.random() < energia/100:
                print("\nStamina aumentó en 10 puntos!")
                Stamina += 10
                energia = max(energia - 12, energia_min)
                satsuki -= 1
            else:
                print("\nTu Umamusume falló el entrenamiento.\nStamina disminuyó en 5 puntos.\n")
                Stamina -= 5
                satsuki -= 1
        elif training == "3":
            if random.random() < energia/100:
                print("\nPower aumentó en 20 puntos!")
                Power += 20
                energia = max(energia - 15, energia_min)
                satsuki -= 1
            else:
                print("\nTu Umamusume falló el entrenamiento.\nPower disminuyó en 5 puntos.\n")
                Power -= 5
                satsuki -= 1
        elif training == "4":
            if random.random() < energia/100:
                print("\nGuts aumentó en 12 puntos!")
                Guts += 12
                energia = max(energia - 18, energia_min)
                satsuki -= 1
            else:
                print("\nTu Umamusume falló el entrenamiento.\nGuts disminuyó en 5 puntos.\n")
                Guts -= 5
                satsuki -= 1
        elif training == "5":
            if random.random() < energia/100:
                print("\nWit aumentó en 10 puntos!")
                Wit += 10
                energia = min(energia + 10, energia_max)
                satsuki -= 1
            else:
                print("\nTu Umamusume falló el entrenamiento.\n")
                energia = min(energia + 10, energia_max)
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
    
    if satsuki_prepare == "1":
        predict_speed = 180
        predict_stamina = 150
        predict_power = 160
        predict_guts = 140
        predict_wit = 125
        speed_prediction = int((Speed / predict_speed) * 100)
        stamina_prediction = int((Stamina / predict_stamina) * 100)
        power_prediction = int((Power / predict_power) * 100)
        guts_prediction = int((Guts / predict_guts) * 100)
        wit_prediction = int((Wit / predict_wit) * 100)
        overall_prediction = int((speed_prediction + stamina_prediction + power_prediction + guts_prediction + wit_prediction) / 5)
        print("\nPredicciones para el Satsuki Sho:\nSpeed: " + int(speed_prediction) + "%\nStamina: " + int(stamina_prediction) + "%\nPower: " + int(power_prediction) + "%\nGuts: " + int(guts_prediction) + "%\nWit: " + int(wit_prediction))
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
        if random.random() < int((Speed + Stamina + Power + Guts + Wit) / 5) :
            print("\n¡Felicidades! Tu Umamusume ha ganado el Satsuki Sho!")
            victorias += 1
        else:
            print("\nTu Umamusume no pudo ganar el Satsuki Sho esta vez.")
    else:
        print("\nNúmero no válido, intente de nuevo.")            