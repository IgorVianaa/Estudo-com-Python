def tempo_foco():

    quanto_tempo = int(input('Quanto tempo deseja o período de foco? '))
    match quanto_tempo:
        case _ if 25 <= quanto_tempo <= 45:
            print(f'O tempo foi ajustado para {quanto_tempo}')
        case x if x < 25:
            print(f'Este tempo é curto, tem que ser entre 25 e 45min')
        case x if x > 45:
            print(f'Este tempo é longo, tem que ser entre 25 e 45min')


tempo_foco()

