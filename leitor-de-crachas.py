
#importação das bibliotecas
#importa o tkinter e as caixas de texto dele
from tkinter import *
import tkinter.messagebox

#import para testar a conecxão com a internet
import urllib.request

#importa as bibliotecas de data e hora
from datetime import datetime
from datetime import date
import time

#importa bibliotecas para criar, mover,apagar arquivos, tudo relacionado a sistema em geral
import shutil
import os
import subprocess
import getpass
import os.path
from tkinter import ttk


def teste_conexao():
    try:
        urllib.request.urlopen('http://google.com')         #retorna um valor verdadeiro ou falso para a função
        return True
    except:
        return False

if teste_conexao() == False:        #testa se a função é falsa
    tkinter.messagebox.showinfo('Erro!' , 'O computador está sem internet!\n'
                                              'Conecte-se a internet ou entre em contato com um técnico para resolver.')
else: #se verdadeira importa os modulos
    import ModuloGoogleDrive
    import modulo_email
#janela principal
    jPri = Tk()
    jPri.title('Leitor de pontos')
    jPri.geometry('1024x764+500+200')
    jPri['bg'] = "#d9d9d9"
    jPri.resizable(width=False, height=False)
    icone=PhotoImage(file='imgs/icon.png')
    jPri.iconphoto(False, icone)        #cria a janela principal

#função para pegar o valor do crachá e outros dados e os gravar em um arquivo
    def msg(name):
        valorduplicado = 0
        with open('Relatorio.wes' , 'a') as dados:    #cria o arquivo "Relatorio.wes"
            header = "cod,qtd,tipo,dt,hr"   #cria uma variavel para ser adcionada no arquivo
            arq = open('Relatorio.wes' , 'r')
            for line in arq :
                if header in line:  #testa se tem header nas linhas
                    break           #se header já estiver no arquivo ele da um break para não coloca-lá novamente
            else :
                with open('Relatorio.wes' , 'a') as f:
                    f.write(header + "\n")   #adciona um cabecalho(HEADER) no arquivo para ser lido e colocado no bd posteriormente
                    f.close()
            while txtBoxC.get() != valorduplicado:
                c = txtBoxC.get() #atribui o valor do input da caixa de texto a o c
                if c == valorduplicado:
                    break
                else:
                    data = str(date.today()) #pega a data de hoje
                    hora = time.strftime("%H:%M:%S") #pega o horário como string
                    qtd = str('1')
                    tipo1 = 'almoco'
                    tipo2 = 'jantar'
                    tipo3 = 'ceia'
                    horario = str(datetime.now().time()) #pega o horário do computador
                    horario = datetime.strptime(horario, '%H:%M:%S.%f')#transforma o horario em um objeto
#atribui um horario em fortato de objeto para as variáveis
                    almoco = datetime.strptime('10:30:00.000000', '%H:%M:%S.%f')
                    almoco2 = datetime.strptime('14:00:00.000000', '%H:%M:%S.%f')
                    jantar = datetime.strptime('18:00:00.000000', '%H:%M:%S.%f')
                    jantar2 = datetime.strptime('20:59:59.000000', '%H:%M:%S.%f')
                    ceia = datetime.strptime('23:00:00.000000', '%H:%M:%S.%f')
                    ceia2 = datetime.strptime('23:59:59.000000', '%H:%M:%S.%f')
#testa o horario relativo com a variável rotornando um valor boleano
                    testadorA = horario >= almoco and horario <= almoco2
                    testadorJ = horario >= jantar and horario <= jantar2
                    testadorC = horario >= ceia and horario <= ceia2
