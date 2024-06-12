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

print(f'Address: {ip[0]}.{ip[1]}.{ip[2]}.{ip[3]} - {classe_ip(ip)}')

calcular_ip(ip, mask)                          
