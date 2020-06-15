from telethon import TelegramClient, events, sync
from tkinter import *
import tkinter
import time
import asyncio
import wckToolTips
from PIL import ImageTk, Image

# DEFINITIONS
HEIGHT = 300
WIDTH = 750

root = Tk()
root.title("M.E. Consultas")
# root.iconbitmap('ME.png')

canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# MAIN FRAMES
logo_img = ImageTk.PhotoImage(Image.open("ME.png"))
frame_logo = Label(root, image=logo_img)
frame_logo.place(relx=0.5, rely=0.02, height=80, width=350, anchor='n')

# frame_user = Frame(root, borderwidth=2, relief="groove")
# frame_user.place(x=72, rely=0.02, height=135, width=130, anchor='n')

frame_cpf = Frame(root, borderwidth=2, relief="groove")
frame_cpf.place(relx=0.5, rely=0.3, height=35, width=250, anchor='n')

frame_nome = Frame(root, borderwidth=2, relief="groove")
frame_nome.place(relx=0.5, rely=0.425, height=25, width=300, anchor='n')

frame_semafaro = Frame(root)
frame_semafaro.place(relx=0.715, rely=0.425, height=25, width=25, anchor='n')

frame_top_infos = Frame(root)
frame_top_infos.place(relx=0.5, rely=0.52, height=20, relwidth=1, anchor='n')

frame_infos = Frame(root)
frame_infos.place(relx=0.5, rely=0.60, height=115, relwidth=0.99, anchor='n')

# INFOS COLUMNS
frame_idade = Frame(frame_infos)
frame_idade.columnconfigure(0, weight=1)
frame_idade.place(relx=0.024, height=120, relwidth=0.05, anchor='n')

frame_nbenef = Frame(frame_infos)
frame_nbenef.columnconfigure(0, weight=1)
frame_nbenef.place(relx=0.0784, height=120, relwidth=0.0585, anchor='n')

frame_salario = Frame(frame_infos)
frame_salario.columnconfigure(0, weight=1)
frame_salario.place(relx=0.1508, height=120, relwidth=0.085, anchor='n')

# frame_data = Frame(frame_infos, bg='blue')
# frame_data.columnconfigure(0, weight=1)
# frame_data.place(relx=0.213, height=120, relwidth=0.068, anchor='n')

frame_cidade = Frame(frame_infos)
frame_cidade.columnconfigure(0, weight=1)
frame_cidade.place(relx=0.26, height=120, relwidth=0.13, anchor='n')

frame_bancos = Frame(frame_infos)
frame_bancos.columnconfigure(0, weight=1)
frame_bancos.place(relx=0.4926, height=120, relwidth=0.332, anchor='n')

frame_qnt = Frame(frame_infos)
frame_qnt.columnconfigure(0, weight=1)
frame_qnt.place(relx=0.682, height=120, relwidth=0.0475, anchor='n')

frame_card = Frame(frame_infos)
frame_card.columnconfigure(0, weight=1)
frame_card.place(relx=0.755, height=120, relwidth=0.096, anchor='n')

frame_mgconsig = Frame(frame_infos)
frame_mgconsig.columnconfigure(0, weight=1)
frame_mgconsig.place(relx=0.8515, height=120, relwidth=0.097, anchor='n')

frame_mgcard = Frame(frame_infos)
frame_mgcard.columnconfigure(0, weight=1)
frame_mgcard.place(relx=0.949, height=120, relwidth=0.0975, anchor='n')

# MAIN CELLS
nome_cell = Label(frame_nome, text='NOME:')
nome_cell.grid(row=0, column=0)

idade_cell = Label(frame_top_infos, text='IDADE', borderwidth=2, relief="groove")
idade_cell.place(relx=0.056, y=10, relwidth=0.05, anchor='e')

nbenef_cell = Label(frame_top_infos, text='BENEF.', borderwidth=2, relief="groove")
nbenef_cell.place(relx=0.114, y=10, relwidth=0.06, anchor='e')

