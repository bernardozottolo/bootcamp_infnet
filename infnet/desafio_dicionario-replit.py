#Import
import os
import random

# Funções
def resp_binaria (variavel, cod1, ref_cod1, cod2, ref_cod2, texto):
    while (variavel.lower()!=cod1.lower() and variavel.upper()!=cod1.upper()) and (variavel.lower()!=cod2.lower() and variavel.upper()!=cod2.upper()):
        variavel = input(f'Código inválido!\n{texto}\n{cod1} --> {ref_cod1}\n{cod2} --> {ref_cod2}\n\nInsira o código: ')
        os.system('cls')
        if variavel == 'encerrar':
            continue
    return variavel

# Banco de dados inicial


dados_clientes = {'id_cliente': [], 'nome_cliente':[], 'idade_cliente':[], 'cpf_cliente':[], 'ids_albuns':[], 'total_da_venda':[], 'total_compras_cliente':[]}

estoque = {
'Rock': {
"ALB0001": {"artista": "AC/DC", "titulo": "Highway to Hell", "ano_lancamento": 1979, "preco": 24.99, "estoque": 50},
"ALB0002": {"artista": "Queen", "titulo": "A Night at the Opera", "ano_lancamento": 1975, "preco": 34.99, "estoque": 25},
"ALB0003": {"artista": "Led Zeppelin", "titulo": "IV", "ano_lancamento": 1971, "preco": 39.99, "estoque": 15},
"ALB0004": {"artista": "The Beatles", "titulo": "Abbey Road", "ano_lancamento": 1969, "preco": 27.99, "estoque": 40},
"ALB0005": {"artista": "Nirvana", "titulo": "Nevermind", "ano_lancamento": 1991, "preco": 19.99, "estoque": 30},
"ALB0006": {"artista": "Metallica", "titulo": "Master of Puppets", "ano_lancamento": 1986, "preco": 31.99, "estoque": 20},
"ALB0007": {"artista": "Guns N' Roses", "titulo": "Appetite for Destruction", "ano_lancamento": 1987, "preco": 24.99, "estoque": 10},
"ALB0008": {"artista": "The Rolling Stones", "titulo": "Exile on Main St.", "ano_lancamento": 1972, "preco": 26.99, "estoque": 35},
"ALB0009": {"artista": "David Bowie", "titulo": "The Rise and Fall of Ziggy Stardust and the Spiders from Mars", "ano_lancamento": 1972, "preco": 21.99, "estoque": 12},
"ALB0010": {"artista": "Radiohead", "titulo": "OK Computer", "ano_lancamento": 1997, "preco": 17.99, "estoque": 8},
"ALB0011": {"artista": "Pearl Jam", "titulo": "Ten", "ano_lancamento": 1991, "preco": 23.99, "estoque": 17},
"ALB0012": {"artista": "Red Hot Chili Peppers", "titulo": "Blood Sugar Sex Magik", "ano_lancamento": 1991, "preco": 28.99, "estoque": 6},
"ALB0013": {"artista": "The Doors", "titulo": "The Doors", "ano_lancamento": 1967, "preco": 25.99, "estoque": 23},
"ALB0014": {"artista": "Jimi Hendrix Experience", "titulo": "Are You Experienced", "ano_lancamento": 1967, "preco": 28.99, "estoque": 11},
"ALB0015": {"artista": "U2", "titulo": "The Joshua Tree", "ano_lancamento": 1987, "preco": 30.99, "estoque": 15},
},
'MPB': {
"ALB1001": {"artista": "Chico Buarque", "titulo": "Construção", "ano_lancamento": 1971, "preco": 29.99, "estoque": 50},
"ALB1002": {"artista": "Elis Regina", "titulo": "Elis & Tom", "ano_lancamento": 1974, "preco": 34.99, "estoque": 25},
"ALB1003": {"artista": "Caetano Veloso", "titulo": "Transa", "ano_lancamento": 1972, "preco": 39.99, "estoque": 15},
"ALB1004": {"artista": "Gilberto Gil", "titulo": "Refazenda", "ano_lancamento": 1975, "preco": 27.99, "estoque": 40},
"ALB1005": {"artista": "Milton Nascimento", "titulo": "Clube da Esquina", "ano_lancamento": 1972, "preco": 19.99, "estoque": 30},
"ALB1006": {"artista": "Maria Bethânia", "titulo": "Álibi", "ano_lancamento": 1978, "preco": 31.99, "estoque": 20},
"ALB1007": {"artista": "Tom Jobim", "titulo": "Wave", "ano_lancamento": 1967, "preco": 24.99, "estoque": 10},
"ALB1008": {"artista": "Tim Maia", "titulo": "Tim Maia", "ano_lancamento": 1970, "preco": 26.99, "estoque": 35},
"ALB1009": {"artista": "Gal Costa", "titulo": "Gal Costa", "ano_lancamento": 1969, "preco": 21.99, "estoque": 12},
"ALB1010": {"artista": "João Gilberto", "titulo": "Chega de Saudade", "ano_lancamento": 1959, "preco": 17.99, "estoque": 8},
"ALB1011": {"artista": "Adoniran Barbosa", "titulo": "Trem das Onze", "ano_lancamento": 1964, "preco": 23.99, "estoque": 17},
"ALB1012": {"artista": "Cartola", "titulo": "Cartola", "ano_lancamento": 1976, "preco": 28.99, "estoque": 6},
"ALB1013": {"artista": "Djavan", "titulo": "Luz", "ano_lancamento": 1982, "preco": 25.99, "estoque": 23},
"ALB1014": {"artista": "Gal Costa", "titulo": "Legal", "ano_lancamento": 1970, "preco": 28.99, "estoque": 11},
"ALB1015": {"artista": "Ivan Lins", "titulo": "Chama Acesa", "ano_lancamento": 1975, "preco": 19.99, "estoque": 18}
},
'Rap Internacional' : {
"ALB2001": {"artista": "Kendrick Lamar", "titulo": "good kid, m.A.A.d city", "ano_lancamento": 2012, "preco": 39.99, "estoque": 25},
"ALB2002": {"artista": "Nas", "titulo": "Illmatic", "ano_lancamento": 1994, "preco": 44.99, "estoque": 15},
"ALB2003": {"artista": "Eminem", "titulo": "The Slim Shady LP", "ano_lancamento": 1999, "preco": 29.99, "estoque": 30},
"ALB2004": {"artista": "Outkast", "titulo": "Aquemini", "ano_lancamento": 1998, "preco": 34.99, "estoque": 20},
"ALB2005": {"artista": "Jay-Z", "titulo": "The Blueprint", "ano_lancamento": 2001, "preco": 37.99, "estoque": 18},
"ALB2006": {"artista": "Kanye West", "titulo": "My Beautiful Dark Twisted Fantasy", "ano_lancamento": 2010, "preco": 42.99, "estoque": 22},
"ALB2007": {"artista": "Wu-Tang Clan", "titulo": "Enter the Wu-Tang (36 Chambers)", "ano_lancamento": 1993, "preco": 29.99, "estoque": 14},
"ALB2008": {"artista": "Dr. Dre", "titulo": "The Chronic", "ano_lancamento": 1992, "preco": 24.99, "estoque": 12},
"ALB2009": {"artista": "Notorious B.I.G.", "titulo": "Ready to Die", "ano_lancamento": 1994, "preco": 27.99, "estoque": 23},
"ALB2010": {"artista": "2Pac", "titulo": "All Eyez on Me", "ano_lancamento": 1996, "preco": 26.99, "estoque": 17},
"ALB2011": {"artista": "Run-DMC", "titulo": "Raising Hell", "ano_lancamento": 1986, "preco": 23.99, "estoque": 10},
"ALB2012": {"artista": "Beastie Boys", "titulo": "Licensed to Ill", "ano_lancamento": 1986, "preco": 19.99, "estoque": 5},
"ALB2013": {"artista": "Public Enemy", "titulo": "It Takes a Nation of Millions to Hold Us Back", "ano_lancamento": 1988, "preco": 22.99, "estoque": 8},
"ALB2014": {"artista": "Gang Starr", "titulo": "Moment of Truth", "ano_lancamento": 1998, "preco": 28.99, "estoque": 31},
"ALB2015": {"artista": "Snoop Dogg", "titulo": "Paid tha Cost to Be da Boss", "ano_lancamento": 2002, "preco": 26.99, "estoque": 28},
},
'Sertanejo': {
"ALB3001": {"artista": "Jorge & Mateus", "titulo": "Ou Some ou Soma", "ano_lancamento": 2015, "preco": 29.99, "estoque": 20},
"ALB3002": {"artista": "Gusttavo Lima", "titulo": "Embaixador", "ano_lancamento": 2018, "preco": 32.99, "estoque": 15},
"ALB3003": {"artista": "Maiara & Maraisa", "titulo": "Reflexo", "ano_lancamento": 2019, "preco": 27.99, "estoque": 18},
"ALB3004": {"artista": "Henrique & Juliano", "titulo": "Novas Histórias", "ano_lancamento": 2017, "preco": 24.99, "estoque": 25},
"ALB3005": {"artista": "Luan Santana", "titulo": "Viva", "ano_lancamento": 2019, "preco": 31.99, "estoque": 10},
"ALB3006": {"artista": "Marília Mendonça", "titulo": "Realidade", "ano_lancamento": 2017, "preco": 26.99, "estoque": 20},
"ALB3007": {"artista": "Zé Neto & Cristiano", "titulo": "Esquece o Mundo Lá Fora", "ano_lancamento": 2018, "preco": 28.99, "estoque": 22},
"ALB3008": {"artista": "Gustavo Mioto", "titulo": "Ao Vivo em Fortaleza", "ano_lancamento": 2020, "preco": 34.99, "estoque": 16},
"ALB3009": {"artista": "Jads & Jadson", "titulo": "Diamante Bruto", "ano_lancamento": 2019, "preco": 25.99, "estoque": 12},
"ALB3010": {"artista": "Michel Teló", "titulo": "Bem Sertanejo - O Show (Ao Vivo)", "ano_lancamento": 2017, "preco": 30.99, "estoque": 13},
"ALB3011": {"artista": "Munhoz & Mariano", "titulo": "Ao Vivo em Campo Grande - Vol. 2", "ano_lancamento": 2013, "preco": 22.99, "estoque": 8},
"ALB3012": {"artista": "César Menotti & Fabiano", "titulo": "Os Menotti no Som - Ao Vivo", "ano_lancamento": 2011, "preco": 21.99, "estoque": 5},
"ALB3013": {"artista": "Zezé Di Camargo & Luciano", "titulo": "Flores em Vida", "ano_lancamento": 2015, "preco": 28.99, "estoque": 22},
"ALB3014": {"artista": "Chitãozinho & Xororó", "titulo": "Tom de Sertão", "ano_lancamento": 2015, "preco": 21.99, "estoque": 26},
"ALB3015": {"artista": "Matheus & Kauan", "titulo": "Na Praia", "ano_lancamento": 2016, "preco": 23.99, "estoque": 20}
},
'Pop Internacional': {
"ALB4001": {"artista": "Adele", "titulo": "21", "ano_lancamento": 2011, "preco": 27.99, "estoque": 20},
"ALB4002": {"artista": "Ed Sheeran", "titulo": "x", "ano_lancamento": 2014, "preco": 24.99, "estoque": 15},
"ALB4003": {"artista": "Taylor Swift", "titulo": "1989", "ano_lancamento": 2014, "preco": 21.99, "estoque": 18},
"ALB4004": {"artista": "Lady Gaga", "titulo": "The Fame", "ano_lancamento": 2008, "preco": 19.99, "estoque": 25},
"ALB4005": {"artista": "Justin Bieber", "titulo": "Purpose", "ano_lancamento": 2015, "preco": 23.99, "estoque": 10},
"ALB4006": {"artista": "Ariana Grande", "titulo": "Dangerous Woman", "ano_lancamento": 2016, "preco": 22.99, "estoque": 20},
"ALB4007": {"artista": "Dua Lipa", "titulo": "Future Nostalgia", "ano_lancamento": 2020, "preco": 29.99, "estoque": 22},
"ALB4008": {"artista": "Katy Perry", "titulo": "Teenage Dream", "ano_lancamento": 2010, "preco": 18.99, "estoque": 16},
"ALB4009": {"artista": "Bruno Mars", "titulo": "24K Magic", "ano_lancamento": 2016, "preco": 26.99, "estoque": 12},
"ALB4010": {"artista": "One Direction", "titulo": "Made in the A.M.", "ano_lancamento": 2015, "preco": 20.99, "estoque": 13},
"ALB4011": {"artista": "Shawn Mendes", "titulo": "Illuminate", "ano_lancamento": 2016, "preco": 21.99, "estoque": 8},
"ALB4012": {"artista": "Charlie Puth", "titulo": "Voicenotes", "ano_lancamento": 2018, "preco": 24.99, "estoque": 5},
"ALB4013": {"artista": "Rihanna", "titulo": "Loud", "ano_lancamento": 2010, "preco": 18.99, "estoque": 17},
"ALB4014": {"artista": "The Weekend", "titulo": "Beauty Behind the Madness", "ano_lancamento": 2015, "preco": 23.99, "estoque": 11},
"ALB4015": {"artista": "Maroon 5", "titulo": "V", "ano_lancamento": 2014, "preco": 24.99, "estoque": 23}
}
}

