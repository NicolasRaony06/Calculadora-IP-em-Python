def cidr_to_netmask(ip): #receber ip completo ou apenas mascara em formato cidr
    BITS = [128,64,32,16,8,4,2,1]

    ip = ip.split('/')
                                
    mascara = ip[1].split('.')

    if not len(mascara) == 4:
        net_mask = []
        for i in range(int(mascara[0])//8):
            net_mask.append(255)

        value = 0
        if int(mascara[0])%8:
            for i, bit in enumerate(BITS):
                value += bit
                if i+1 == int(mascara[0])%8:
                    break
            net_mask.append(value)
        
        while not len(net_mask) == 4:
            net_mask.append(0)

    return net_mask

if __name__ == '__main__':
    cidr_to_netmask()