salario_cell = Label(frame_top_infos, text='SALÁRIO', borderwidth=2, relief="groove")
salario_cell.place(relx=0.198, y=10, relwidth=0.085, anchor='e')

# data_cell = Label(frame_top_infos, text='DATA', borderwidth=2, relief="groove")
# data_cell.place(relx=0.255, y=10, relwidth=0.0725, anchor='e')

cidade_cell = Label(frame_top_infos, text='AGENCIA', borderwidth=2, relief="groove")
cidade_cell.place(relx=0.329, y=10, relwidth=0.131, anchor='e')

bancos_cell = Label(frame_top_infos, text='BANCOS', borderwidth=2, relief="groove")
bancos_cell.place(relx=0.659, y=10, relwidth=0.331, anchor='e')

qnt_cell = Label(frame_top_infos, text='QNT.', borderwidth=2, relief="groove")
qnt_cell.place(relx=0.708, y=10, relwidth=0.05, anchor='e')

bcard_cell = Label(frame_top_infos, text='CARD', borderwidth=2, relief="groove")
bcard_cell.place(relx=0.805, y=10, relwidth=0.1, anchor='e')

mgconsig_cell = Label(frame_top_infos, text='MG. CONSIG', borderwidth=2, relief="groove")
mgconsig_cell.place(relx=0.9, y=10, relwidth=0.1, anchor='e')

mgcard_cell = Label(frame_top_infos, text='MG. CARD', borderwidth=2, relief="groove")
mgcard_cell.place(relx=0.996, y=10, relwidth=0.1, anchor='e')

# # USER ENTRY
# user = Label(frame_user, text='Usuário:')
# user.place(relx=0.2, rely=0.02, anchor='n', height=20, width=45)
#
# user_entry = Entry(frame_user)
# user_entry.place(relx=0.68, rely=0.02, anchor='n', height=18, width=75)
#
# passw = Label(frame_user, text='Senha:')
# passw.place(relx=0.180, rely=0.17, anchor='n', height=20, width=40)
#
# passw_entry = Entry(frame_user, show="*")
# passw_entry.place(relx=0.68, rely=0.18, anchor='n', height=18, width=75)

# CLIENTE CODE ENTRY
cpf_entry = Entry(frame_cpf)
cpf_entry.place(relx=0.01, rely=0.03, height=26, width=170)

# TELEGRAM SETUP
api_id = 1311637
api_hash = '149718fbbd581b34c98c8a214b997222'

client = TelegramClient('session_name', api_id, api_hash)
client.start()


