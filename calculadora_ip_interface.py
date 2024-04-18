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
        def calculo_ip(range_lista, net_mask, hostsnet):
            global address, network, broadcast, firsthost, lasthost, netmask, hosts_net, subnets, subnets_valores
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
                        network = (f'\nNetwork: {ip[0]}.{ip[1]}.{ip[2]}.{ip[3]}')

                        ip[posicao] = jumps2[j] - 1
                        broadcast_octetos[posicao] = jumps2[j] - 1
                        broadcast = (f' Broadcast: {broadcast_octetos[0]}.{broadcast_octetos[1]}.{broadcast_octetos[2]}.{broadcast_octetos[3]}')

                        match posicao:
                            case 3:
                                firsthost_octetos[posicao] = jumps[j] + 1
                                firsthost = (f' Firsthost: {firsthost_octetos[0]}.{firsthost_octetos[1]}.{firsthost_octetos[2]}.{firsthost_octetos[3]}')
                            case _:
                                firsthost_octetos[posicao] = jumps[j]
                                firsthost = (f' Firsthost: {firsthost_octetos[0]}.{firsthost_octetos[1]}.{firsthost_octetos[2]}.{firsthost_octetos[3]}')

                        match posicao:
                            case 3:
                                lasthost_octetos[posicao] = jumps2[j] - 2
                                lasthost = (f' Lasthost: {lasthost_octetos[0]}.{lasthost_octetos[1]}.{lasthost_octetos[2]}.{lasthost_octetos[3]}')
                            case _:
                                lasthost_octetos[posicao] = jumps2[j] - 1
                                lasthost = (f' Lasthost: {lasthost_octetos[0]}.{lasthost_octetos[1]}.{lasthost_octetos[2]}.{lasthost_octetos[3]}')
                else:
                    if ip[posicao] >= jumps[j]:
                        ip[posicao] = jumps[j]
                        network = (f'\nNetwork: {ip[0]}.{ip[1]}.{ip[2]}.{ip[3]}')

                        ip[posicao] = jumps[j] - 1
                        broadcast_octetos[posicao] = 255
                        broadcast = (f' Broadcast: {broadcast_octetos[0]}.{broadcast_octetos[1]}.{broadcast_octetos[2]}.{broadcast_octetos[3]}')

                        match posicao:
                            case 3:
                                firsthost_octetos[posicao] = jumps[j] + 1
                                firsthost = (f' Firsthost: {firsthost_octetos[0]}.{firsthost_octetos[1]}.{firsthost_octetos[2]}.{firsthost_octetos[3]}')
                            case _:
                                firsthost_octetos[posicao] = jumps[j]
                                firsthost = (f' Firsthost: {firsthost_octetos[0]}.{firsthost_octetos[1]}.{firsthost_octetos[2]}.{firsthost_octetos[3]}')

                        match posicao:
                            case 3:
                                lasthost_octetos[posicao] = 254
                                lasthost = (f' Lasthost: {lasthost_octetos[0]}.{lasthost_octetos[1]}.{lasthost_octetos[2]}.{lasthost_octetos[3]}')
                            case _:
                                lasthost_octetos[posicao] = 255
                                lasthost = (f' Lasthost: {lasthost_octetos[0]}.{lasthost_octetos[1]}.{lasthost_octetos[2]}.{lasthost_octetos[3]}')

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

            info_envio(address, network, broadcast, firsthost, lasthost, netmask, hosts_net, subnets, subnets_valores)

        page.remove(*page.controls)
        global net_mask
        match mascara:
            case 8:
                range_lista = [255, 255]
                net_mask = [255,0,0,0,8]
                hostsnet = (2 ** 24 - 2)
                calculo_ip(range_lista, net_mask, hostsnet)
            case 9:
                range_lista = [129, 128]
                net_mask = [255,128,0,0,9]
                hostsnet = (2 ** 23 - 2)
                calculo_ip(range_lista, net_mask, hostsnet)
            case 10:
                range_lista = [193, 64]
                net_mask = [255,192,0,0,10]
                hostsnet = (2 ** 22 - 2)
                calculo_ip(range_lista, net_mask, hostsnet)
            case 11:
                range_lista = [225, 32]
                net_mask = [255,224,0,0,11]
                hostsnet = (2 ** 21 - 2)
                calculo_ip(range_lista, net_mask, hostsnet)
            case 12:
                range_lista = [241, 16]
                net_mask = [255,240,0,0,12]
                hostsnet = (2 ** 20 - 2)
                calculo_ip(range_lista, net_mask, hostsnet)
            case 13:
                range_lista = [249, 8]
                net_mask = [255,248,0,0,13]
                hostsnet = (2 ** 19 - 2)
                calculo_ip(range_lista, net_mask, hostsnet)
            case 14:
                range_lista = [253, 4]
                net_mask = [255,252,0,0,14]
                hostsnet = (2 ** 18 - 2)
                calculo_ip(range_lista, net_mask, hostsnet)
            case 15:
                range_lista = [255, 2]
                net_mask = [255,254,0,0,15]
                hostsnet = (2 ** 17 - 2) 
                calculo_ip(range_lista, net_mask, hostsnet)
            case 16:
                range_lista = [255, 255]
                net_mask = [255,255,0,0,16]
                hostsnet = (2 ** 16 - 2)
                calculo_ip(range_lista, net_mask, hostsnet)
            case 17:
                range_lista = [129, 128]
                net_mask = [255,255,128,0,17]
                hostsnet = (2 ** 15 - 2)
                calculo_ip(range_lista, net_mask, hostsnet)
            case 18:
                range_lista = [193, 64]
                net_mask = [255,255,192,0,18]
                hostsnet = (2 ** 14 - 2)
                calculo_ip(range_lista, net_mask, hostsnet)
            case 19:
                range_lista = [225, 32]
                net_mask = [255,255,224,0,19]
                hostsnet = (2 ** 13 - 2)
                calculo_ip(range_lista, net_mask, hostsnet)
            case 20:
                range_lista = [241, 16]
                net_mask = [255,255,240,0,20]
                hostsnet = (2 ** 12 - 2)
                calculo_ip(range_lista, net_mask, hostsnet)
            case 21:
                range_lista = [249, 8]
                net_mask = [255,255,248,0,21]
                hostsnet = (2 ** 11 - 2) 
                calculo_ip(range_lista, net_mask, hostsnet)
            case 22:
                range_lista = [253, 4]
                net_mask = [255,255,252,0,22]
                hostsnet = (2 ** 10 - 2)
                calculo_ip(range_lista, net_mask, hostsnet)
            case 23:
                range_lista = [255, 2]
                net_mask = [255,255,254,0,23]
                hostsnet = (2 ** 9 - 2)
                calculo_ip(range_lista, net_mask, hostsnet)
            case 24:
                range_lista = [255, 255]
                net_mask = [255,255,255,0,24]
                hostsnet = (2 ** 8 - 2)  
                calculo_ip(range_lista, net_mask, hostsnet)
            case 25:
                range_lista = [129, 128]
                net_mask = [255,255,255,128,25]
                hostsnet = (2 ** 7 - 2)
                calculo_ip(range_lista, net_mask, hostsnet)
            case 26:
                range_lista = [193, 64]
                net_mask = [255,255,255,192,26]
                hostsnet = (2 ** 6 - 2)
                calculo_ip(range_lista, net_mask, hostsnet)
            case 27:
                range_lista = [225, 32]
                net_mask = [255,255,255,224,27]
                hostsnet = (2 ** 5 - 2)
                calculo_ip(range_lista, net_mask, hostsnet)
            case 28:
                range_lista = [241, 16]
                net_mask = [255,255,255,241,28]
                hostsnet = (2 ** 4 - 2)
                calculo_ip(range_lista, net_mask, hostsnet)
            case 29:
                range_lista = [249, 8]
                net_mask = [255,255,255,248,29]
                hostsnet = (2 ** 3 - 2)
                calculo_ip(range_lista, net_mask, hostsnet)
            case 30:
                range_lista = [253, 4]
                net_mask = [255,255,255,252,30]
                hostsnet = (2 ** 2 - 2)
                calculo_ip(range_lista, net_mask, hostsnet)
            case _:
                abrir_popup(None)
                
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
        
    def cancelar_popup(event):
        popup_enderecoinv.open = False
        page.remove(*page.controls)
        page.add(titulo, envio_info)
        page.update()

    botao_cancelar_popup = ft.ElevatedButton('Ok', on_click=cancelar_popup, width=180)
    popup_enderecoinv = ft.AlertDialog( 
        modal= True,
        open= False,
        title= ft.Text("ERRO!", text_align=ft.TextAlign.CENTER),
        content= ft.Text("Endereço IP inválido!\nO endereço IP deve seguir junto a sua mascara, o formato '0.0.0.0/24' com \nvalores de octetos e mascaras válidos"),
        actions= [botao_cancelar_popup], actions_alignment=ft.MainAxisAlignment.CENTER 
    )

    def abrir_popup(event):
        page.dialog = popup_enderecoinv
        popup_enderecoinv.open = True
        ip_entrada.value = ''
        page.remove(*page.controls)
        page.update()

    def tratamento_ip(event):
        global lista_ip
        ip_entrada.value = (ip_entrada.value).split('.')

        lista_ip = ip_entrada.value

        while True:
            try:
                mascara = lista_ip[3].split('/')
                lista_ip[3] = mascara[0]
                mascara.pop(0)
                mascara = int(mascara[0])
                break
            except IndexError:
                ip_entrada.value = ''
                lista_ip = ''
                mascara = 0
                abrir_popup(event)
                break
            
        if lista_ip == '':
            abrir_popup(event)
        else:
            for item in range(len(lista_ip)):
                lista_ip[item] = int(lista_ip[item])

        ordem = 0
        acertos = 0
        for octeto in lista_ip:
            ordem += 1
            match ordem:
                case 1:
                    if octeto > 0 and octeto < 256:
                        acertos += 1
                        continue
                    else:
                        abrir_popup(event)
                        break
                case 2:
                    if octeto >= 0 and octeto < 256:
                        acertos += 1
                        continue
                    else:
                        abrir_popup(event)
                        break
                case 3:
                    if octeto >= 0 and octeto < 256:
                        acertos += 1
                        continue
                    else:
                        abrir_popup(event)
                        break
                case 4:
                    if octeto >= 0 and octeto < 256:
                        acertos += 1
                        continue
                    else:
                        abrir_popup(event)
                        break

        if acertos == 4:
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
