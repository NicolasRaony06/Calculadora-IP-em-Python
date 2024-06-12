from utilitarios import titulo, classe_ip, calcular_ip

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

classe = classe_ip(ip)

print('Address: {}.{}.{}.{} - {}'.format(ip[0], ip[1], ip[2], ip[3], classe))

match mask:
    case 8:
        ip_info = {'range_lista': [255, 255], 'net_mask': [255,0,0,0,8], 'hostsnet': (2 ** 24 - 2)}
        calcular_ip(ip_info, ip)
    case 9:
        ip_info = {'range_lista': [129, 128], 'net_mask': [255,128,0,0,9], 'hostsnet': (2 ** 23 - 2)}
        calcular_ip(ip_info, ip)
    case 10:
        ip_info = {'range_lista': [193, 64], 'net_mask': [255,192,0,0,10], 'hostsnet': (2 ** 22 - 2)}
        calcular_ip(ip_info, ip)
    case 11:
        ip_info = {'range_lista': [225, 32], 'net_mask': [255,224,0,0,11], 'hostsnet': (2 ** 21 - 2)}
        calcular_ip(ip_info, ip)
    case 12:
        ip_info = {'range_lista': [241, 16], 'net_mask': [255,240,0,0,12], 'hostsnet': (2 ** 20 - 2)}
        calcular_ip(ip_info, ip)
    case 13:
        ip_info = {'range_lista': [249, 8], 'net_mask': [255,248,0,0,13], 'hostsnet': (2 ** 19 - 2)}
        calcular_ip(ip_info, ip)
    case 14:
        ip_info = {'range_lista': [253, 4], 'net_mask': [255,252,0,0,14], 'hostsnet': (2 ** 18 - 2)}
        calcular_ip(ip_info, ip)
    case 15:
        ip_info = {'range_lista': [255, 2], 'net_mask': [255,254,0,0,15], 'hostsnet': (2 ** 17 - 2) }
        calcular_ip(ip_info, ip)
    case 16:
        ip_info = {'range_lista': [255, 255], 'net_mask': [255,255,0,0,16], 'hostsnet': (2 ** 16 - 2)}
        calcular_ip(ip_info, ip)
    case 17:
        ip_info = {'range_lista': [129, 128], 'net_mask': [255,255,128,0,17], 'hostsnet': (2 ** 15 - 2)}
        calcular_ip(ip_info, ip)
    case 18:
        ip_info = {'range_lista': [193, 64], 'net_mask': [255,255,192,0,18], 'hostsnet': (2 ** 14 - 2)}
        calcular_ip(ip_info, ip)
    case 19:
        ip_info = {'range_lista': [225, 32], 'net_mask': [255,255,224,0,19], 'hostsnet': (2 ** 13 - 2)}
        calcular_ip(ip_info, ip)
    case 20:
        ip_info = {'range_lista': [241, 16], 'net_mask': [255,255,240,0,20], 'hostsnet': (2 ** 12 - 2)}
        calcular_ip(ip_info, ip)
    case 21:
        ip_info = {'range_lista': [249, 8], 'net_mask': [255,255,248,0,21], 'hostsnet': (2 ** 11 - 2)}
        calcular_ip(ip_info, ip)
    case 22:
        ip_info = {'range_lista': [253, 4], 'net_mask': [255,255,252,0,22], 'hostsnet': (2 ** 10 - 2)}
        calcular_ip(ip_info, ip)
    case 23:
        ip_info = {'range_lista': [255, 2], 'net_mask': [255,255,254,0,23], 'hostsnet': (2 ** 9 - 2)}
        calcular_ip(ip_info, ip)
    case 24:
        ip_info, ip = {'range_lista': [255, 255], 'net_mask': [255,255,255,0,24], 'hostsnet': (2 ** 8 - 2)}
        calcular_ip(ip_info, ip)
    case 25:
        ip_info = {'range_lista': [129, 128], 'net_mask': [255,255,255,128,25], 'hostsnet': (2 ** 7 - 2)}
        calcular_ip(ip_info, ip)
    case 26:
        ip_info = {'range_lista': [193, 64], 'net_mask': [255,255,255,192,26], 'hostsnet': (2 ** 6 - 2)}
        calcular_ip(ip_info, ip)
    case 27:
        ip_info = {'range_lista': [225, 32], 'net_mask': [255,255,255,224,27], 'hostsnet': (2 ** 5 - 2)}
        calcular_ip(ip_info, ip)
    case 28:
        ip_info = {'range_lista': [241, 16], 'net_mask': [255,255,255,241,28], 'hostsnet': (2 ** 4 - 2)}
        calcular_ip(ip_info, ip)
    case 29:
        ip_info = {'range_lista': [249, 8], 'net_mask': [255,255,255,248,29], 'hostsnet': (2 ** 3 - 2)}
        calcular_ip(ip_info, ip)
    case 30:
        ip_info = {'range_lista': [253, 4], 'net_mask': [255,255,255,252,30], 'hostsnet': (2 ** 2 - 2)}
        calcular_ip(ip_info, ip)