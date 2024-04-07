import flet as ft

def main(page: ft.Page):
    def info_envio(address, network, broadcast, firsthost, lasthost, netmask, hosts_net, subnets, subnets_valores):
            global informacoes_ip
            informacoes_ip = ft.Column([ft.Text(address), ft.Text(network), ft.Text(broadcast), ft.Text(firsthost), ft.Text(lasthost), ft.Text(netmask),  ft.Text(hosts_net), ft.Text(subnets), subnets_valores])

            informacoes_rede = ft.Container(
                content= informacoes_ip,
                padding=15,
                width= 320,
                alignment= ft.alignment.center,
                bgcolor=ft.colors.BLACK12,
                border_radius=10
            )

            centralizar_info = ft.Row([informacoes_rede], alignment=ft.MainAxisAlignment.CENTER)

            page.add(titulo, envio_info, centralizar_info)

    def informacoes(classe, ip, mascara): 
        ip_entrada.value = ''
        def calculo_ip(range_lista, octetos, net_mask, hostsnet, calcular, predef_mascara_info):
            global address, network, broadcast, firsthost, lasthost, netmask, hosts_net, subnets, subnets_valores
            match calcular:
                case True:
                    address = f'Address: {ip[0]}.{ip[1]}.{ip[2]}.{ip[3]} | {classe}'

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
                    for i in range(0, range_lista[0], range_lista[1]):
                        jumps.append(i)
                        jumps2.append(i)
                    del (jumps2[0])

                    for j in range(0, len(jumps)):
                        if j <= len(jumps2) - 1:
                            if ip[posicao] >= jumps[j] and ip[posicao] < jumps2[j]:
                                ip[posicao] = jumps[j]
                                network = ('\nNetwork: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], ip[3]))

                                ip[posicao] = jumps2[j] - 1
                                broadcast_octetos[posicao] = jumps2[j] - 1
                                broadcast = (' Broadcast: {}.{}.{}.{}'.format(broadcast_octetos[0], broadcast_octetos[1], broadcast_octetos[2], broadcast_octetos[3]))

                                match posicao:
                                    case 3:
                                        firsthost_octetos[posicao] = jumps[j] + 1
                                        firsthost = (' Firsthost: {}.{}.{}.{}'.format(firsthost_octetos[0], firsthost_octetos[1], firsthost_octetos[2], firsthost_octetos[3]))
                                    case _:
                                        firsthost_octetos[posicao] = jumps[j]
                                        firsthost = (' Firsthost: {}.{}.{}.{}'.format(firsthost_octetos[0], firsthost_octetos[1], firsthost_octetos[2], firsthost_octetos[3]))

                                match posicao:
                                    case 3:
                                        lasthost_octetos[posicao] = jumps2[j] - 2
                                        lasthost = (' Lasthost: {}.{}.{}.{}'.format(lasthost_octetos[0], lasthost_octetos[1], lasthost_octetos[2], lasthost_octetos[3]))
                                    case _:
                                        lasthost_octetos[posicao] = jumps2[j] - 1
                                        lasthost = (' Lasthost: {}.{}.{}.{}'.format(lasthost_octetos[0], lasthost_octetos[1], lasthost_octetos[2], lasthost_octetos[3]))
                        else:
                            if ip[posicao] >= jumps[j]:
                                ip[posicao] = jumps[j]
                                network = ('\nNetwork: {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], ip[3]))

                                ip[posicao] = jumps[j] - 1
                                broadcast_octetos[posicao] = 255
                                broadcast = (' Broadcast: {}.{}.{}.{}'.format(broadcast_octetos[0], broadcast_octetos[1], broadcast_octetos[2], broadcast_octetos[3]))

                                match posicao:
                                    case 3:
                                        firsthost_octetos[posicao] = jumps[j] + 1
                                        firsthost = (' Firsthost: {}.{}.{}.{}'.format(firsthost_octetos[0], firsthost_octetos[1], firsthost_octetos[2], firsthost_octetos[3]))
                                    case _:
                                        firsthost_octetos[posicao] = jumps[j]
                                        firsthost = (' Firsthost: {}.{}.{}.{}'.format(firsthost_octetos[0], firsthost_octetos[1], firsthost_octetos[2], firsthost_octetos[3]))

                                match posicao:
                                    case 3:
                                        lasthost_octetos[posicao] = 254
                                        lasthost = (' Lasthost: {}.{}.{}.{}'.format(lasthost_octetos[0], lasthost_octetos[1], lasthost_octetos[2], lasthost_octetos[3]))
                                    case _:
                                        lasthost_octetos[posicao] = 255
                                        lasthost = (' Lasthost: {}.{}.{}.{}'.format(lasthost_octetos[0], lasthost_octetos[1], lasthost_octetos[2], lasthost_octetos[3]))

                    netmask = (f'\nNetmask: {net_mask[0]}.{net_mask[1]}.{net_mask[2]}.{net_mask[3]} = {net_mask[4]}')
                    subnets = ('\nSubnets:')
                    subnets_valores = ft.Column(
                        height=200,
                        width=250,
                        scroll=ft.ScrollMode.ALWAYS
                    )
                    subnets_valores_lista = []

                    for jump in range(0, range_lista[0], range_lista[1]):
                        ip[posicao] = jump
                        subnets_valores.controls.append(ft.Text(' {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], ip[3])))

                    hosts_net = ('\nHosts/Net: {}'.format(hostsnet))
                case False:
                    address = f'Address: {ip[0]}.{ip[1]}.{ip[2]}.{ip[3]} | {classe}'
                    network = f'\nNetwork: {predef_mascara_info[0]}'
                    broadcast = f' Broadcast: {predef_mascara_info[1]}'
                    firsthost = f' Firsthost: {predef_mascara_info[2]}'
                    lasthost = f' Lasthost: {predef_mascara_info[3]}'
                    netmask = f'\nNetmask: {net_mask[0]}.{net_mask[1]}.{net_mask[2]}.{net_mask[3]} = {net_mask[4]}'
                    hosts_net = f'\nHosts_net: {predef_mascara_info[4]}'
                    subnets = f'\nSubnets: {predef_mascara_info[5]}'
                    subnets_valores = ft.Row()

            info_envio(address, network, broadcast, firsthost, lasthost, netmask, hosts_net, subnets, subnets_valores)

        page.remove(*page.controls)
        global net_mask
        match mascara:
            case 8:
                calcular = bool(0)
                net_mask = '255.0.0.0 = 8'
                predef_mascara_info = [f'{ip[0]}.{0}.{0}.{0}', f'{ip[0]}.{255}.{255}.{255}', f'{ip[0]}.{0}.{0}.{1}', f'{ip[0]}.{255}.{255}.{254}', f'{2**24 - 2}', f'{ip[0]}.{0}.{0}.{0}']
                calculo_ip(None, None, net_mask, None, calcular, predef_mascara_info)
            case 9:
                calcular = bool(1)
                range_lista = [129, 128]
                octetos = [0, 1, 254, 255]
                net_mask = [255,128,0,0,9]
                hostsnet = (2 ** 23 - 2)
                calculo_ip(range_lista, octetos, net_mask, hostsnet, calcular, None)
            case 10:
                calcular = bool(1)
                range_lista = [193, 64]
                octetos = [0, 1, 254, 255]
                net_mask = [255,192,0,0,10]
                hostsnet = (2 ** 22 - 2)
                calculo_ip(range_lista, octetos, net_mask, hostsnet, calcular, None)
            case 11:
                calcular = bool(1)
                range_lista = [225, 32]
                octetos = [0, 1, 254, 255]
                net_mask = [255,224,0,0,11]
                hostsnet = (2 ** 21 - 2)
                calculo_ip(range_lista, octetos, net_mask, hostsnet, calcular, None)
            case 12:
                calcular = bool(1)
                range_lista = [241, 16]
                octetos = [0, 1, 254, 255]
                net_mask = [255,240,0,0,12]
                hostsnet = (2 ** 20 - 2)
                calculo_ip(range_lista, octetos, net_mask, hostsnet, calcular, None)
            case 13:
                calcular = bool(1)
                range_lista = [249, 8]
                octetos = [0, 1, 254, 255]
                net_mask = [255,248,0,0,13]
                hostsnet = (2 ** 19 - 2)
                calculo_ip(range_lista, octetos, net_mask, hostsnet, calcular, None)
            case 14:
                calcular = bool(1)
                range_lista = [253, 4]
                octetos = [0, 1, 254, 255]
                net_mask = [255,252,0,0,14]
                hostsnet = (2 ** 18 - 2)
                calculo_ip(range_lista, octetos, net_mask, hostsnet, calcular, None)
            case 15:
                calcular = bool(1)
                range_lista = [255, 2]
                octetos = [0, 1, 254, 255]
                net_mask = [255,254,0,0,15]
                hostsnet = (2 ** 17 - 2) 
                calculo_ip(range_lista, octetos, net_mask, hostsnet, calcular, None)
            case 16:
                calcular = bool(0)
                net_mask = '255.255.0.0 = 16'
                predef_mascara_info = [f'{ip[0]}.{ip[1]}.{0}.{0}', f'{ip[0]}.{ip[1]}.{255}.{255}', f'{ip[0]}.{ip[1]}.{0}.{1}', f'{ip[0]}.{ip[1]}.{255}.{254}', f'{2 ** 16 - 2}', f'{ip[0]}.{ip[1]}.{0}.{0}']
                calculo_ip(None, None, net_mask, None, calcular, predef_mascara_info)
            case 17:
                calcular = bool(1)
                range_lista = [129, 128]
                octetos = [0, 1, 254, 255]
                net_mask = [255,255,128,0,17]
                hostsnet = (2 ** 15 - 2)
                calculo_ip(range_lista, octetos, net_mask, hostsnet, calcular, None)
            case 18:
                calcular = bool(1)
                range_lista = [193, 64]
                octetos = [0, 1, 254, 255]
                net_mask = [255,255,192,0,18]
                hostsnet = (2 ** 14 - 2)
                calculo_ip(range_lista, octetos, net_mask, hostsnet, calcular, None)
            case 19:
                calcular = bool(1)
                range_lista = [225, 32]
                octetos = [0, 1, 254, 255]
                net_mask = [255,255,224,0,19]
                hostsnet = (2 ** 13 - 2)
                calculo_ip(range_lista, octetos, net_mask, hostsnet, calcular, None)
            case 20:
                calcular = bool(1)
                range_lista = [241, 16]
                octetos = [0, 1, 254, 255]
                net_mask = [255,255,240,0,20]
                hostsnet = (2 ** 12 - 2)
                calculo_ip(range_lista, octetos, net_mask, hostsnet, calcular, None)
            case 21:
                calcular = bool(1)
                range_lista = [249, 8]
                octetos = [0, 1, 254, 255]
                net_mask = [255,255,248,0,21]
                hostsnet = (2 ** 11 - 2) 
                calculo_ip(range_lista, octetos, net_mask, hostsnet, calcular, None)
            case 22:
                calcular = bool(1)
                range_lista = [253, 4]
                octetos = [0, 1, 254, 255]
                net_mask = [255,255,252,0,22]
                hostsnet = (2 ** 10 - 2)
                calculo_ip(range_lista, octetos, net_mask, hostsnet, calcular, None)
            case 23:
                calcular = bool(1)
                range_lista = [255, 2]
                octetos = [0, 1, 254, 255]
                net_mask = [255,255,254,0,23]
                hostsnet = (2 ** 9 - 2)
                calculo_ip(range_lista, octetos, net_mask, hostsnet, calcular, None)
            case 24:
                calcular = bool(0)
                net_mask = [255,255,255,0,24]
                predef_mascara_info = [f'{ip[0]}.{ip[1]}.{ip[2]}.{0}', f'{ip[0]}.{ip[1]}.{ip[2]}.{255}', f'{ip[0]}.{ip[1]}.{ip[2]}.{1}', f'{ip[0]}.{ip[1]}.{ip[2]}.{254}', f'{2**8 - 2}', f'{ip[0]}.{ip[1]}.{0}.{0}']
                calculo_ip(None, None, net_mask, None, calcular, predef_mascara_info)
            case 25:
                calcular = bool(1)
                range_lista = [129, 128]
                octetos = [0, 1, 254, 255]
                net_mask = [255,255,255,128,25]
                hostsnet = (2 ** 7 - 2)
                calculo_ip(range_lista, octetos, net_mask, hostsnet, calcular, None)
            case 26:
                calcular = bool(1)
                range_lista = [193, 64]
                octetos = [0, 1, 254, 255]
                net_mask = [255,255,255,192,26]
                hostsnet = (2 ** 6 - 2)
                calculo_ip(range_lista, octetos, net_mask, hostsnet, calcular, None)
            case 27:
                calcular = bool(1)
                range_lista = [225, 32]
                octetos = [0, 1, 254, 255]
                net_mask = [255,255,255,224,27]
                hostsnet = (2 ** 5 - 2)
                calculo_ip(range_lista, octetos, net_mask, hostsnet, calcular, None)
            case 28:
                calcular = bool(1)
                range_lista = [241, 16]
                octetos = [0, 1, 254, 255]
                net_mask = [255,255,255,241,28]
                hostsnet = (2 ** 4 - 2)
                calculo_ip(range_lista, octetos, net_mask, hostsnet, calcular, None)
            case 29:
                calcular = bool(1)
                range_lista = [249, 8]
                octetos = [0, 1, 254, 255]
                net_mask = [255,255,255,248,29]
                hostsnet = (2 ** 3 - 2)
                calculo_ip(range_lista, octetos, net_mask, hostsnet, calcular, None)
            case 30:
                calcular = bool(1)
                range_lista = [253, 4]
                octetos = [0, 1, 254, 255]
                net_mask = [255,255,255,252,30]
                hostsnet = (2 ** 2 - 2) 
                calculo_ip(range_lista, octetos, net_mask, hostsnet, calcular, None)
            case 31:
                calcular = bool(0)
                net_mask = [255,255,255,254,31]
                predef_mascara_info = [f'{ip[0]}.{ip[1]}.{ip[2]}.{ip[3]}', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A']
                calculo_ip(None, None, net_mask, None, calcular, predef_mascara_info)
            case 32:
                calcular = bool(0)
                net_mask = [255,255,255,255,32]
                predef_mascara_info = [f'{ip[0]}.{ip[1]}.{ip[2]}.{ip[3]}', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A']
                calculo_ip(None, None, net_mask, None, calcular, predef_mascara_info)

    def classificacao(lista_ip, mascara):
        classe = ''
        if lista_ip[0] >= 1 and lista_ip[0] < 10:
            classe = 'Class A - Public'
        elif lista_ip[0] > 10 and lista_ip[0] < 128:
            classe = 'Class A - Public'
        elif lista_ip[0] > 127 and lista_ip[0] < 172:
            classe = 'Class B - Public'
        elif lista_ip[0] == 172:
            if lista_ip[1] > 31:
                classe = 'Class B - Public'
            if lista_ip[1] > 15 and lista_ip[1] < 32:
                classe = 'Class B - Private'
        elif lista_ip[0] > 172 and lista_ip[0] < 192:
            classe = 'class B - Público'
        elif lista_ip[0] == 192:
            if lista_ip[1] == 168:
                classe = 'Class C - Private'
            else:
                classe = 'Class C - Public'
        elif lista_ip[0] > 192 and lista_ip[0] < 224:
            classe = 'Class C - Public'
        elif lista_ip[0] > 223 and lista_ip[0] < 240:
            classe = 'Class D - Public'
        elif lista_ip[0] > 239 and lista_ip[0] < 256:
            classe = 'Class E - Public'
        elif lista_ip[0] == 10:
            classe = 'Class A - Private'

        page.add(ft.Text(classe))
        informacoes(classe, lista_ip, mascara)

    def tratamento_ip(event):
        global lista_ip
        ip_entrada.value = (ip_entrada.value).split('.')

        lista_ip = ip_entrada.value

        mascara = lista_ip[3].split('/')
        lista_ip[3] = mascara[0]
        mascara.pop(0)
        mascara = int(mascara[0])
            
        for item in range(len(lista_ip)):
            lista_ip[item] = int(lista_ip[item])

        classificacao(lista_ip, mascara)
   
    ip_entrada = ft.TextField(
        label="Endereço Ip", hint_text='0.0.0.0/0',
        on_submit=tratamento_ip,
        max_length=18
        )

    page.title = "Calculadora IP"
    page.padding = 20
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    titulo = ft.Text('Calculadora IP', size=50, weight=ft.FontWeight.W_400, text_align=ft.TextAlign.END)
    enviar_botao = ft.ElevatedButton('Enviar',on_click=tratamento_ip)
    envio_info = ft.Row([ip_entrada, enviar_botao], alignment=ft.MainAxisAlignment.CENTER)

    page.add(titulo, envio_info)
    page.scroll = 'always'

ft.app(target=main)