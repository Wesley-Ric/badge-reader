# Leitor de crachás.
## Feito para ler pontos de almoço de crachás com leitor rfid e gerar relatórios.

O código feito tem como objetivo:
* ler o crachá sem a necessidade de um operador apertar a tecla enter.
* gerar um relatório com as seguintes informações.
    1. Código do crachá _número do crachá_.
    2. Qunatidade de refeições _no caso do almoço jantar e ceia sempre será 1_ servem para contabilizar no powerBY.
    3. Tipo:
        * Almoço.
        * Jantar.
        * Ceia.
    4. Data.
    5. Hora.

### Código do crachá.

Para captar o número ultilizei o sistema rfid, com um leitor e um crachá rfid, 
no código, porém precisava que o sistema reconhecesso o enter como um command
de um button, para isso ultilizei a seguinte linha de código: 

~~~python
txtBoxC.bind('<Return>', msg)
~~~

Onde o entry retorna seu valor para a função msg e é pego pela na linha 58 com o comando:

~~~python
txtBoxC.get()
~~~

### Data e hora.

#### Data.
Logo após isso o script pega a data do pc por meio da biblioteca datetime e a converte em string para ser gravada no arquivo .txt com os comandos:
~~~python
from datetime import date
data = str(date.today())
~~~

#### Hora.
A hora é pega por meio da biblioteca time em formato de string, formatada e atribuida a uma variavél.

~~~python
import time
hora = time.strftime("%H:%M:%S")
~~~

### Quantidade.
A quantidade é um valor fixo de um, usado apenas para somar os valores no banco de dados e no powerBY posteriormente.

### Tipo.
Os tipos são separados em 3 e testados por ifs, que testam o horario em que o cracha foi batido com o pegando o horario do registro com ` horario = str(datetime.now().time())` pega o horário do computador
e `horario = datetime.strptime(horario, '%H:%M:%S.%f')` que transforma o horario em um objeto, depois atribuimos os valores a serem testanos, no caso os horarios que são o almoço o jatar e a ceia:

~~~python
almoco = datetime.strptime('10:30:00.000000', '%H:%M:%S.%f')
almoco2 = datetime.strptime('14:00:00.000000', '%H:%M:%S.%f')
jantar = datetime.strptime('18:00:00.000000', '%H:%M:%S.%f')
jantar2 = datetime.strptime('20:59:59.000000', '%H:%M:%S.%f')
ceia = datetime.strptime('23:00:00.000000', '%H:%M:%S.%f')
ceia2 = datetime.strptime('23:59:59.000000', '%H:%M:%S.%f')
~~~

As variaveis recebem o valor do começo e do fim de cada intervalo.

## testes de ifs

Para testar as variaveis eu atribui o valor boleano a outra variavel e depois testei ela com o if da seguinte forma:

~~~python
testadorA = horario >= almoco and horario <= almoco2
testadorJ = horario >= jantar and horario <= jantar2
testadorC = horario >= ceia and horario <= ceia2
if testadorA == True:
elif testadorJ == True:
elif testadorC == True:
~~~

## Abre o arquivo e grava os dados nele:

~~~python
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
~~~

Depis temos o tratamento de erro com o else:
~~~python
else:    #exibe erro, se não atender aos requisitos dos ifs
    respStts["text"] = 'Erro!'
    respHora['text'] = 'Erro!'
    respData['text'] = 'Erro!'
    respReg.insert(1.0 ,'Registro feito fora do horário permitido!\n')
    jPri.after(1500 , clear_label)
    tkinter.messagebox.showinfo('Erro!' ,   'Registro feito fora do horário permitido!!\n'
                                            'Horários permitidos:\n'
                                            'Almoço das 10:30 às 14:00\n'
                                            'Jantar das 18:00 às 21:00\n'
                                            'Ceia das 21:00 às 00:00\n')
                    break
        txtBoxC.delete(0 , END) #apaga o valor do crachá
~~~

## Relatórios.

A segunda funcionalidade pega os arquivos txt gerados pelo programa, e gera um relatório com um command em um objeto button.
Podemos separar a funcionalidade dessa função em 5 etapas:
1. Cria a pasta de backup _se não existir_ e envia uma cópia do relatório para lá.
2. Cria uma pasta na área de trabalho chamada ´Relatórios´ _se não existir_ e envia uma cópia do arquivo para lá.
3. Envia o arquivo para a pasta do google drive com o modulo do google drive.
4. Envia o arquivo por email com o modulo email.
5. Apaga o arquivo que ficou na pasta inícial.

#### código:

~~~python
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
                respStts ['text']='Relatório gerado'

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
                os.remove('Relatorio.wes') #apaga o arquivo
                jPri.after(1000 , clear_label)
~~~
 
 ### Atualização 1.0
##### Problema:

o programa apresentava um bug, onde quando vc cadastrava um crachá fora do horario em que o programa permitia ele gerava o arquivo "Relatorio.wes" apenas com
o cabeçalho *header*, para corrigir o bug primeiro fechei todos os arquivos Relatorio.wes que estavam abertos, no caso eram três:

1.
~~~python
with open('Relatorio.wes' , 'a') as dados:
~~~
2.
~~~python
arq = open('Relatorio.wes' , 'r')
~~~
3.
~~~python
with open('Relatorio.wes' , 'a') as f:
~~~
#### Solução:
~~~python
with open('Relatorio.wes' , 'a') as f:
    f.write(header + "\n")  
    f.close()
    
else:    #exibe erro, se não atender aos requisitos dos ifs
    dados.close()
    arq.close()
~~~
logo após no caso else o script pega o tamnho do arquivo com o comando ´os.path.getsize("Relatorio.wes")´ que está apenas com o header dentro e testa:

~~~python
aberto = os.path.getsize('Relatorio.wes')  # atribui o tamanho do arquivo a variável
if aberto == 20:  # testa se está vazio pelo getsize
    os.remove('Relatorio.wes')
~~~
Assim apagando o arquivo depois de o cria-ló

##obrigado por ler sobre meu código, se possivel me siga e favorite meus commits <3