def send_telegram():
    # CLEAN PREVIOUS SEARCHES
    for widget in frame_idade.winfo_children():
        widget.destroy()

    for widget in frame_nbenef.winfo_children():
        widget.destroy()

    for widget in frame_salario.winfo_children():
        widget.destroy()

    # for widget in frame_data.winfo_children():
    #     widget.destroy()

    for widget in frame_cidade.winfo_children():
        widget.destroy()

    for widget in frame_bancos.winfo_children():
        widget.destroy()

    for widget in frame_qnt.winfo_children():
        widget.destroy()

    for widget in frame_card.winfo_children():
        widget.destroy()

    for widget in frame_mgconsig.winfo_children():
        widget.destroy()

    for widget in frame_mgcard.winfo_children():
        widget.destroy()

    cpf = cpf_entry.get()
    consulta = client.send_message('ConsignadoBot', cpf)
    while consulta.out is not True:
        time.sleep(1)
    file = open("respostas.txt", "r")
    resposta_file = file.readlines()
    file.close()

    print(resposta_file)

    i = 0
    for l in resposta_file:
        if 'VERMELHO' in l:
            update = 'VERMELHO'
            vermelho = Label(frame_semafaro, bg="red")
            vermelho.place(height=25, width=25)
        if 'AMARELO' in l:
            update = 'AMARELO'
            amarelo = Label(frame_semafaro, bg="yellow")
            vermelho.place(height=25, width=25)
        if 'VERDE' in l:
            update = 'VERDE'
            verde = Label(frame_semafaro, bg="green")
            verde.place(height=25, width=25)
        if 'NOME:' in l:
            nome = re.search(r'NOME:(.*)', l).group(1)
            nome_plc = Label(frame_nome, text=nome)
            nome_plc.grid(row=0, column=1, sticky=EW)

        elif 'IDADE:' in l:
            split = l.split(' // ')
            age = re.search('IDADE:(.*)', split[0]).group(1)
            idade = int(age)
            cidade = re.search('CIDADE:(.*)', split[1]).group(1)
            beneficio = re.search('BENEFÍCIO:(.*)', split[2]).group(1)
            salario = re.search('SALÁRIO:(.*)', split[3]).group(1)
            bancos = re.search('BANCOS:(.*)', split[4]).group(1)
            quantidade = re.search('QNT:(.*)', split[5]).group(1)
            qnt = int(quantidade)
            card = re.search('CARTÃO:(.*)', split[6]).group(1)
            mg_consig = re.search('MG. CONSIG:(.*)', split[7]).group(1)
            mg_card = re.search('MG. CARD:(.*)', split[8]).group(1)

            if idade < 75:
                idade_plc = Label(frame_idade, text=idade, borderwidth=1, relief="groove")
                idade_plc.grid(row=i + 1, column=0, sticky=EW)
            elif idade > 75:
                idade_plc = Label(frame_idade, text=idade, borderwidth=1, relief="groove", bg='red')
                idade_plc.grid(row=i + 1, column=0, sticky=EW)
            benef_plc = Label(frame_nbenef, text=beneficio, borderwidth=1, relief="groove")
            benef_plc.grid(row=i + 1, column=0, sticky=EW)
            agencia_plc = Label(frame_cidade, text=cidade, borderwidth=1, relief="groove")
            agencia_plc.grid(row=i + 1, column=0, sticky=EW)
            wckToolTips.register(agencia_plc, cidade)
            salario_plc = Label(frame_salario, text=salario, borderwidth=1, relief="groove")
            salario_plc.grid(row=i + 1, column=0, sticky=EW)
            wckToolTips.register(salario_plc, salario)
            bancos_plc = Label(frame_bancos, text=bancos, borderwidth=1, relief="groove")
            bancos_plc.grid(row=i + 1, column=0, sticky=EW)
            wckToolTips.register(bancos_plc, bancos)
            if qnt >= 9:
                qnt_plc = Label(frame_qnt, text=qnt, borderwidth=1, relief="groove", bg='red')
                qnt_plc.grid(row=i + 1, column=0, sticky=EW)
            elif qnt < 9:
                qnt_plc = Label(frame_qnt, text=qnt, borderwidth=1, relief="groove")
                qnt_plc.grid(row=i + 1, column=0, sticky=EW)
            card_plc = Label(frame_card, text=card, borderwidth=1, relief="groove")
            card_plc.grid(row=i + 1, column=0, sticky=EW)
            wckToolTips.register(card_plc, card)
            mgconsig_plc = Label(frame_mgconsig, text=mg_consig, borderwidth=1, relief="groove")
            mgconsig_plc.grid(row=i + 1, column=0, sticky=EW)
            mgcard_plc = Label(frame_mgcard, text=mg_card, borderwidth=1, relief="groove")
            mgcard_plc.grid(row=i + 1, column=0, sticky=EW)
            i += 1

    file = open("respostas.txt", 'w')
    file.write('')
    file.close()


cpf_btn = Button(frame_cpf, text='Consultar', command=send_telegram)
cpf_btn.place(relx=0.72, rely=0.055)


def main():
    try:

        while True:
            root.update()
            root.minsize(750, 300)
            root.maxsize(1920, 300)
    except KeyboardInterrupt:
        pass
    except tkinter.TclError as e:
        if 'application has been destroyed' not in e.args[0]:
            raise
    finally:
        client.disconnect()


client.loop.run_until_complete(main())
