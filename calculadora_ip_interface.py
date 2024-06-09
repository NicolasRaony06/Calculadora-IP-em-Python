import flet as ft
from fpdf import FPDF
from time import strftime, localtime, sleep

def main(page: ft.Page):
    def gerar_relatorio(event):
        relatorio = FPDF()
        relatorio.add_page()
        relatorio.set_font("Arial")

        enderecos_pdf = [address, network, broadcast, firsthost, lasthost, netmask, hosts_net, subnets]

        data_atual = strftime("%d/%m/%Y às %H:%M:%S", localtime())

        relatorio.set_font("Arial", "B", 20)

        relatorio.cell(200, 10, txt="Cálculadora IP - Relatório", ln=True, align='C')

        relatorio.set_font("Arial", "", 13)
        relatorio.set_xy(15, 30)        

        relatorio.multi_cell(0, 7, txt=f"Relatório do cálculo de ip do Endereço {lista_ip[0]}.{lista_ip[1]}.{lista_ip[2]}.{lista_ip[3]} de CDIR/Máscara {net_mask[0]}.{net_mask[1]}.{net_mask[2]}.{net_mask[3]} = {net_mask[4]}, registrado em {data_atual}. Os seguintes endereços abaixo, estão de acordo com o cálculo realizado:", align="J")

        relatorio.set_font("Arial", "B", 11)

        y_pdf = 55
        for info in enderecos_pdf:
            y_pdf += 10
            relatorio.text(20, y_pdf, info)

        for subnet in subnets_valores_lista:
            y_pdf += 7
            relatorio.text(20, y_pdf, subnet)

        verificado = True
        while True:
            if diretorio_pdf.value:              
                try:
                    relatorio.output(diretorio_pdf.value)
                    break
                except:
                    verificado = False
                    break
            else:
                verificado = False
                break   
        
        diretorio_pdf_popupinfo = diretorio_pdf.value
        diretorio_pdf.value = ''
        match verificado:
            case True:
                popup_relatorio.actions = []
                popup_relatorio.content = ft.Row([ft.Text(f"Relatório criado com Sucesso em:", size=15), ft.Text(f"{diretorio_pdf_popupinfo}", size=18,  weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER)])
                page.update()
                sleep(1.5)
                popup_relatorio.open = False
                page.update()
            case False:
                popup_relatorio.content = ft.Column([diretorio_pdf, ft.Text("Diretório Inválido!", size=15)], height=75)
                page.update()

    def cancelar_popup_relatorio(event):
        popup_relatorio.open = False
        page.update() 

    botao_gerar_relatorio = ft.ElevatedButton("Enviar", width=150, on_click=gerar_relatorio)
    botao_cancelar_popup_relatorio = ft.ElevatedButton("Cancelar", width=150, on_click=cancelar_popup_relatorio)
    diretorio_pdf = ft.TextField(label="Diretório Local", hint_text=f"Ex.: C:\\Desktop\\relatorio.pdf", width=500, on_submit=gerar_relatorio)
    popup_relatorio = ft.AlertDialog(
        modal=True,
        open=True,
        title= ft.Text('Gerar Relatório'),  
    )

    def abrir_popup_relatorio(event):
        page.dialog = popup_relatorio
        popup_relatorio.content = diretorio_pdf
        popup_relatorio.actions = [botao_gerar_relatorio, botao_cancelar_popup_relatorio]
        popup_relatorio.open = True
        page.update()

    botao_popup_relatorio = ft.ElevatedButton("Gerar Relatório",on_click = abrir_popup_relatorio)
    
    def info_envio(event):
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

            page.add(titulo, envio_info, centralizar_info, botao_popup_relatorio)

    def informacoes(classe, ip, mascara):
        ip_entrada.value = ''
        def calculo_ip(ip_info):
            global address, network, broadcast, firsthost, lasthost, netmask, hosts_net, subnets, subnets_valores, subnets_valores_lista, net_mask

            address = f'Address: {ip[0]}.{ip[1]}.{ip[2]}.{ip[3]} | {classe}'

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
                subnets_valores_lista.append('   {}.{}.{}.{}'.format(ip[0], ip[1], ip[2], ip[3]))

            hosts_net = ('\nHosts/Net: {}'.format(ip_info['hostsnet']))

            info_envio(None)

        page.remove(*page.controls)
        match mascara:
            case 8:
                ip_info = {'range_lista': [255, 255], 'net_mask': [255,0,0,0,8], 'hostsnet': (2 ** 24 - 2)}
                calculo_ip(ip_info)
            case 9:
                ip_info = {'range_lista': [129, 128], 'net_mask': [255,128,0,0,9], 'hostsnet': (2 ** 23 - 2)}
                calculo_ip(ip_info)
            case 10:
                ip_info = {'range_lista': [193, 64], 'net_mask': [255,192,0,0,10], 'hostsnet': (2 ** 22 - 2)}
                calculo_ip(ip_info)
            case 11:
                ip_info = {'range_lista': [225, 32], 'net_mask': [255,224,0,0,11], 'hostsnet': (2 ** 21 - 2)}
                calculo_ip(ip_info)
            case 12:
                ip_info = {'range_lista': [241, 16], 'net_mask': [255,240,0,0,12], 'hostsnet': (2 ** 20 - 2)}
                calculo_ip(ip_info)
            case 13:
                ip_info = {'range_lista': [249, 8], 'net_mask': [255,248,0,0,13], 'hostsnet': (2 ** 19 - 2)}
                calculo_ip(ip_info)
            case 14:
                ip_info = {'range_lista': [253, 4], 'net_mask': [255,252,0,0,14], 'hostsnet': (2 ** 18 - 2)}
                calculo_ip(ip_info)
            case 15:
                ip_info = {'range_lista': [255, 2], 'net_mask': [255,254,0,0,15], 'hostsnet': (2 ** 17 - 2) }
                calculo_ip(ip_info)
            case 16:
                ip_info = {'range_lista': [255, 255], 'net_mask': [255,255,0,0,16], 'hostsnet': (2 ** 16 - 2)}
                calculo_ip(ip_info)
            case 17:
                ip_info = {'range_lista': [129, 128], 'net_mask': [255,255,128,0,17], 'hostsnet': (2 ** 15 - 2)}
                calculo_ip(ip_info)
            case 18:
                ip_info = {'range_lista': [193, 64], 'net_mask': [255,255,192,0,18], 'hostsnet': (2 ** 14 - 2)}
                calculo_ip(ip_info)
            case 19:
                ip_info = {'range_lista': [225, 32], 'net_mask': [255,255,224,0,19], 'hostsnet': (2 ** 13 - 2)}
                calculo_ip(ip_info)
            case 20:
                ip_info = {'range_lista': [241, 16], 'net_mask': [255,255,240,0,20], 'hostsnet': (2 ** 12 - 2)}
                calculo_ip(ip_info)
            case 21:
                ip_info = {'range_lista': [249, 8], 'net_mask': [255,255,248,0,21], 'hostsnet': (2 ** 11 - 2)}
                calculo_ip(ip_info)
            case 22:
                ip_info = {'range_lista': [253, 4], 'net_mask': [255,255,252,0,22], 'hostsnet': (2 ** 10 - 2)}
                calculo_ip(ip_info)
            case 23:
                ip_info = {'range_lista': [255, 2], 'net_mask': [255,255,254,0,23], 'hostsnet': (2 ** 9 - 2)}
                calculo_ip(ip_info)
            case 24:
                ip_info = {'range_lista': [255, 255], 'net_mask': [255,255,255,0,24], 'hostsnet': (2 ** 8 - 2)}
                calculo_ip(ip_info)
            case 25:
                ip_info = {'range_lista': [129, 128], 'net_mask': [255,255,255,128,25], 'hostsnet': (2 ** 7 - 2)}
                calculo_ip(ip_info)
            case 26:
                ip_info = {'range_lista': [193, 64], 'net_mask': [255,255,255,192,26], 'hostsnet': (2 ** 6 - 2)}
                calculo_ip(ip_info)
            case 27:
                ip_info = {'range_lista': [225, 32], 'net_mask': [255,255,255,224,27], 'hostsnet': (2 ** 5 - 2)}
                calculo_ip(ip_info)
            case 28:
                ip_info = {'range_lista': [241, 16], 'net_mask': [255,255,255,241,28], 'hostsnet': (2 ** 4 - 2)}
                calculo_ip(ip_info)
            case 29:
                ip_info = {'range_lista': [249, 8], 'net_mask': [255,255,255,248,29], 'hostsnet': (2 ** 3 - 2)}
                calculo_ip(ip_info)
            case 30:
                ip_info = {'range_lista': [253, 4], 'net_mask': [255,255,255,252,30], 'hostsnet': (2 ** 2 - 2)}
                calculo_ip(ip_info)
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

        while True:
            try:
                ip_entrada.value = (ip_entrada.value).split('.')
                lista_ip = ip_entrada.value
                mascara = lista_ip[3].split('/')
                lista_ip[3] = mascara[0]
                mascara.pop(0)
                mascara = int(mascara[0])
                break
            except:
                ip_entrada.value = ''
                lista_ip = ''
                mascara = 0
                abrir_popup(event)
                break
            
        if lista_ip == '':
            abrir_popup(event)
        else:
            for item in range(len(lista_ip)):
                while True:
                    try:
                        lista_ip[item] = int(lista_ip[item])
                        break
                    except:
                        abrir_popup(event)
                        break

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
    
    def dark_light_mode(event):
        if theme_mode.value:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
        page.update()

    theme_mode = ft.Switch(
                adaptive=True,
                label="Modo de Tema",
                value=True,
                on_change= dark_light_mode
            )
    
    ip_entrada = ft.TextField(
        label="Endereço Ip", 
        hint_text='0.0.0.0/0',
        on_submit=tratamento_ip,
        max_length=18
        )

    page.title = "Calculadora IP"
    page.padding = 20
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    titulo = ft.Text('Calculadora IP', size=50, weight=ft.FontWeight.W_400, text_align=ft.TextAlign.END)
    enviar_botao = ft.ElevatedButton('Enviar',on_click=tratamento_ip)
    envio_info = ft.Row([ip_entrada, enviar_botao, theme_mode], alignment=ft.MainAxisAlignment.CENTER)

    page.add(titulo, envio_info)
    page.scroll = 'always'

ft.app(target=main)