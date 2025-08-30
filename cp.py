
mensagens = []


def criar_mensagem(remetente, assunto, destinatario, conteudo):
    msg = {
        "remetente": remetente,
        "assunto": assunto,
        "destinatario": destinatario,
        "conteudo": conteudo
    }
    mensagens.append(msg)


def popular_20_mensagens():
    assuntos = ["Login", "Matrícula", "Dúvida", "Entrega dos trabalhos", "Feedback",
                "Financiamento", "Challenger", "Eventos", "Convite", "Talent Lab"]
    remetentes = ["bruno@fiap.com", "gianolli@fiap.com", "enzo@fiap.com", "gustavo@fiap.com",
                     "larissa@fiap.com", "erick@fiap.com", "matheus@fiap.com",]
    destinatarios = ["professor@fiap.com", "suporte@fiap.com", "orientador@fiap.com", "financeiro@fiap.com"]

    i = 0
    while i < 20:
        assunto = assuntos[i % len(assuntos)] + " #" + str(i+1)
        destinatario = destinatarios[i % len(destinatarios)]
        remetente = remetentes[i % len(remetentes)]
        conteudo = "Mensagem de exemplo " + str(i+1)
        criar_mensagem(remetente, assunto, destinatario, conteudo)
        i += 1


def ordenar():
    mensagens.sort(key=lambda m: m["destinatario"])


def buscar_todas(dest_alvo):
    inicio = 0
    fim = len(mensagens) - 1
    pos = -1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        atual = mensagens[meio]["destinatario"]
        if atual == dest_alvo:
            pos = meio
            break
        elif atual < dest_alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    if pos == -1:
        return []  


    esquerda = pos
    while esquerda - 1 >= 0 and mensagens[esquerda - 1]["destinatario"] == dest_alvo:
        esquerda -= 1

   
    direita = pos
    while direita + 1 < len(mensagens) and mensagens[direita + 1]["destinatario"] == dest_alvo:
        direita += 1


    return mensagens[esquerda:direita+1]


def cadastrar_interativo():

    print("\n=== Cadastrar Mensagem ===")
    remetente = input("Remetente (e-mail): ").strip()
    assunto = input("Assunto: ").strip()
    destinatario = input("Destinatário (e-mail): ").strip()
    conteudo = input("Conteúdo: ").strip()
    criar_mensagem(remetente, assunto, destinatario, conteudo)
    ordenar() 
    print("Mensagem cadastrada.\n")

def buscar_interativo():
    if not mensagens:
        print("\nNão há mensagens cadastradas.\n")
        return
    ordenar()
    alvo = input("\nDestinatário para buscar: ").strip()
    resultados = buscar_todas(alvo)
    if not resultados:
        print("Nenhuma mensagem para:", alvo, "\n")
    else:
        print("\nEncontradas", len(resultados), "mensagem(ns) para", alvo)
        i = 0
        while i < len(resultados):
            m = resultados[i]
            print("- Assunto:", m["assunto"])
            print("  Remetente:", m["remetente"])
            print("  Conteúdo:", m["conteudo"])
            i += 1
        print()

def menu():
    popular_20_mensagens()   
    ordenar()
    while True:
        print("=== MENU ===")
        print("1 - Cadastrar nova mensagem")
        print("2 - Buscar por destinatário")
        print("3 - Total de mensagens")
        print("0 - Sair")
        op = input("Opção: ").strip()

        if op == "1":
            cadastrar_interativo()
        elif op == "2":
            buscar_interativo()
        elif op == "3":
            print("\nTotal:", len(mensagens), "mensagens\n")
        elif op == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida.\n")

menu()
