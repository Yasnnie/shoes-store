from employee import Employee

employees = [Employee("12345678988","Yasmin Carvalho", "teste","22/09/2002", "Estoquista")]


def find_option(list_options, option):
    find = None

    for x in list_options:
        if x.get_cpf() == option:
            find = x
        
    return find


def category_address():
    print("Endereço")

def category_product():
    print("Produto")

def category_employee():
    print("========== Escolha uma função: ==========\n\n1.Criar funcionário\n2.Listar funcionários\n3.Comissão de um funcionário:\n4.Sair\n\n==========================================")
    option = int(input())

    if option == 1:

        print("Digite respectivamente: CPF, Nome, Endereço, Data de aniversário e Cargo")
        cpf = input()
        name = input()
        address = input()
        birth_date = input()
        office = input()
        employees.append(Employee(cpf,name,address,birth_date,office))

    if option == 2:
        print("======= Funcionários =======")
        for x in employees:
            print("{}\n----------------------------".format(x))

    
    if option == 3: 

        print("Digite o CPF do funcionário:")
        cpf = input()

        find = find_option(employees, cpf)

        if find != None:
            print(find.comission())

        else:
            print("Funcionário não encontrado!!")


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