# Declaração de variáveis gerais do sistema
sales_total = 0
maior_compra_geral = 0



######################################################### PROGRAMA #####################################################################
os.system('cls')
for i in dados_clientes:
    print(f'{i} = {dados_clientes[i]}')
input('Pressione enter para começar o programa\n')
os.system('cls')

# Declaração de variáveis diárias
sales_dia = 0
maior_compra_dia = 0
rpt = '1'

# --------------------------------------------------MENU INICIAL DO CLIENTE-------------------------------------------------------------------------------
while rpt.lower()=='1':
# Declaração de variáveis diárias
    cliente_ou_nao = input('Primeira vez por aqui?\n1 --> sim\n2 --> não\n9 --> Para encerrar\nInsira um código: ')
    os.system('cls')
    while (cliente_ou_nao!='1' and cliente_ou_nao!='2') and cliente_ou_nao!='9':
        cliente_ou_nao = input("Código inválido!\nJá é cliente da loja?\nS --> Sim\nN --> Não\n9 --> Para encerrar\nInsira um código: ")
        os.system('cls')
        if cliente_ou_nao == '9':
            break
    if cliente_ou_nao == '9':
        os.system('cls')
        break  



# --------------------------------------------------------CLIENTES NOVOS-----------------------------------------------------------------------------
    if cliente_ou_nao.lower() == '1':
        novo_cliente = input('Insira seu nome completo: ') #Inserindo o nome do cliente
        os.system('cls')
        if novo_cliente == 'cancelar': #caso tenha inserido a opção de cancelar
            continue
        idade = input("Insira sua idade: ") #Inserindo a idade do cliente
        
        #Verificando se a idade do cliente é válido:
        while idade.isnumeric() == False or int(idade) < 0:
            if idade == 'cancelar': #caso tenha inserido a opção de cancelar
                break
            elif idade.isnumeric() == False: #caso o valor informado não seja um número
                idade = input("Valor incorreto!\nInsira novamente sua idade: ")
            elif int(idade) < 0: #caso seja um número negativo
                idade = input("Iadade precisa ser um número inteiro e positivo!\nInsira novamente sua idade: ")
        if idade == 'cancelar': #caso tenha inserido a opção de cancelar
            os.system('cls')
            continue
        os.system('cls')
        # Para confirmar a idade do cliente
        confirmar = input(f"Idade: {idade} anos\nConfirma a idade inserida:\n'C' --> para confirmar\n'E' --> para editar a idade\n'R' --> para retornar para a tela inicial\n\nInsira o código: ")
        os.system('cls')
        while confirmar.lower() not in ['c','e','r']: #Protegendo de valores inválidos
            confirmar = input(f"Código inválido!\nCPF: {idade}\nConfirma a idade inserida:\n'C' --> para confirmar\n'E' --> para editar a idade\n'R' --> para retornar para a tela inicial\n\nInsira o código: ")
            os.system('cls')
        #Quando o cliente deseja editar a idade inserida e iniciando a entrada da idade novamente
        while confirmar.lower() == 'e':
            idade = input("Insira sua idade: ") #Inserindo o idade do cliente
            os.system('cls')
            #Verificando se a idade do cliente é válido:
            while idade.isnumeric() == False or int(idade) < 0:
                if idade == 'cancelar': #caso tenha inserido a opção de cancelar
                    break
                elif idade.isnumeric() == False: #caso o valor informado não seja um número
                    idade = input("Valor inválido!\nInsira novamente sua idade: ")
                elif int(idade) < 0 : #caso seja um valor negativo
                    idade = input("Idade precisa ser um número inteiro positivo!\nInsira novamente sua idade: ")
                if idade == 'cancelar': #caso tenha inserido a opção de cancelar
                    os.system('cls')
                    break
                os.system('cls')
            #Confirmando novamente o idade do cliente, porém já dentro do looping
            confirmar = input(f"Idade: {idade} anos\nConfirma a idade inserida:\n'C' --> para confirmar\n'E' --> para editar a idade\n'R' --> para retornar para a tela inicial\n\nInsira o código: ")
            os.system('cls')
            while confirmar.lower() not in ['c','e','r']:
                confirmar = input(f"Código inválido!\nCPF: {idade}\nConfirma a idade inserida:\n'C' --> para confirmar\n'E' --> para editar a idade\n'R' --> para retornar para a tela inicial\n\nInsira o código: ")            
                os.system('cls')
            if confirmar.lower() == 'r': #caso tenha inserido a opção de cancelar
                os.system('cls')
                break  
            if confirmar.lower() == 'r': #caso tenha inserido a opção de cancelar
                os.system('cls')
                break 
            if idade == 'cancelar': #caso tenha inserido a opção de cancelar
                os.system('cls')
                break

        if idade == 'cancelar': #caso tenha inserido a opção de cancelar
            os.system('cls')
            continue            
        if confirmar.lower() == 'r': #caso tenha inserido a opção de cancelar
            os.system('cls')
            continue   
        os.system('cls')    
        
        #Inserindo o CPF do cliente:
        cpf = input("Insira seu CPF (apenas números, sem '.' ou '-'): ") #Inserindo o CPF do cliente
        
        #Verificando se o CPF do cliente é válido:
        while (cpf.isnumeric() == False or (len(cpf) != 11 or int(cpf) < 0)) or (cpf in dados_clientes['cpf_cliente'] == True):
            if cpf == 'cancelar': #caso tenha inserido a opção de cancelar
                break
            elif cpf.isnumeric() == False: #caso o valor informado não seja um número
                cpf = input("Valor incorreto!\nInsira seu CPF (apenas números, sem '.' e '-'): ")
            elif int(cpf) < 0: #caso o valor informado não seja um número
                cpf = input("Valor não pode ser negativo!\nInsira seu CPF (apenas números, sem '.' e '-'): ")    
            elif len(cpf) != 11: #caso a quantidade de números do CPF não esteja correta
                cpf = input("CPF precisa conter 11 números!\nInsira seu CPF (apenas números, sem '.' e '-'): ")
            elif cpf in dados_clientes['cpf_clientes'] == True: #caso o cpf já esteja cadastrado no banco de dados dos clientes
                cpf = input("CPF já cadastrado! Se já for cliente e deseja entrar com seus dados, basta digitar 'cancelar' para voltar para o menu inicial de atendimento e digitar o código de que já é cliente!\nInsira seu CPF (apenas números, sem '.' e '-') ou digite 'cancelar': ")
        if cpf == 'cancelar': #caso tenha inserido a opção de cancelar
            os.system('cls')
            continue
        os.system('cls')
        # Para confirmar o CPF do cliente
        confirmar = input(f"CPF: {cpf}\nConfirma o CPF inserido:\n'C' --> para confirmar\n'E' --> para editar o CPF\n'R' --> para retornar para a tela inicial\n\nInsira o código: ")
        os.system('cls')
        while confirmar.lower() not in ['c','e','r']: #Protegendo de valores inválidos
            confirmar = input(f"Código inválido!\nCPF: {cpf}\nConfirma o CPF inserido:\n'C' --> para confirmar\n'E' --> para editar o CPF\n'R' --> para retornar para a tela inicial\n\nInsira o código: ")
            os.system('cls')
        #Quando o cliente deseja editar o CPF inserido e iniciando a entrada do CPF novamente
        while confirmar.lower() == 'e':
            cpf = input("Insira seu CPF (apenas números, sem '.' ou '-'): ") #Inserindo o CPF do cliente
            os.system('cls')
            #Verificando se o CPF do cliente é válido:
            while (cpf.isnumeric() == False or (len(cpf) != 11 or int(cpf) < 0)) or (cpf in dados_clientes['cpf_cliente'] == True):
                if cpf == 'cancelar': #caso tenha inserido a opção de cancelar
                    break
                elif cpf.isnumeric() == False: #caso o valor informado não seja um número
                    cpf = input("Valor incorreto!\nInsira seu CPF (apenas números, sem '.' e '-'): ")
                elif int(cpf) < 0: #caso o valor informado não seja um número
                    cpf = input("Valor não pode ser negativo!\nInsira seu CPF (apenas números, sem '.' e '-'): ") 
                elif len(cpf) != 11: #caso a quantidade de números do CPF não esteja correta
                    cpf = input("CPF precisa conter 11 números!\nInsira seu CPF (apenas números, sem '.' e '-'): ")
                elif cpf in dados_clientes['cpf_clientes'] == True: #caso o cpf já esteja cadastrado no banco de dados dos clientes
                    cpf = input("CPF já cadastrado! Se já for cliente e deseja entrar com seus dados, basta digitar 'cancelar' para voltar para o menu inicial de atendimento e digitar o código de que já é cliente!\nInsira seu CPF (apenas números, sem '.' e '-') ou digite 'cancelar': ")
                if cpf == 'cancelar': #caso tenha inserido a opção de cancelar
                    os.system('cls')
                    break
                os.system('cls')
                #Confirmando novamente o CPF do cliente, porém já dentro do looping
            confirmar = input(f"CPF: {cpf}\nConfirma o CPF inserido:\n'C' --> para confirmar\n'E' --> para editar o CPF\n'R' --> para retornar para a tela inicial\n\nInsira o código: ")
            os.system('cls')
            while confirmar.lower() not in ['c','e','r']:
                confirmar = input(f"Código inválido!\nCPF: {cpf}\nConfirma o CPF inserido:\n'C' --> para confirmar\n'E' --> para editar o CPF\n'R' --> para retornar para a tela inicial\n\nInsira o código: ")            
                os.system('cls')
            if confirmar.lower() == 'r': #caso tenha inserido a opção de cancelar
                os.system('cls')
                break 
            if cpf == 'cancelar': #caso tenha inserido a opção de cancelar
                os.system('cls')
                break

        if cpf == 'cancelar': #caso tenha inserido a opção de cancelar
            os.system('cls')
            continue            
        if confirmar.lower() == 'r': #caso tenha inserido a opção de cancelar
            os.system('cls')
            continue   
        os.system('cls')    
        #Para escolher o álbum
        album = 'r'
        while album.lower() == 'r':
            print('Insira o gênero que do álbum que deseja:')
            cod_generos={}
            num_generos=0
            for i in estoque:
                num_generos += 1
                cod_generos[num_generos] = i
                print(f"{num_generos} --> {i}")
            print('')
            genero = input('Insira o código: ')
            os.system('cls')
            while genero.isnumeric()==False or int(genero) not in cod_generos: # Para verificar se inseriu um código válido
                if genero == 'cancelar': #caso tenha inserido a opção de cancelar
                    break
                print('Código inválido!\nInsira um código válido para o gênero do álbum:')
                for i in cod_generos:
                    print(f'{cod_generos[i]} --> {i}')                    
                genero = input('Insira o código: ')
                os.system('cls')
            if genero == 'cancelar':#caso tenha inserido a opção de cancelar
                break
            os.system('cls')
            print(f'Gênero - {cod_generos[int(genero)]}:')
            #Irá imprimir o código de cada álbum juntamente com seu código
            print('Código - Artista - Título - Ano de lançamento - Preço\n')
            for i in estoque[cod_generos[int(genero)]]:
                print(f"{i}\n{estoque[cod_generos[int(genero)]][i]['artista']} - {estoque[cod_generos[int(genero)]][i]['titulo']} - {estoque[cod_generos[int(genero)]][i]['ano_lancamento']} - ${estoque[cod_generos[int(genero)]][i]['preco']:.2f}\n") #genero vai retornar o número da chave, que tem como valor o genêro desejado, chamando então 
            #Pedindo para o cliente inserir o código do álbum
            album = input("Insira o código do álbum que deseja, ou digite 'r' para retornar ao índice de gêneros dos álbums: ").upper()
            while album.upper() not in estoque[cod_generos[int(genero)]] and album.lower() != 'r': #proteção para valores inválidos
                os.system('cls')
                print(f'Gênero - {cod_generos[int(genero)]}:')
                #Irá imprimir o código de cada álbum juntamente com seu código
                print('Código - Artista - Título - Ano de lançamento - Preço\n')
                for i in estoque[cod_generos[int(genero)]]:
                    print(f"{i}\n{estoque[cod_generos[int(genero)]][i]['artista']} - {estoque[cod_generos[int(genero)]][i]['titulo']} - {estoque[cod_generos[int(genero)]][i]['ano_lancamento']} - ${estoque[cod_generos[int(genero)]][i]['preco']:.2f}\n") #genero vai retornar o número da chave, que tem como valor o genêro desejado, chamando então 
                album = input("Código inválido!\nInsira um código válido do álbum que deseja, ou digite 'r' para retornar ao índice de gêneros dos álbums: ").upper()
            os.system('cls')
            if album.lower() != 'r':
                os.system('cls')
                confirmar = input(f"Álbum selecionado:\n{album}\n{estoque[cod_generos[int(genero)]][album]['artista']} - {estoque[cod_generos[int(genero)]][album]['titulo']} - {estoque[cod_generos[int(genero)]][album]['ano_lancamento']} - ${estoque[cod_generos[int(genero)]][album]['preco']:.2f}\n'C' --> para confirmar\n'R' --> Para retornar para os gêneros\n\nInsira o código: ")   
            #Confirmação da compra
                while confirmar.lower() != 'c' and confirmar.lower()!='r':
                    confirmar = input(f"Código Inválido!\n\nÁlbum selecionado:\n{album}\n{estoque[cod_generos[int(genero)]][album]['artista']} - {estoque[cod_generos[int(genero)]][album]['titulo']} - {estoque[cod_generos[int(genero)]][album]['ano_lancamento']} - ${estoque[cod_generos[int(genero)]][album]['preco']:.2f}\n'C' --> para confirmar\n'R' --> Para retornar para os gêneros\n\nInsira o código: ")
                if confirmar.lower() == 'r':
                    album == 'r'
        album_list = [] #Criando uma lista de albuns comprado, para que seja uma lista de albuns para cada cliente
        album_list.append(album)
        dados_clientes['nome_cliente'].append(novo_cliente) #Adicionando o nome do cliente ao banco de dados
        dados_clientes['idade_cliente'].append(idade) #Adicionando a idade do cliente ao banco de dados
        dados_clientes['cpf_cliente'].append(cpf) #Adicionando o CPF do cliente ao banco de dados
        n = dados_clientes['nome_cliente'].index(novo_cliente) #pegando o index do cliente
        os.system('cls')
        print(f'Muito obrigado pela sua primeira compra conosco, {novo_cliente.split()[0]}! Sua Id da loja é {n} para realizar compras futuras, também podendo ser realizado login pelo seu CPF.\n')
        dados_clientes['id_cliente'].append(n) #Adicionando a id ao banco de dados - obs: leva o mesmo valor do index
        dados_clientes['total_compras_cliente'].append(1) #Adicionando um número com o número de vezes que o cliente fez uma compra na loja
        dados_clientes['ids_albuns'].append(album_list) #Adicionando a lista, com a primeira compra do cliente
        price = estoque[cod_generos[int(genero)]][album]['preco'] #Atribuindo a uma variável o preço da do álbum
        dados_clientes['total_da_venda'].append(float(price)) #Adiicionando o valor da venda, ao total de compras do cliente para compras futuras
        estoque[cod_generos[int(genero)]][album]['estoque'] -= 1 #Decrementando uma unidade no estoque do álbum
        sales_dia+=1 #Incrementando o número de vendas feitas
        if price > maior_compra_dia: # Pegando os dados da maior compra, caso seja o caso
            maior_compra_dia = float(price)
            maior_comprador = n

