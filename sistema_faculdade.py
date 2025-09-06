alunos = []
contadores_matricula = {}

def gerar_matricula(curso):
    curso = curso.upper()
    if curso not in contadores_matricula:
        contadores_matricula[curso] = 0
    contadores_matricula[curso] += 1
    numero_sequencial = contadores_matricula[curso]
    return f"{curso}{numero_sequencial}"

def cadastrar_aluno():    
    cursos_validos = ["GEA", "GES", "GEC", "GEP", "GEB", "GET", "GEL"]
    
    nome = input("Digite o nome do aluno: ")
    email = input("Digite o e-mail do aluno: ")
    curso = input(f"Digite a sigla do curso ({', '.join(cursos_validos)}): ")

    if curso.upper() not in cursos_validos:
        print(f"\nErro: Curso inválido. Opções válidas são: {', '.join(cursos_validos)}")
        return

    if not nome or not email:
        print("Erro: Nome e e-mail são campos obrigatórios. O aluno não foi cadastrado.")
        return

    matricula = gerar_matricula(curso)
    
    aluno = {
        "matricula": matricula,
        "nome": nome,
        "email": email,
        "curso": curso.upper()
    }
    
    alunos.append(aluno)
    print(f"\nAluno '{nome}' cadastrado com sucesso! Matrícula: {matricula}")

def listar_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        for aluno in alunos:
            print(f"Matrícula: {aluno['matricula']}, Nome: {aluno['nome']}, E-mail: {aluno['email']}, Curso: {aluno['curso']}")

def atualizar_aluno():
    matricula_alvo = input("Digite a matrícula do aluno a ser atualizado: ")
    
    for aluno in alunos:
        if aluno["matricula"].upper() == matricula_alvo.upper():
            print(f"Atualizando dados do aluno: {aluno['nome']}")
            
            novo_nome = input(f"Digite o novo nome (atual: {aluno['nome']}): ")
            novo_email = input(f"Digite o novo e-mail (atual: {aluno['email']}): ")
            
            if novo_nome:
                aluno["nome"] = novo_nome
            if novo_email:
                aluno["email"] = novo_email
                
            print("\nAluno atualizado com sucesso!")
            return
            
    print(f"Aluno com matrícula '{matricula_alvo}' não encontrado.")

def remover_aluno():
    matricula_alvo = input("Digite a matrícula do aluno a ser removido: ")
    
    for aluno in alunos:
        if aluno["matricula"].upper() == matricula_alvo.upper():
            alunos.remove(aluno)
            print(f"Aluno '{aluno['nome']}' removido com sucesso!")
            return
            
    print(f"Aluno com matrícula '{matricula_alvo}' não encontrado.")

def main():
    while True:
        print("\n Menu de opções:")
        print("1. Cadastrar Aluno")
        print("2. Listar Alunos")
        print("3. Atualizar Aluno")
        print("4. Remover Aluno")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_aluno()
        elif opcao == '2':
            listar_alunos()
        elif opcao == '3':
            atualizar_aluno()
        elif opcao == '4':
            remover_aluno()
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Por favor, tente novamente.")

if __name__ == "__main__":
    main()