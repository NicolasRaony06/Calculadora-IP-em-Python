def titulo(coeficiente, valor):
    print(f"-_-"*coeficiente,valor,"-_-"*coeficiente,"\n")

titulo(15, "IP ADDRESSES")
print(
'''Starting IP Address      Ending IP Address       Subnet Mask   
    Class A 10.0.0.0	   10.255.255.255	   255.0.0.0 
    Class B 172.16.0.0	   172.31.255.255	   255.255.0.0  
    Class C 192.168.0.0	   192.168.255.255	   255.255.255.0\n''')
while True:
    try:
        while True:
            ip = input("Digite o endereço ip: ").split('.')

            for octeto in range(len(ip)):
                ip[octeto] = int(ip[octeto])

            acertos = 0
            for octeto in ip:
                if octeto in range(0, 256):
                    acertos += 1 
                    continue
                else:
                    break

            if acertos == 4:
                break
            else:
                print('Valor inválido\n')
                continue
        break
    except ValueError:
        print("Valor inválido\n")
        continue
    
while True:
    mask = int(input("\nDigite o valor da máscara: ").strip("/"))
    if mask in range(8, 31):
        break
    else:
        print('Valor inválido')
        continue

titulo(15, "ADDRESS RESULTS")

classe = ''
if ip[0] >= 1 and ip[0] < 10:
    classe = 'Class A - Public'
elif ip[0] > 10 and ip[0] < 128:
    classe = 'Class A - Public'
elif ip[0] > 127 and ip[0] < 172:
    classe = 'Class B - Public'
elif ip[0] == 172:
    if ip[1] > 31:
        classe = 'Class B - Public'
    if ip[1] > 15 and ip[1] < 32:
        classe = 'Class B - Private'
elif ip[0] > 172 and ip[0] < 192:
    classe = 'class B - Público'
elif ip[0] == 192:
    if ip[1] == 168:
        classe = 'Class C - Private'
    else:
        classe = 'Class C - Public'
elif ip[0] > 192 and ip[0] < 224:
    classe = 'Class C - Public'
elif ip[0] > 223 and ip[0] < 240:
    classe = 'Class D - Public'
elif ip[0] > 239 and ip[0] < 256:
    classe = 'Class E - Public'
elif ip[0] == 10:
    classe = 'Class A - Private'

print('Address: {}.{}.{}.{} - {}'.format(ip[0], ip[1], ip[2], ip[3], classe))

def calcular_ip(ip_info):
    net_mask = ip_info['net_mask']
    net_mask2 = []
    net_mask2.extend(net_mask)
    net_mask2.pop(-1)
    posicao = -1
    for octeto in net_mask2:
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

    print(f'\nNetmask: {net_mask[0]}.{net_mask[1]}.{net_mask[2]}.{net_mask[3]} = {net_mask[4]}')
    print('\nSubnets:')
    for jump in range(0, range_lista[0], range_lista[1]):
        ip[posicao] = jump
        print(' {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], ip[3]))

    print(f'\nHosts/Net: {ip_info['hostsnet']}')

match mask:
    case 8:
        ip_info = {'range_lista': [255, 255], 'net_mask': [255,0,0,0,8], 'hostsnet': (2 ** 24 - 2)}
        calcular_ip(ip_info)
    case 9:
        ip_info = {'range_lista': [129, 128], 'net_mask': [255,128,0,0,9], 'hostsnet': (2 ** 23 - 2)}
        calcular_ip(ip_info)
    case 10:
        ip_info = {'range_lista': [193, 64], 'net_mask': [255,192,0,0,10], 'hostsnet': (2 ** 22 - 2)}
        calcular_ip(ip_info)
    case 11:
        ip_info = {'range_lista': [225, 32], 'net_mask': [255,224,0,0,11], 'hostsnet': (2 ** 21 - 2)}
        calcular_ip(ip_info)
    case 12:
        ip_info = {'range_lista': [241, 16], 'net_mask': [255,240,0,0,12], 'hostsnet': (2 ** 20 - 2)}
        calcular_ip(ip_info)
    case 13:
        ip_info = {'range_lista': [249, 8], 'net_mask': [255,248,0,0,13], 'hostsnet': (2 ** 19 - 2)}
        calcular_ip(ip_info)
    case 14:
        ip_info = {'range_lista': [253, 4], 'net_mask': [255,252,0,0,14], 'hostsnet': (2 ** 18 - 2)}
        calcular_ip(ip_info)
    case 15:
        ip_info = {'range_lista': [255, 2], 'net_mask': [255,254,0,0,15], 'hostsnet': (2 ** 17 - 2) }
        calcular_ip(ip_info)
    case 16:
        ip_info = {'range_lista': [255, 255], 'net_mask': [255,255,0,0,16], 'hostsnet': (2 ** 16 - 2)}
        calcular_ip(ip_info)
    case 17:
        ip_info = {'range_lista': [129, 128], 'net_mask': [255,255,128,0,17], 'hostsnet': (2 ** 15 - 2)}
        calcular_ip(ip_info)
    case 18:
        ip_info = {'range_lista': [193, 64], 'net_mask': [255,255,192,0,18], 'hostsnet': (2 ** 14 - 2)}
        calcular_ip(ip_info)
    case 19:
        ip_info = {'range_lista': [225, 32], 'net_mask': [255,255,224,0,19], 'hostsnet': (2 ** 13 - 2)}
        calcular_ip(ip_info)
    case 20:
        ip_info = {'range_lista': [241, 16], 'net_mask': [255,255,240,0,20], 'hostsnet': (2 ** 12 - 2)}
        calcular_ip(ip_info)
    case 21:
        ip_info = {'range_lista': [249, 8], 'net_mask': [255,255,248,0,21], 'hostsnet': (2 ** 11 - 2)}
        calcular_ip(ip_info)
    case 22:
        ip_info = {'range_lista': [253, 4], 'net_mask': [255,255,252,0,22], 'hostsnet': (2 ** 10 - 2)}
        calcular_ip(ip_info)
    case 23:
        ip_info = {'range_lista': [255, 2], 'net_mask': [255,255,254,0,23], 'hostsnet': (2 ** 9 - 2)}
        calcular_ip(ip_info)
    case 24:
        ip_info = {'range_lista': [255, 255], 'net_mask': [255,255,255,0,24], 'hostsnet': (2 ** 8 - 2)}
        calcular_ip(ip_info)
    case 25:
        ip_info = {'range_lista': [129, 128], 'net_mask': [255,255,255,128,25], 'hostsnet': (2 ** 7 - 2)}
        calcular_ip(ip_info)
    case 26:
        ip_info = {'range_lista': [193, 64], 'net_mask': [255,255,255,192,26], 'hostsnet': (2 ** 6 - 2)}
        calcular_ip(ip_info)
    case 27:
        ip_info = {'range_lista': [225, 32], 'net_mask': [255,255,255,224,27], 'hostsnet': (2 ** 5 - 2)}
        calcular_ip(ip_info)
    case 28:
        ip_info = {'range_lista': [241, 16], 'net_mask': [255,255,255,241,28], 'hostsnet': (2 ** 4 - 2)}
        calcular_ip(ip_info)
    case 29:
        ip_info = {'range_lista': [249, 8], 'net_mask': [255,255,255,248,29], 'hostsnet': (2 ** 3 - 2)}
        calcular_ip(ip_info)
    case 30:
        ip_info = {'range_lista': [253, 4], 'net_mask': [255,255,255,252,30], 'hostsnet': (2 ** 2 - 2)}
        calcular_ip(ip_info)