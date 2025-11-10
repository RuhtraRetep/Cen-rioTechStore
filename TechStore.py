import mysql.connector

conexao = mysql.connector.connect(
    host= "localhost",
    user = "root",
    password = "",
    database = "techstore",
    port = 3309
)

cursor = conexao.cursor()



def menu():

    print("MENU TECHSTORE\n[1] Inserir produtos\n[2] Visualizar produtos\n[3] Atualizar produtos\n[4] Excluir produtos\n[0] Sair")

    match input("Escolha uma opção: "):
        case "1": inserir_produtos()
        case "2": visualizar_produtos()
        case "3": atualizar_produtos()
        case "4": excluir_produtos()
        case _: exit()

def inserir_produtos():

    print("Digite os dados do produto:\n")
    input_nome = input("Nome: ")
    input_preco = float(input("Preço: "))
    input_categoria = input("Categoria: ")

    sql_INSERT = "insert into produtos (nome, preco, categoria) values (%s, %s, %s)"
    valores = (input_nome, input_preco, input_categoria)

    cursor.execute(sql_INSERT, valores)
    conexao.commit()

    print(f"{cursor.rowcount} produto(s) inserido(s) com sucesso!")
   
    print("\n\nChamar menu? [1] Sim [0] Não")
    if input() == "1":
        menu()


def visualizar_produtos():
    sql_SELECT = "select * from produtos"

    cursor.execute(sql_SELECT)
    produtos = cursor.fetchall()

    print("\nProdutos cadastrados:")
    for p in produtos:
        print(p)

    print("\n\nChamar menu? [1] Sim [0] Não")
    if input() == "1":
        menu()
    

def atualizar_produtos():

    coluna = ""
    print("Atualizar preço dos produtos\n\n")
    where_id = int(input("Id do produto: "))
    update_valor = float(input("Digite o novo preço: "))
    
    sql_UPDATE = "UPDATE produtos SET preco = (%s) WHERE id = (%s)"

    valores = (update_valor, where_id)

    cursor.execute(sql_UPDATE, valores)
    conexao.commit()

    print("\n\nChamar menu? [1] Sim [0] Não")
    if input() == "1":
        menu()

def excluir_produtos():
    id_produto = int(input("Excluir produtos\n\nId do produto: "))

    sql_DELETE = "Delete from produtos where id = (%s)"
    valores = (id_produto,)

    cursor.execute(sql_DELETE, valores)
    conexao.commit()

    print("\n\nChamar menu? [1] Sim [0] Não")
    if input() == "1":
        menu()


menu()
