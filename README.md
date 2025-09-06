# Sistema faculdade

Um programa de linha de comando simples, desenvolvido em Python, para o gerenciamento de cadastros de alunos. O sistema permite criar, listar, atualizar e remover (CRUD) alunos de uma lista.

## ✨ Funcionalidades

-   **Cadastrar Alunos:** Adiciona novos alunos ao sistema.
-   **Geração Automática de Matrícula:** Cria uma matrícula única para cada aluno, baseada na sigla do curso e um número sequencial (ex: `GES1`, `GEC1`, `GES2`).
-   **Validação de Curso:** Garante que apenas cursos válidos (`GEA`, `GES`, `GEC`, `GEP`, `GEB`, `GET`, `GEL`) sejam aceitos no cadastro.
-   **Listar Alunos:** Exibe a lista completa de alunos cadastrados com suas informações.
-   **Atualizar Alunos:** Permite a modificação do nome e e-mail de um aluno já cadastrado, buscando-o por sua matrícula.
-   **Remover Alunos:** Exclui o registro de um aluno do sistema.
-   **Menu Interativo:** Interface de fácil utilização diretamente no terminal.

## 🚀 Como Executar

1.  **Clone o repositório** (ou simplesmente baixe o arquivo `sistema_faculdade.py`):
    ```sh
    git clone https://github.com/lucassobana/C216.git
    ```
2.  **Execute o script** através do terminal:
    ```sh
    python sistema_faculdade.py
    ```
3.  Pronto! O menu interativo será exibido e você poderá utilizar o sistema.