#testa se o resultado da variável e verdadeira
                    if testadorA == True:
                        crachas = c + ','   # acrescenta "," aos valores
                        qtds = qtd + ','
                        tipos1 = tipo1 + ','
                        datas = data + ','
                        horan = str(hora)
                        dados.writelines(crachas)   #escreve os dados no arquivo "relátorio.wes"
                        dados.writelines(qtds)
                        dados.writelines(tipos1)
                        dados.writelines(datas)
                        dados.writelines(horan + '\n')
                        respStts["text"] = 'Registrado'     #Exibe as mensagens nos labels
                        respHora['text'] = (hora)
                        respData['text'] = (data)
                        respReg.insert(1.0 ,f'O {tipo1} do cracha {c} foi registrado às {hora} no dia {data} \n')
                        jPri.after(700 , clear_label) #limpa os labels após X tempo,puxando a função "clear_label",  não sendo valido para o "resReg" pois é um txt
                    elif testadorJ == True:
                        crachas = c + ','
                        qtds = qtd + ','
                        tipos2 = tipo2 + ','
                        datas = data + ','
                        horan = str(hora)
                        dados.writelines(crachas)
                        dados.writelines(qtds)
                        dados.writelines(tipos2)
                        dados.writelines(datas)
                        dados.writelines(horan + '\n')
                        respStts["text"] = 'Registrado'
                        respHora['text'] = (hora)
                        respData['text'] = (data)
                        respReg.insert(1.0 ,f'O {tipo2} do cracha {c} foi registrado às {hora} no dia {data} \n')
                        jPri.after(700 , clear_label)
                    elif testadorC == True:
                        crachas = c + ','
                        qtds = qtd + ','
                        tipos3 = tipo3 + ','
                        datas = data + ','
                        horan = str(hora)
                        dados.writelines(crachas)
                        dados.writelines(qtds)
                        dados.writelines(tipos3)
                        dados.writelines(datas)
                        dados.writelines(horan + '\n')
                        respStts["text"] = 'Registrado'
                        respHora['text'] = (hora)
                        respData['text'] = (data)
                        respReg.insert(1.0 ,f'A {tipo3} do cracha {c} foi registrado às {hora} no dia {data} \n')
                        jPri.after(700 , clear_label)
                    else:    #exibe erro, se não atender aos requisitos dos ifs
                        dados.close()
                        arq.close()
                        respStts["text"] = 'Erro!'
                        respHora['text'] = 'Erro!'
                        respData['text'] = 'Erro!'
                        respReg.insert(1.0 ,'Registro feito fora do horário permitido!\n')
                        jPri.after(1500 , clear_label)
                        tkinter.messagebox.showinfo('Erro!' , 'Registro feito fora do horário permitido!!\n'
                                                              'Horários permitidos:\n'
                                                              'Almoço das 10:30 às 14:00\n'
                                                              'Jantar das 18:00 às 21:00\n'
                                                              'Ceia das 21:00 às 00:00\n')
                        aberto = os.path.getsize('Relatorio.wes')  # atribui o tamanho do arquivo a variável
                        if aberto == 20:  # testa se está vazio pelo getsize
                            os.remove('Relatorio.wes')
                            break  # se header já estiver no arquivo ele da um break para não coloca-lá novamente
                    break
        txtBoxC.delete(0 , END) #apaga o valor do crachá
    def progresso() :
        for x in range(10) :
            progressBr['value'] += 10
            jPri.update_idletasks()
            time.sleep(0.1)