#--------------------------------------------------------CLIENTES ANTIGOS------------------------------------------------------------------------
    elif cliente_ou_nao.lower() == '2':
        old = input('\nInsira seu CPF ou sua Id: ')
        os.system('cls')
        if old == 'cancelar': #caso deseja retornar para a tela inicial
            os.system('cls')
            continue
        # proteção que analisa se a entrada consta no banco de dados
        while int(old) not in dados_clientes['id_cliente'] and old not in dados_clientes['cpf_cliente']:
            old = input("CPF ou Id incorretos! Tente novamente ou digite 'cancelar' para voltar para a entrada inicial: ")
            os.system('cls')
            if old == 'cancelar':
                break
        if old == 'cancelar':
            os.system('cls')
            continue
        #Verificando se a pessoa inseriu o CPF ou a sua Id da loja
        if len(old) < 11: #Se tiver menos que 11 caracteres, que é o tamanho do CPF, então o usuário entrou com a Id
            n = int(old)
        elif len(old) == 11: #Se tiver 11 caracteres, o usuário entrou com o CPF
            n = dados_clientes['cpf_cliente'].index(old)

        album = 'r'
        while album.lower() == 'r':
            print('Insira o gênero que do álbum que deseja:')
            cod_generos={}
            num_generos=0
            for i in estoque:
                num_generos += 1
                cod_generos[num_generos] = i
                print(f"{num_generos} --> {i}")
            print('')
            genero = input('Insira o código: ')
            os.system('cls')
            while genero.isnumeric()==False or int(genero) not in cod_generos: # Para verificar se inseriu um código válido
                if genero == 'cancelar': #caso tenha inserido a opção de cancelar
                    break
                print('Código inválido!\nInsira um código válido para o gênero do álbum:')
                for i in cod_generos:
                    print(f'{cod_generos[i]} --> {i}')                    
                genero = input('Insira o código: ')
                os.system('cls')
            if genero == 'cancelar':#caso tenha inserido a opção de cancelar
                break
            os.system('cls')
            print(f'Gênero - {cod_generos[int(genero)]}:')
            #Irá imprimir o código de cada álbum juntamente com seu código
            print('Código - Artista - Título - Ano de lançamento - Preço\n')
            for i in estoque[cod_generos[int(genero)]]:
                print(f"{i}\n{estoque[cod_generos[int(genero)]][i]['artista']} - {estoque[cod_generos[int(genero)]][i]['titulo']} - {estoque[cod_generos[int(genero)]][i]['ano_lancamento']} - ${estoque[cod_generos[int(genero)]][i]['preco']:.2f}\n") #genero vai retornar o número da chave, que tem como valor o genêro desejado, chamando então 
            #Pedindo para o cliente inserir o código do álbum
            album = input("Insira o código do álbum que deseja, ou digite 'r' para retornar ao índice de gêneros dos álbums: ").upper()
            while album.upper() not in estoque[cod_generos[int(genero)]] and album.lower() != 'r': #proteção para valores inválidos
                os.system('cls')
                print(f'Gênero - {cod_generos[int(genero)]}:')
                #Irá imprimir o código de cada álbum juntamente com seu código
                print('Código - Artista - Título - Ano de lançamento - Preço\n')
                for i in estoque[cod_generos[int(genero)]]:
                    print(f"{i}\n{estoque[cod_generos[int(genero)]][i]['artista']} - {estoque[cod_generos[int(genero)]][i]['titulo']} - {estoque[cod_generos[int(genero)]][i]['ano_lancamento']} - ${estoque[cod_generos[int(genero)]][i]['preco']:.2f}\n") #genero vai retornar o número da chave, que tem como valor o genêro desejado, chamando então 
                album = input("Código inválido!\nInsira um código válido do álbum que deseja, ou digite 'r' para retornar ao índice de gêneros dos álbums: ").upper()
            os.system('cls')
            confirmar = input(f"Álbum selecionado:\n{album}\n{estoque[cod_generos[int(genero)]][album]['artista']} - {estoque[cod_generos[int(genero)]][album]['titulo']} - {estoque[cod_generos[int(genero)]][album]['ano_lancamento']} - ${estoque[cod_generos[int(genero)]][album]['preco']:.2f}\n'C' --> para confirmar\n'R' --> Para retornar para os gêneros\n\nInsira o código: ")
            os.system('cls')
            #Confirmação da compra
            while confirmar.lower() != 'c' and confirmar.lower()!='r':
                confirmar = input(f"Código Inválido!\n\nÁlbum selecionado:\n{album}\n{estoque[cod_generos[int(genero)]][album]['artista']} - {estoque[cod_generos[int(genero)]][album]['titulo']} - {estoque[cod_generos[int(genero)]][album]['ano_lancamento']} - ${estoque[cod_generos[int(genero)]][album]['preco']:.2f}\n'C' --> para confirmar\n'R' --> Para retornar para os gêneros\n\nInsira o código: ")
                os.system('cls')
            if confirmar.lower() == 'r':
                album == 'r'
        dados_clientes['ids_albuns'][n].append(album) #FEITO Adicionando o album a lista de albums do cliente
        price = estoque[cod_generos[int(genero)]][album]['preco'] #Atribuindo a uma variável o preço da do álbum
        dados_clientes['total_compras_cliente'][n] += 1 #Incrementando em uma unidade o número de vezes que o cliente fez uma compra
        dados_clientes['total_da_venda'][n] += price #Adicionando o valor da venda, ao total de compras do cliente para compras futuras
        estoque[cod_generos[int(genero)]][album]['estoque'] -= 1 #Decrementando uma unidade no estoque do álbum
        sales_dia+=1 #Incrementando o número de vendas feitas
        if price > maior_compra_dia: # Analisando se tiver sido a maior compra, e atualizando o dado, se for o caso
            maior_compra_dia = float(price)
            maior_comprador = n
    
    ##### PERGUNTANDO SE O CLIENTE QUER COMPRAR MAIS #####
    buy_more = input('Você gostaria de comprar algo mais? (1 - sim, 2 - não)\n\nInsira o código: ')
    os.system('cls')
    buy_more = resp_binaria(buy_more, '1', 'Sim', '2', 'Não', 'Você gostaria de comprar algo mais?')
    while buy_more.lower() == '1':
        print('Insira o gênero que do álbum que deseja:')
        cod_generos={}
        num_generos=0
        for i in estoque:
            num_generos += 1
            cod_generos[num_generos] = i
            print(f"{num_generos} --> {i}")
        print('')
        genero = input('Insira o código: ')
        os.system('cls')
        while genero.isnumeric()==False or int(genero) not in cod_generos: # Para verificar se inseriu um código válido
            if genero == 'cancelar': #caso tenha inserido a opção de cancelar
                break
            print('Código inválido!\nInsira um código válido para o gênero do álbum:')
            for i in cod_generos:
                print(f'{cod_generos[i]} --> {i}')                    
            genero = input('Insira o código: ')
            os.system('cls')
        if genero == 'cancelar':#caso tenha inserido a opção de cancelar
            break
        os.system('cls')
        print(f'Gênero - {cod_generos[int(genero)]}:')
        #Irá imprimir o código de cada álbum juntamente com seu código
        print('Código - Artista - Título - Ano de lançamento - Preço\n')
        for i in estoque[cod_generos[int(genero)]]:
            print(f"{i}\n{estoque[cod_generos[int(genero)]][i]['artista']} - {estoque[cod_generos[int(genero)]][i]['titulo']} - {estoque[cod_generos[int(genero)]][i]['ano_lancamento']} - ${estoque[cod_generos[int(genero)]][i]['preco']:.2f}\n") #genero vai retornar o número da chave, que tem como valor o genêro desejado, chamando então 
        #Pedindo para o cliente inserir o código do álbum
        album = input("Insira o código do álbum que deseja, ou digite 'r' para retornar ao índice de gêneros dos álbums: ").upper()
        while album.upper() not in estoque[cod_generos[int(genero)]] and album.lower != 'r': #proteção para valores inválidos
            os.system('cls')
            print(f'Gênero - {cod_generos[int(genero)]}:')
            #Irá imprimir o código de cada álbum juntamente com seu código
            print('Código - Artista - Título - Ano de lançamento - Preço\n')
            for i in estoque[cod_generos[int(genero)]]:
                print(f"{i}\n{estoque[cod_generos[int(genero)]][i]['artista']} - {estoque[cod_generos[int(genero)]][i]['titulo']} - {estoque[cod_generos[int(genero)]][i]['ano_lancamento']} - ${estoque[cod_generos[int(genero)]][i]['preco']:.2f}\n") #genero vai retornar o número da chave, que tem como valor o genêro desejado, chamando então 
            album = input("Código inválido!\nInsira um código válido do álbum que deseja, ou digite 'r' para retornar ao índice de gêneros dos álbums: ").upper()
        os.system('cls')
        confirmar = input(f"Álbum selecionado:\n{album}\n{estoque[cod_generos[int(genero)]][album]['artista']} - {estoque[cod_generos[int(genero)]][album]['titulo']} - {estoque[cod_generos[int(genero)]][album]['ano_lancamento']} - ${estoque[cod_generos[int(genero)]][album]['preco']:.2f}\n'C' --> para confirmar\n'R' --> Para retornar para os gêneros\n\nInsira o código: ")   
        #Confirmação da compra
        while confirmar.lower() != 'c' and confirmar.lower()!='r':
            os.system('cls')
            confirmar = input(f"Código Inválido!\n\nÁlbum selecionado:\n{album}\n{estoque[cod_generos[int(genero)]][album]['artista']} - {estoque[cod_generos[int(genero)]][album]['titulo']} - {estoque[cod_generos[int(genero)]][album]['ano_lancamento']} - ${estoque[cod_generos[int(genero)]][album]['preco']:.2f}\n'C' --> para confirmar\n'R' --> Para retornar para os gêneros\n\nInsira o código: ")
        if confirmar.lower() == 'r':
            album = 'r'
        if confirmar.lower() != "r":
            dados_clientes['ids_albuns'][n].append(album) #Adicionando o album a lista de albums do cliente
            price = estoque[cod_generos[int(genero)]][album]['preco'] #Atribuindo a uma variável o preço da do álbum
            dados_clientes['total_compras_cliente'][n] += 1 #Incrementando em uma unidade o número de vezes que o cliente fez uma compra
            dados_clientes['total_da_venda'][n] += price #Adiicionando o valor da venda, ao total de compras do cliente para compras futuras
            estoque[cod_generos[int(genero)]][album]['estoque'] -= 1 #Decrementando uma unidade no estoque do álbum
            sales_dia+=1 #Incrementando o número de vendas feitas
            if price > maior_compra_dia: # Analisando se tiver sido a maior compra, e atualizando o dado, se for o caso
                maior_compra_dia = float(price)
                maior_comprador = n
            buy_more = input('Você gostaria de comprar algo mais?\n1 --> Sim\n2 --> Não\n\nInsira o código: ')
            os.system('cls')
            buy_more = resp_binaria(buy_more, '1', 'Sim', '2', 'Não', 'Você gostaria de comprar algo mais?')
    if len(dados_clientes['ids_albuns'][n]) > 1:
        input(f"Muito obrigado por comprar conosco mais uma vez, {dados_clientes['nome_cliente'][n].split()[0]}!\nPressione 'Enter' para encerrar o atendimento!")
        os.system('cls')                

    


  
  
