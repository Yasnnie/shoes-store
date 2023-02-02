def category_address():
    print("Endereço")

def category_product():
    print("Produto")

def category_employee():
    print("Funcionário")

def category_customer():
    print("Cliente")

def category_stock():
    print("Estoque")

def category_cashier():
    print("Caixa")


while True:
    print("========= Escolha uma categoria: =========\n\n1.Endereço\n2.Produto\n3.Funcionário\n4.Cliente\n5.Estoque\n6.Caixa\n7.Sair\n\n===========================================")
    option = int(input())
    if option == 1:
        category_address()
    if option == 2:
        category_product()
    if option == 3:
        category_employee()
    if option == 4:
        category_customer()
    if option == 5:
        category_stock()
    if option == 6:
        category_cashier()
    if option < 1 or option >= 7:
        break