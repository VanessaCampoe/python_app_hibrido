"""CRUD é um acrônimo usado em programação e banco de dados que representa as quatro operações básicas de manipulação de dados:

✅ C – Create (Criar)

Inserir novos registros.
Ex.: adicionar um novo usuário ao sistema.

✅ R – Read (Ler)

Consultar dados existentes.
Ex.: listar todos os produtos cadastrados.

✅ U – Update (Atualizar)

Modificar dados existentes.
Ex.: editar o nome de um cliente.

✅ D – Delete (Excluir)

Remover dados do sistema.
Ex.: apagar um registro de pedido."""

import os 

def limpar():
    os.system("cls" if os.name == "nt" else "clear")