#-------------------------------------------------Novo atendimento ou encerramento----------------------------------------------------------
    rpt = input("1 --> para começar novo atendimento\n2 --> para finalizar o programa e ver os balanços do dia\nInsira um código: ")
    os.system('cls')
    rpt = resp_binaria(rpt, '1', 'para começar um novo atendimento', '2', 'para finalizar o programa', 'Tente outra vez!')


#--------------------------------------------Repondo o estoque depois de cada dia----------------------------------------------------------------------------------------

for i in estoque:
    for j in estoque[i]:
        if estoque[i][j]['estoque'] <= 10:
            estoque[i][j]['estoque'] += random.randint(10,35)

#-------------------------------------------------Incrementando variáveis gerais-------------------------------------------------------------

sales_total+=sales_dia
if maior_compra_dia > maior_compra_geral:
    maior_compra_geral = maior_compra_dia
if len(dados_clientes["id_cliente"]) >= 1:
    os.system('cls')
    maior_gasto = dados_clientes['total_da_venda'].index((sorted(dados_clientes['total_da_venda'],reverse=True))[0])


#------------------------------------------------Calculando os dados obtidos no dia---------------------------------------------------------------------

####################################################### AINDA FALTA REALIZAR ############################################################
# Calculando quem é o cliente que mais gastou dinheiro na loja

    # for i in dados_clientes:
    #     print(dados_clientes[i])

    # print(f'Número de vendas = {sales_dia}')
    # print()

    # print(f"Total em vendas = ${sum(dados_clientes['total_da_venda']):.2f}")
    # print()

    # print(f"O cliente que mais gastou foi o {dados_clientes['nome_cliente'][maior_gasto]}, que gastou um total de {dados_clientes['total_da_venda'][maior_gasto]}")
    # print()

    # print(f"A maior compra foi de R${maior_compra_dia:.2f} feita pelo {dados_clientes['nome_cliente'][maior_comprador]}")
    # print()

    # print(f'Albuns vendidos em ordem = {albuns_vendidos}\n\n')
    # print('Os albuns mais vendidos foram:')
    # print('\nPosição - Nome do album - Número de vendas\n')
    # for i in range(3):
    #     if i < len(albuns_vendidos) :
    #         print(f'{i+1}º - {albuns_em_ordem[i]} - {albuns_vendidos[albuns_em_ordem[i]]}')

    # print()
    # print()
    # for i in dados_clientes:
    #     print(f'{i} = {dados_clientes[i]}')

