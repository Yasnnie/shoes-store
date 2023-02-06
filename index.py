import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

import PySimpleGUI as sg
from employee import Employee
from customer import Customer
from product import Product
from cashier import Cashier
from stock import Stock


sg.theme('DarkAmber')

products = [Product(200,"tênis", "Nike", "Jordan 4", 39), Product(100,"Tênis", "Nike", "Jordan 4", 39)]
stocks = [Stock()]
cashiers = [Cashier(stocks[0],2000)]
employees = [Employee("12345678988","Yasmin Carvalho", "teste","22/09/2002", "Estoquista")]
customers = [Customer("44455566678", "Victor Rafael", "Teste","13/12/1998"),Customer("52834588820", "Luisa", "Teste","23/02/1994")]

def list_all(objects_list):
    layout2 = []
            
    for x in objects_list:
        layout2.append([sg.Text(x)])
        layout2.append([sg.Text("------------------------")])

    form = sg.Window('Titulo', layout2)
    form.read()

def find_option(list_options, option):
    find = None

    for x in list_options:
        if x.get_cpf() == option:
            find = x
        
    return find

def category_address():
    print("Endereço")

def category_product():
    layout = [
        [sg.Text("Selecione uma opção:")],
        [sg.Listbox(values=['Adicionar produto', 'Listar produtos'], size=(60, 6))],
        [sg.Ok(), sg.Cancel()]
        ]
    
    window = sg.Window('Produtos', layout)

    while True:
        event, values = window.read()

        if event == "Ok":
            option = values[0][0]

            if option == "Adicionar produto":
                layout2 = [
                    [sg.Text("Preço:"),sg.InputText()],
                    [sg.Text("Tipo:"),sg.InputText()],
                    [sg.Text("Marca:"),sg.InputText()],
                    [sg.Text("Modelo:"),sg.InputText()],
                    [sg.Text("Tamanho:"),sg.InputText()],
                    [sg.Ok()]
                ]

                form = sg.Window(option, layout2)
                
                event2, values2 = form.read()

                if event2 == "Ok":
                    products.append(Product(float(values2[0]), values2[1], values2[2], values2[3], int(values2[4])))
                    form.close()

            if option == "Listar produtos":
                list_all(products)

        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            window.close()
            break

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
    layout = [
        [sg.Text("Selecione uma opção:")],
        [sg.Listbox(values=['Adicionar ao estoque', 'Remover do estoque', 'Listar itens'], size=(60, 6))],
        [sg.Ok(), sg.Cancel()]
        ]
    
    window = sg.Window('Estoque', layout)

    while True:
        event, values = window.read()

        if event == "Ok":
            option = values[0][0]

            if option == "Adicionar ao estoque":
                """Cria o layout base, com uma lista de produtos"""
                layout2 = [
                    [sg.Listbox(values=products, size=(90, 6), enable_events=True)],
                    [sg.Text(key='-TEXT-')],
                    [sg.Ok()]]

                form = sg.Window(option, layout2)
                
                while True:
                    event2, values2 = form.read()

                    """Caso seja selecionado algum produto, o texto é atualizado com o __str__ desse produto
                        com um produto selecionado, caso seja pressionado o botão OK, o produto é adicionado ao estoque"""
                    if event2 == 0:
                        form['-TEXT-'].Update(values2[0][0])

                    if event2 == sg.WIN_CLOSED or event2 == 'Cancel':
                        form.close()
                        break

                    if event2 == "Ok":
                        stocks[0].add(values2[0][0])
                        form.close()

            if option == "Remover do estoque":
                """Cria o layout base com uma lista de produtos disponíveis no estoque, o deixando clicáveis"""
                layout2 = [
                    [sg.Listbox(values=stocks[0].get_products(), size=(90, 6), enable_events=True)],
                    [sg.Text(key='-TEXT-')],
                    [sg.Ok()]]

                form = sg.Window(option, layout2)
                
                while True:
                    event2, values2 = form.read()

                    if event2 == 0:
                        form['-TEXT-'].Update(values2[0][0])

                    if event2 == sg.WIN_CLOSED or event2 == 'Cancel':
                        form.close()
                        break
                    
                    """Remove o produto selecionado do estoque"""
                    if event2 == "Ok":
                        stocks[0].remove(values2[0][0])
                        form.close()
            
            """Retorna todos os itens do estoque"""
            if option == "Listar itens":
                list_all(stocks[0].get_products())

        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            window.close()
            break

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