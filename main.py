import mysql.connector as mysql
import os #biblioteca usada na funcao de salvar_arquivo()

#as 3 atividades do programa divididas em funcoes:
def mostra_historico():
    try:
        conexao = mysql.connect(host="localhost", user="root", password="SUA SENHA AQUI", database="reg_tempo_estudo")
        cursor = conexao.cursor(buffered=True)

    except mysql.Error as erro: \
            print(f"Erro no MySQL: {erro}")

    positivo = "SELECT disciplina, tempo, historico FROM estudo"
    cursor.execute(positivo)
    resultados = cursor.fetchall()
    if resultados:
        print("\nDisciplina | Tempo | Quantidade de estudos:")
        for linha in resultados:
            print(linha[0], "", linha[1], " ", linha[2])
    cursor.close()

    pergunta = input("\nDeseja fazer algo mais? S para sim. Qualquer outra tecla para sair ").strip().lower()
    if pergunta == 's':
        print("\n")
        menu()
    else:
        conexao.close()
        print("\nConexão encerrada. Até a próxima!")

def salvar_arquivo():
    try:
        conexao = mysql.connect(host="localhost", user="root", password="SUA SENHA AQUI", database="reg_tempo_estudo")
        cursor = conexao.cursor(buffered=True)

    except mysql.Error as erro: \
            print(f"Erro no MySQL: {erro}")

    positivo = "SELECT disciplina, tempo, historico FROM estudo"
    cursor.execute(positivo)
    salvamento = cursor.fetchall()
    if salvamento:
        nome_base = "historico_estudos"
        extensao = ".txt"
        contador = 1
        nome_final = f"{nome_base}{extensao}"

        while os.path.exists(nome_final): #evita que dados sejam sobrescritos
            nome_final = f"{nome_base}_{contador}{extensao}"
            contador += 1

        with open(nome_final, 'w', newline='', encoding='utf-8') as arquivo:
            arquivo.write("Disciplina | Tempo | Quantidade de estudos:\n")
            for linha in salvamento:
                texto_linha = f"{linha[0]} | {linha[1]} | {linha[2]}\n"
                arquivo.write(texto_linha)
            print("Arquivo TXT criado com sucesso!")
    cursor.close()

    pergunta = input("\nDeseja fazer algo mais? S para sim. Qualquer outra tecla para sair ").strip().lower()
    if pergunta == 's':
        print("\n")
        menu()
    else:
        conexao.close()
        print("\nConexão encerrada. Até a próxima!")

def novo_estudo():
    try:
        conexao = mysql.connect(host="localhost", user="root", password="SUA SENHA AQUI", database="reg_tempo_estudo")
        cursor = conexao.cursor(buffered=True)

    except mysql.Error as erro: \
            print(f"Erro no MySQL: {erro}")

    while True:
        disciplina = input("Qual disciplina voce estudou? ou '0' para sair").strip().lower()
        if disciplina == '0':
            break

        try:
            h_ini = int(input("Hora de início: "))
            m_ini = int(input("Minutos de início: "))
            h_fim = int(input("Hora de término: "))
            m_fim = int(input("Minutos de término: "))

            duracao = (h_fim * 60 + m_fim) - (h_ini * 60 + m_ini)
            if duracao < 0:
                print(
                    "Tempo negativo ou ultrapassou meia-noite (nesse caso registre as horas ate meia noite e as horas do outro dia separadas)")
                continue
        except ValueError:
            print("Erro: Digite apenas números inteiros.")
            continue

        # VERIFICAÇÃO SE JÁ EXISTE O REGISTRO
        verificar = "SELECT tempo, historico FROM estudo WHERE disciplina = %s"
        cursor.execute(verificar, (disciplina,))
        resultado = cursor.fetchone()

        if resultado:
            tempo_atual = resultado[0] or 0
            historico_atual = resultado[1] or 0

            novo_tempo = tempo_atual + duracao
            novo_historico = historico_atual + 1

            sql_update = "UPDATE estudo SET tempo = %s, historico = %s WHERE disciplina = %s"
            cursor.execute(sql_update, (novo_tempo, novo_historico, disciplina))
            print(f"Atualizado! Total: {novo_tempo}min | Quantidade de estudos: {novo_historico}")

        else:
            # 3. INSERT
            sql_insert = "INSERT INTO estudo (disciplina, tempo, historico) VALUES (%s, %s, %s)"
            cursor.execute(sql_insert, (disciplina, duracao, 1))
            print(f"'{disciplina.capitalize()}' cadastrada com {duracao}min.")

        conexao.commit()

        continue
    cursor.close()

    pergunta = input("\nDeseja fazer algo mais? S para sim. Qualquer outra tecla para sair ").strip().lower()
    if pergunta == 's':
        print("\n")
        menu()
    else:
        conexao.close()
        print("\nConexão encerrada. Até a próxima!")

def menu(): #COMANDA O PROGRAMA
    print("=" * 35)
    print("** Controle de Tempo de Estudo **")
    print("=" * 35)

    print("1 - Mostrar historico de estudos")
    print("2 - Salvar arquivo txt com historico de estudos")
    print("3 - Registrar novo estudo")
    print("0 - Para sair do programa\n")

    while True:
        opcao = input("O que deseja fazer?")
        if opcao == '0':
            break
        elif opcao == '1':
            mostra_historico()
        elif opcao == '2':
            salvar_arquivo()
        elif opcao == '3':
            novo_estudo()
        else:
            print("Opção invalida!\n")
            continue
        break

    if 'conexao' in locals() and conexao.is_connected():
        cursor.close()
        conexao.close()
        print("\nConexão encerrada. Até a próxima!")


# CODIGO PRINCIPAL
menu()