#----------------------------------------------Calculando os dados gerais---------------------------------------------------------------------

# Calculando quem é o cliente que mais gastou dinheiro na loja
if len(dados_clientes["id_cliente"]) >= 1:
    os.system('cls')

    # Calculando quem é o cliente que mais gastou dinheiro na loja
    maior_gasto = dados_clientes['total_da_venda'].index((sorted(dados_clientes['total_da_venda'],reverse=True))[0])

    # Calculando o albuns mais vendido
    albuns_vendidos = {}
    for i in dados_clientes['ids_albuns']:
        for j in i:
            if j not in albuns_vendidos:
                albuns_vendidos[j] = 1
            elif j in albuns_vendidos:
                albuns_vendidos[j] += 1
    albuns_em_ordem = sorted(albuns_vendidos, key = albuns_vendidos.get, reverse=True) #aplicando a uma variável a lista dos álbums mais vendidos em ordem
    
    # Calculando os gêneros comprados por cada idade:

    #Criando uma lista com os gêneros existentes
    generos = []
    for i in estoque:
        generos.append(i)

    generos_por_idade = {'menor_que_18':{}, 'entre_18_e_25':{}, 'entre_25_e_35':{}, 'entre_35_e_55':{}, 'maior_que_55':{}}
    for i in dados_clientes["id_cliente"]: #Passando pelos index de cada cliente
        for album_do_cliente in dados_clientes["ids_albuns"][i]: #Passando por cada album do cliente
            for genero in generos: #Passando por cada gênero existente de albuns
                if album_do_cliente in estoque[genero]: #se o genero do album for igual ao genero que está sendo passado no momento
                    if dados_clientes["idade_cliente"][i] < 18: #Para cada idade do cliente
                        if genero not in generos_por_idade['menor_que_18']: #Adicione uma nova chave com uma unidade de valor
                            generos_por_idade['menor_que_18'][genero] = 1 
                        elif genero not in generos_por_idade['menor_que_18']: #Ou incremente uma unidade no valor existente da chave
                            generos_por_idade["menor_que_18"][genero] += 1                            
                    elif dados_clientes["idade_cliente"][i] >= 18 and dados_clientes["idade_cliente"][i] < 25:
                        if genero not in generos_por_idade['entre_18_e_25']:
                            generos_por_idade['entre_18_e_25'][genero] = 1
                        elif genero not in generos_por_idade['entre_18_e_25']:
                            generos_por_idade["entre_18_e_25"][genero] += 1 
                    elif dados_clientes["idade_cliente"][i] >= 25 and dados_clientes["idade_cliente"][i] < 35:
                        if genero not in generos_por_idade['entre_25_e_35']:
                            generos_por_idade['entre_25_e_35'][genero] = 1
                        elif genero not in generos_por_idade['entre_25_e_35']:
                            generos_por_idade["entre_25_e_35"][genero] += 1 
                    elif dados_clientes["idade_cliente"][i] >= 35 and dados_clientes["idade_cliente"][i] < 55:
                        if genero not in generos_por_idade['entre_35_e_55']:
                            generos_por_idade['entre_35_e_55'][genero] = 1
                        elif genero not in generos_por_idade['entre_35_e_55']:
                            generos_por_idade["entre_35_e_55"][genero] += 1 
                    elif dados_clientes["idade_cliente"][i] >= 55:
                        if genero not in generos_por_idade['maior_que_55']:
                            generos_por_idade['maior_que_55'][genero] = 1
                        elif genero not in generos_por_idade['maior_que_55']:
                            generos_por_idade["maior_que_55"][genero] += 1

    #Criando listas por faixa-etária em ordem do genero mais comprado pelo intervalo de idade, com 
    
    menor_que_18 = sorted(generos_por_idade["menor_que_18"], key = albuns_vendidos.get, reverse=True)
    entre_18_e_25 = sorted(generos_por_idade["entre_18_e_25"], key = albuns_vendidos.get, reverse=True)    
    entre_25_e_35 = sorted(generos_por_idade["entre_25_e_35"], key = albuns_vendidos.get, reverse=True)    
    entre_35_e_55 = sorted(generos_por_idade["entre_35_e_55"], key = albuns_vendidos.get, reverse=True)    
    maior_que_55 = sorted(generos_por_idade["maior_que_55"], key = albuns_vendidos.get, reverse=True)
    



    #Plus 1   Quantas vendas foram realizadas?
    #sales_total
    print(f'Total de vendas = {sales_total} vendas')
    
    #Plus 2   Qual foi o faturamento total da loja?
    #print(f"Total do faturamento da loja = ${sum(dados_clientes['total_da_venda']):.2f}")
    print(f"Total do faturamento da loja = ${sum(dados_clientes['total_da_venda']):.2f}")

    #Plus 3   Qual cliente mais gastou?
    #maior_gasto --> Index do cliente que mais gastou na loja
    print(f"O cliente que mais gastou foi o {dados_clientes['nome_cliente'][maior_gasto]}, que gastou um total de {dados_clientes['total_da_venda'][maior_gasto]}")

    #Plus 4   Qual foi a maior compra?
    #maior_compra_geral
    print(f"A maior compra foi de R${maior_compra_geral:.2f} feita pelo {dados_clientes['nome_cliente'][maior_comprador]}")
    print()

    #Plus 5   Qual é o album mais vendido?
    #albuns_em_ordem --> Dicionário com a chave sendo o número de vezes que o álbum foi vendido e o valor sendo o código do álbum
    print(f'Albuns vendidos em ordem = {albuns_vendidos}\n\n')
    print('Os albuns mais vendidos foram:')
    print('\nPosição - Nome do album - Número de vendas\n')
    for i in range(3):
        if i < len(albuns_vendidos) :
            print(f'{i+1}º - {albuns_em_ordem[i]} - {albuns_vendidos[albuns_em_ordem[i]]}')

    #Plus 6    Quais sao os generos mais comprados pelas faixas de idade abaixo:
    # - 18 a 25 anos
    # - 25 a 35 anos
    # - 35 a 55 anos
    # - acima de 55 anos

    print("Albúns mais vendidos por faixa-etária:/n")

    print("Abaixo de 18 anos:")
    for i in range(len(menor_que_18)): #Vai chamar para os generos mais comprados em ordem para cada faixa-etária
        print(f"{i+1} - {menor_que_18[i]} - {generos_por_idade['menor_que_18'][menor_que_18[i]]}") #Vai imprimir a posição, gênero e o número de vendas desse gênero naquela faixa etária
    
    print("Entre 18 e 25 anos:")
    for i in range(len(entre_18_e_25)):
        print(f"{i+1} - {entre_18_e_25[i]} - {generos_por_idade['entre_18_e_25'][entre_18_e_25[i]]}")
    
    print("Entre 18 e 25 anos:")
    for i in range(len(entre_25_e_35)):
        print(f"{i+1} - {entre_25_e_35[i]} - {generos_por_idade['entre_25_e_35'][entre_25_e_35[i]]}")
    
    print("Entre 18 e 25 anos:")
    for i in range(len(entre_35_e_55)):
        print(f"{i+1} - {entre_35_e_55[i]} - {generos_por_idade['entre_35_e_55'][entre_35_e_55[i]]}")
    
    print("Acima de 55 anos:")
    for i in range(len(maior_que_55)):
        print(f"{i+1} - {maior_que_55[i]} - {generos_por_idade['maior_que_55'][maior_que_55[i]]}")