#função para limpar os labels
    def clear_label():
        respStts['text'] = ''
        respData['text'] = ''
        respHora['text'] = ''

    #função para gerar a pasta backup e gerar uma pasta de relatorio na area de trabalho
    def relatoriobackup():
        if teste_conexao() == False : #testa a conexão com a internet quando o botão é acionado por meio do "teste_conexão()"
            tkinter.messagebox.showinfo('Erro!' , 'O computador está sem internet!\n'
                                                  'Conecte-se a internet ou entre em contato com um técnico para resolver.')
        else :
            pergunta = tkinter.messagebox.askyesno(title='Confirmar',
                                                   message='Tem certeza de que deseja gerar o relatório?')
                                                # pergunta se deseja gerar relatorio gerando um valor boleano e atribuindo ele a variavel
            if pergunta == True:
                relatorio = r'Relatorio.wes'
                existir = os.path.exists(relatorio)
                if not existir: #testa se o relatorio existe para gerar a pasta backup e demais
                    respStts["text"] = 'Erro!'
                    respHora['text'] = 'Erro!'
                    respData['text'] = 'Erro!'
                    respReg.insert(1.0 , 'O arquivo relatorio.wes não existe!\n')
                    jPri.after(1500 , clear_label)
                    tkinter.messagebox.showinfo('Erro!' , 'O arquivo relatorio.wes não existe!\n'
                                                         'Cadastre algum valor antes de gerar o relatorio.')
                else:

                    user = getpass.getuser() #pega o nome do user do computador
                    now=str(datetime.now())[:19]
                    now=now.replace(':','_')
                    pastaatual =r'Relatorio.wes'
                    if not os.path.exists('backup'):   #testa se a pasta backup existe e a cria se não existir#
                        subprocess.call(r'mkdir backup', shell=True)
                    destino=r'backup/RelatorioBackup_'+str(now)+'.wes'

                    pasta='C:/Users/'+user+'/Desktop/Relatorios'
                    existe=os.path.exists(pasta)
                    if not existe:
                        subprocess.call(r'mkdir Relatorios', shell=True)
                        diretoriomover = r'Relatorios'
                        destinomover = 'C:/Users/' + user + '/Desktop/'
                        shutil.move(diretoriomover , destinomover)
                        # cria e move a pasta Relatorios para o desktop
                    destino2='C:/Users/'+user+r'/Desktop/Relatorios/RelatorioBackup_'+str(now)+'.wes'
                    shutil.copy(pastaatual, destino)
                    shutil.copy(pastaatual,destino2)
                    ModuloGoogleDrive.google() #invoca a função do modulo, enviando os arquivos para o google drive
                    modulo_email.email()    #invoca a função do modulo enviando os arquivos para o email
                    progresso()
                    respStts ['text']='Relatório gerado'
                    tkinter.messagebox.showinfo('Sucesso!' , 'O relatório foi gerado com sucesso')
                    os.remove('Relatorio.wes') #apaga o arquivo
                    jPri.after(1000 , clear_label)





    #GUI
    frametitulo = Frame(jPri, bg='red')
    frametitulo.pack(side=TOP, fill=X)
    framecorpo = Frame(jPri, bg='#d9dee8')
    framecorpo.pack(fill=BOTH, expand=True)

    #==-label titulo==-
    lblTitulo = Label(frametitulo, text='Leitor de ponto de almoço e jantar', width=100, height=3)
    lblTitulo ['bg'] = '#00a0f5'
    lblTitulo ['font'] = 'Calibri 18'
    lblTitulo ['fg'] = '#ffffff'
    lblTitulo.pack(side=TOP, fill=X, ipady=10)
    #==-label cod e entry==-=-
    lblCod = Label(framecorpo, text='*')
    lblCod['bg']='#d9dee8'
    lblCod['font']='Calibri 20'
    lblCod['fg']='red'
    lblCod.place(x=30,y=45)

    lblCod2 = Label(framecorpo, text='Código do crachá:')
    lblCod2['bg']='#d9dee8'
    lblCod2['font']='Calibri 20'
    lblCod2['fg']='#0055be'
    lblCod2.place(x=50,y=45)

    #entry

    txtBoxC= Entry(framecorpo, width=20, relief='flat', highlightthickness=2)
    txtBoxC.config(highlightbackground='#0055be', highlightcolor='#0055be')
    txtBoxC['font']='Calibri 20'
    txtBoxC['fg']='#0055be'
    txtBoxC.bind('<Return>', msg)
    txtBoxC.focus_set()
    txtBoxC.place(x=30,y=100, height=40)
    #==-label stts e entry==-=-=-=-=-=-=

    lblStts = Label(framecorpo, text='*')
    lblStts['bg']='#d9dee8'
    lblStts['font']='Calibri 20'
    lblStts['fg']='red'
    lblStts.place(x=30,y=155)

    lblStts2 = Label(framecorpo, text='Status:')
    lblStts2['bg']='#d9dee8'
    lblStts2['font']='Calibri 20'
    lblStts2['fg']='#0055be'
    lblStts2.place(x=50,y=155)

    #entry

    respStts= Label(framecorpo, width=20, relief='flat', highlightthickness=2, bg='white', text='', anchor='w')
    respStts.config(highlightbackground='#0055be', highlightcolor='#0055be')
    respStts['font']='Calibri 20'
    respStts['fg']='#0055be'
    respStts.place(x=30,y=210, height=40)

    #===-=-=-=-=-=-=-=-labels horario e entry====-=-=-=-=-=-=-
    lblHr = Label(framecorpo, text='*')
    lblHr['bg']='#d9dee8'
    lblHr['font']='Calibri 20'
    lblHr['fg']='red'
    lblHr.place(x=370,y=155)

    lblHr2 = Label(framecorpo, text='Horário:')
    lblHr2['bg']='#d9dee8'
    lblHr2['font']='Calibri 20'
    lblHr2['fg']='#0055be'
    lblHr2.place(x=390,y=155)

    #entry

    respHora= Label(framecorpo, width=20, relief='flat', highlightthickness=2, bg='white', text='', anchor='w')
    respHora.config(highlightbackground='#0055be', highlightcolor='#0055be')
    respHora['font']='Calibri 20'
    respHora['fg']='#0055be'
    respHora.place(x=370,y=210, height=40)

    #=-=-=-=-labels data e entry=-=-=-=-=-=-=-=-
    lblData = Label(framecorpo, text='*')
    lblData['bg']='#d9dee8'
    lblData['font']='Calibri 20'
    lblData['fg']='red'
    lblData.place(x=685,y=155)

    lblData2 = Label(framecorpo, text='Data:')
    lblData2['bg']='#d9dee8'
    lblData2['font']='Calibri 20'
    lblData2['fg']='#0055be'
    lblData2.place(x=705,y=155)

    respData = Label(framecorpo, width=20, relief='flat', highlightthickness=2, bg='white', text='', anchor='w')
    respData.config(highlightbackground='#0055be', highlightcolor='#0055be')
    respData['font']='Calibri 20'
    respData['fg']='#0055be'
    respData.place(x=705,y=210, height=40)

    #=-=-=-=-labels registro e entry=-=-=-=-=-=-=-=-

    lblReg = Label(framecorpo, text='*')
    lblReg['bg']='#d9dee8'
    lblReg['font']='Calibri 20'
    lblReg['fg']='red'
    lblReg.place(x=30,y=265)

    lblReg2 = Label(framecorpo, text='Registros:')
    lblReg2['bg']='#d9dee8'
    lblReg2['font']='Calibri 20'
    lblReg2['fg']='#0055be'
    lblReg2.place(x=50,y=265)

    respReg = Text(framecorpo, width=65, height=6, relief='flat', highlightthickness=2, bg='white')
    respReg.config(highlightbackground='#0055be', highlightcolor='#0055be')
    respReg['font']='Calibri 14'
    respReg['fg']='#0055be'
    respReg.place(x=30, y=320)
    #-=-=-=-=-=-=-=botões=-=
    imgbtnGerar = PhotoImage(file='imgs/gerar.png')
    imgbtnSair = PhotoImage(file='imgs/sair.png')

    progressBr = ttk.Progressbar(framecorpo , orient=HORIZONTAL , length=800)
    progressBr.place(x=100, y=540, height=35)

    btnRel = Button(framecorpo, image=imgbtnGerar, borderwidth=0, bg='#d9dee8', activebackground='#d9dee8', command=relatoriobackup)
    btnRel.place(x=710, y=320)

    btnSair = Button(framecorpo, image=imgbtnSair, borderwidth=0, bg='#d9dee8', activebackground='#d9dee8', command=jPri.destroy)
    btnSair.place(x=710, y=395)



    jPri.mainloop()