def titulo(coeficiente, valor):
    print(f"-_-"*coeficiente,valor,"-_-"*coeficiente,"\n")

def classe_ip(ip):
    if ip[0] in range(1, 10): #TODO teste: ip[0] in range(1, 10)
        classe = 'Class A - Public'
    elif ip[0] in range(11, 128): #TODO teste em: ip[0] > 10 and ip[0] < 128
        classe = 'Class A - Public'
    elif ip[0] in range(128, 172): #TODO teste em: ip[0] > 127 and ip[0] < 172
        classe = 'Class B - Public'
    elif ip[0] == 172:
        if ip[1] > 31:
            classe = 'Class B - Public'
        if ip[1] in range(16, 32): #TODO teste em: ip[1] > 15 and ip[1] < 32
            classe = 'Class B - Private'
    elif ip[0] in range(173, 192): #TODO teste em: ip[0] > 172 and ip[0] < 192
        classe = 'class B - Público'
    elif ip[0] == 192:
        if ip[1] == 168:
            classe = 'Class C - Private'
        else:
            classe = 'Class C - Public'
    elif ip[0] in range(193, 224): #TODO teste em: ip[0] > 192 and ip[0] < 224
        classe = 'Class C - Public'
    elif ip[0] in range(224, 240): #TODO teste em: ip[0] > 223 and ip[0] < 240
        classe = 'Class D - Public'
    elif ip[0] in range(240, 256): #TODO teste em: ip[0] > 239 and ip[0] < 256
        classe = 'Class E - Public'
    elif ip[0] == 10:
        classe = 'Class A - Private'
    
    return classe

def calcular_ip(ip_info, ip, mascara): #TODO adicionar função de calcular hostnet e o range do pulos.
    octetos_completos = mascara//8
    octetos_incompletos = mascara%8

    bits = [128,64,32,16,8,4,2,1]

    cdir = [0,0,0,0]
    for i in range(octetos_completos):
        cdir[i] = 255

    octeto = 0
    for i in range(octetos_incompletos):
        octeto += bits[i]
        cdir[octetos_completos] = octeto

    posicao = -1
    for octeto in cdir:
        posicao += 1
        if octeto < 255:
            match posicao:
                case 1:
                    ip[posicao + 1] = 0
                    ip[posicao + 2] = 0
                    broadcast_octetos = [ip[0], ip[1], 255, 255]
                    lasthost_octetos = [ip[0], ip[1], 255, 254]
                    firsthost_octetos = [ip[0], ip[1], ip[2], 1]
                    break
                case 2:
                    ip[posicao + 1] = 0
                    broadcast_octetos = [ip[0], ip[1], ip[2], 255]
                    lasthost_octetos = [ip[0], ip[1], ip[2], 254]
                    firsthost_octetos = [ip[0], ip[1], ip[2], 1]
                    break
                case 3:
                    broadcast_octetos = [ip[0], ip[1], ip[2], ip[3]]
                    lasthost_octetos = [ip[0], ip[1], ip[2], ip[3]]
                    firsthost_octetos = [ip[0], ip[1], ip[2], 1]
                    break
        else:
            continue

    jumps = []
    jumps2 = []
    range_lista = ip_info['range_lista']
    for i in range(0, range_lista[0], range_lista[1]):
        jumps.append(i)
        jumps2.append(i)
    del (jumps2[0])

    for j in range(0, len(jumps)):
        if j <= len(jumps2) - 1:
            if ip[posicao] >= jumps[j] and ip[posicao] < jumps2[j]:
                ip[posicao] = jumps[j]
                print('\nNetwork: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], ip[3]))

                ip[posicao] = jumps2[j] - 1
                broadcast_octetos[posicao] = jumps2[j] - 1
                print(' Broadcast: {}.{}.{}.{}'.format(broadcast_octetos[0], broadcast_octetos[1], broadcast_octetos[2], broadcast_octetos[3]))

                match posicao:
                    case 3:
                        firsthost_octetos[posicao] = jumps[j] + 1
                        print(' Firsthost: {}.{}.{}.{}'.format(firsthost_octetos[0], firsthost_octetos[1], firsthost_octetos[2], firsthost_octetos[3]))
                    case _:
                        firsthost_octetos[posicao] = jumps[j]
                        print(' Firsthost: {}.{}.{}.{}'.format(firsthost_octetos[0], firsthost_octetos[1], firsthost_octetos[2], firsthost_octetos[3]))

                match posicao:
                    case 3:
                        lasthost_octetos[posicao] = jumps2[j] - 2
                        print(' Lasthost: {}.{}.{}.{}'.format(lasthost_octetos[0], lasthost_octetos[1], lasthost_octetos[2], lasthost_octetos[3]))
                    case _:
                        lasthost_octetos[posicao] = jumps2[j] - 1
                        print(' Lasthost: {}.{}.{}.{}'.format(lasthost_octetos[0], lasthost_octetos[1], lasthost_octetos[2], lasthost_octetos[3]))
        else:
            if ip[posicao] >= jumps[j]:
                ip[posicao] = jumps[j]
                print('\nNetwork: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], ip[3]))

                ip[posicao] = jumps[j] - 1
                broadcast_octetos[posicao] = 255
                print(' Broadcast: {}.{}.{}.{}'.format(broadcast_octetos[0], broadcast_octetos[1], broadcast_octetos[2], broadcast_octetos[3]))

                match posicao:
                    case 3:
                        firsthost_octetos[posicao] = jumps[j] + 1
                        print(' Firsthost: {}.{}.{}.{}'.format(firsthost_octetos[0], firsthost_octetos[1], firsthost_octetos[2], firsthost_octetos[3]))
                    case _:
                        firsthost_octetos[posicao] = jumps[j]
                        print(' Firsthost: {}.{}.{}.{}'.format(firsthost_octetos[0], firsthost_octetos[1], firsthost_octetos[2], firsthost_octetos[3]))

                match posicao:
                    case 3:
                        lasthost_octetos[posicao] = 254
                        print(' Lasthost: {}.{}.{}.{}'.format(lasthost_octetos[0], lasthost_octetos[1], lasthost_octetos[2], lasthost_octetos[3]))
                    case _:
                        lasthost_octetos[posicao] = 255
                        print(' Lasthost: {}.{}.{}.{}'.format(lasthost_octetos[0], lasthost_octetos[1], lasthost_octetos[2], lasthost_octetos[3]))

    print(f'\nNetmask: {cdir[0]}.{cdir[1]}.{cdir[2]}.{cdir[3]} = {mascara}')
    print('\nSubnets:')
    for jump in range(0, range_lista[0], range_lista[1]):
        ip[posicao] = jump
        print(' {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], ip[3]))

    print(f'\nHosts/Net: {ip_info['hostsnet']}')