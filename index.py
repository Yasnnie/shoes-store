import PySimpleGUI as sg
import locale

from purchase import Purchase
from employee import Employee
from customer import Customer
from address import Address
from product import Product
from cashier import Cashier
from stock import Stock

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


sg.theme('DarkAmber')

address = [Address("Rua 1", "São Paulo", "SP", "Brasil", "Centro")]
products = [Product(200,"tênis", "Nike", "Jordan 4", 39), Product(100,"Tênis", "Nike", "Jordan 4", 39)]
stocks = [Stock(products)]
cashiers = [Cashier(stocks[0],2000)]
employees = [Employee("12345678988","Yasmin Carvalho", address[0],"22/09/2002", "Estoquista")]
customers = [Customer("44455566678", "Victor Rafael", address[0],"13/12/1998"),Customer("52834588820", "Luisa", "Teste","23/02/1994")]
Purchases = [Purchase(employees[0], customers[0], products[0], "pending")]

def list_all(objects_list):
    layout2 = []
            
    for x in objects_list:
        layout2.append([sg.Text(x)])
        layout2.append([sg.Text("------------------------")])

    form = sg.Window(values[0][0], layout2)
    form.read()

def find_option(list_options, option):
    find = None

    for x in list_options:
        if x.get_cpf() == option:
            find = x
        
    return find

    

def category_address():
    layout = [
        [sg.Text("Selecione uma opção:")],
        [sg.Listbox(values=['Adicionar endereço', 'Listar endereços'], size=(60, 6))],
        [sg.Ok(), sg.Cancel()]
        ]
    window = sg.Window('Endereço', layout)

    while True:
        event, values = window.read()

        if event == "Ok":
            option = values[0][0]

            if option == "Adicionar endereço":
                layout2 = [
                    [sg.Text("Rua:"),sg.InputText()],
                    [sg.Text("Cidade:"),sg.InputText()],
                    [sg.Text("Estado:"),sg.InputText()],
                    [sg.Text("País :"),sg.InputText()],
                    [sg.Text("Bairro:"),sg.InputText()],
                    [sg.Ok()]
                ]

                form = sg.Window(option, layout2)
                
                event2, values2 = form.read()

                if event2 == "Ok":
                    address.append(Address(values2[0], values2[1], values2[2], values2[3], values2[4]))
                    form.close()

            if option == "Listar endereços":
                list_all(address)

        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            window.close()
            break

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
    layout = [[sg.Text("Selecione uma opção:")],[sg.Listbox(values=['Criar funcionário', 'Listar funcionários', 'Comissão de um funcionário'], size=(60, 6))],[sg.Ok(), sg.Cancel()]]

    window = sg.Window('Funcionário', layout)
    

    while True:
        event, values = window.read()
        if event == "Ok":
            option = values[0][0]

     
            if option == "Criar funcionário":

                layout2 = [[sg.Text("CPF:"),sg.InputText()],
                [sg.Text("Nome:"),sg.InputText()],
                [sg.Text("Endereço:"),sg.Listbox(values=address,size=(60, 6))],
                [sg.Text("Data de aniversário:"),sg.InputText()],
                [sg.Text("Cargo:"),sg.InputText()],
                [sg.Ok()]]

                form = sg.Window(values[0][0], layout2)
                
                event2, values2 = form.read()

                if event2 == "Ok" and values2:
                    employees.append(Employee(values2[0],values2[1],values2[2],values2[3],values2[4]))
                    form.close()

            if option == "Listar funcionários":
                list_all(employees)

            
            if option == "Comissão de um funcionário": 
                layout2 = [[sg.Listbox(values=employees,size=(90, 6),enable_events=True)],
                [sg.Text( key='-TEXT-')],
                [sg.Ok()]]

                form = sg.Window(option, layout2)
                while True:
                    event2, values2 = form.read()

                    if event2 == 0:
                        form['-TEXT-'].Update(values2[0][0].comission())
                    if event2 == sg.WIN_CLOSED or event2 == 'Cancel':
                        break
                        form.close()

        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            window.close()
            break

def category_customer():
    
    layout = [[sg.Text("Selecione uma opção:")],[sg.Listbox(values=['Criar cliente', 'Listar clientes','Visualizar Cliente','Comprar' ,'Pagar compra', 'Cancelar compra', 'Visualizar compra'], size=(60, 6))],[sg.Ok(), sg.Cancel()]]

    window = sg.Window('Cliente', layout)
    

    while True:
        event, values = window.read()

        if event == "Ok":
            option = values[0][0]

            if option == "Criar cliente":
                layout2 = [[sg.Text("CPF:"),sg.InputText()],
                [sg.Text("Nome:"),sg.InputText()],
                [sg.Text("Endereço:"),sg.Listbox(values=address,size=(60, 6))],
                [sg.Text("Data de aniversário:"),sg.InputText()],
                [sg.Ok()]]

                form = sg.Window(option, layout2)
                
                event2, values2 = form.read()

                if event2 == "Ok" and values2:
                    customers.append(Customer(values2[0],values2[1],values2[2],values2[3]))
                    form.close()

            if option == "Listar clientes":
                list_all(customers)

            if option == "Visualizar Cliente":
                layout2 = [[sg.Listbox(values=customers,size=(90, 6),enable_events=True)],
                [sg.Text( key='-TEXT-')],
                [sg.Ok()]]

                form = sg.Window(option, layout2)
                while True:
                    event2, values2 = form.read()

                    if event2 == 0:
                        form['-TEXT-'].Update(values2[0][0].get_all_information())
                    if event2 == sg.WIN_CLOSED or event2 == 'Cancel':
                        break
                        form.close()

            if option == "Comprar":
                layout2 = [[sg.Listbox(values=customers,size=(90, 6))],
                [sg.Listbox( values=employees,size=(90, 6))],
                [sg.Listbox( values=cashiers,size=(90, 6),enable_events=True)],
                [sg.Listbox( values=[],size=(90, 6),visible= False,select_mode='extended', key="-PRODUCTS-LIST-")],
                [sg.Button("Comprar"),sg.Cancel()]]

                form = sg.Window(option, layout2)

                while True:
                    event2, values2 = form.read()
                    
                    if event2 == 2:
                        form["-PRODUCTS-LIST-"].Update(values=values2[2][0].get_stock().get_products(), visible=True)

                    if event2 == "Comprar":
                        if values2[0][0] and values2[1][0] and values2[2][0] and values2["-PRODUCTS-LIST-"][0]:
                            values2[0][0].create_purchase(values2["-PRODUCTS-LIST-"],values2[2][0],values2[1][0])
                            form.close()
                            break

                        else:
                            print("error")

                    if event2 == sg.WIN_CLOSED or event2 == 'Cancel': # if user closes window or clicks cancel
                        form.close()
                        break
                                 
            if option == "Pagar compra" or option == "Cancelar compra":
                layout2 = [[sg.Listbox(values=customers,enable_events=True,size=(90, 6))],
                [sg.Listbox( values=[],key='-LIST-PRODUCTS-',visible=False,size=(90, 6)),sg.Button(option, key="-BUTTON-VER-", visible=False)],
                [sg.Cancel()]]

                form = sg.Window(option, layout2)

                while True:
                    event2, values2 = form.read()
                    print(event2)
                    if event2 == 0:
                        form['-LIST-PRODUCTS-'].Update(values=values2[0][0].get_purchases(),visible=True)
                        form['-BUTTON-VER-'].Update(visible=True)

                    if event2 == "-BUTTON-VER-":
                        if option == "Pagar compra":
                            values2[0][0].pay_purchase(values2["-LIST-PRODUCTS-"][0].get_id())
                        else:
                            values2[0][0].cancel_purchase(values2["-LIST-PRODUCTS-"][0].get_id())

                    if event2 == sg.WIN_CLOSED or event2 == 'Cancel': # if user closes window or clicks cancel
                        form.close()
                        break

            if option == "Visualizar compra":
                layout2 = [[sg.Listbox(values=customers,enable_events=True,size=(90, 6))],
                [sg.Listbox( values=[],key='-LIST-PRODUCTS-',visible=False,size=(90, 6)),sg.Button(option, key="-BUTTON-VER-", visible=False)],
                [sg.Text(key="-TEXT-")],
                [sg.Cancel()]]

                form = sg.Window(option, layout2)

                while True:
                    event2, values2 = form.read()

                    if event2 == 0:
                        form['-LIST-PRODUCTS-'].Update(values=values2[0][0].get_purchases(),visible=True)
                        form['-BUTTON-VER-'].Update(visible=True)

                    if event2 == "-BUTTON-VER-":
                        form["-TEXT-"].Update(values2["-LIST-PRODUCTS-"][0])

                    if event2 == sg.WIN_CLOSED or event2 == 'Cancel': # if user closes window or clicks cancel
                        form.close()
                        break

        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            window.close()
            break

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
    layout = [
        [sg.Text("Selecione uma opção:")],
        [sg.Listbox(values=['Criar Compra', 'Cancelar Compra'], size=(60, 6))],
        [sg.Ok(), sg.Cancel()]
        ]
    
    window = sg.Window('Caixa', layout)

    while True:
        event, values = window.read()

        if event == "Ok":
            option = values[0][0]

            if option == "Criar Compra":
                layout2 = [
                    [sg.Listbox(values=employees, size=(90, 6), enable_events=True)],
                    [sg.Text(key='-TEXT-')],
                    [sg.Ok()]]

                form = sg.Window("Funcionário", layout2)
                
                

                while True:
                    event2, values2 = form.read()

                    if event2 == 0:
                        form['-TEXT-'].Update(values2[0][0])

                    if event2 == sg.WIN_CLOSED or event2 == 'Cancel':
                        form.close()
                        break
                    
                    if event2 == "Ok":
                        employee = (values2[0][0])
                        
                        form.close()


                layout3 = [
                    [sg.Listbox(values=customers, size=(90, 6), enable_events=True)],
                    [sg.Text(key='-TEXT-')],
                    [sg.Ok()]]

                form = sg.Window("Cliente", layout3)
                
                

                while True:
                    event3, values3 = form.read()

                    if event3 == 0:
                        form['-TEXT-'].Update(values3[0][0])

                    if event3 == sg.WIN_CLOSED or event3 == 'Cancel':
                        form.close()
                        break
                    
                    if event3 == "Ok":
                        customerPurchase = (values3[0][0])
                        
                        form.close()
                        break

                purchaseProducts = []

                layout4 = [
                    [sg.Listbox(values=stocks[0].get_products(), size=(90, 6), enable_events=True)],
                    [sg.Text(key='-TEXT-')],
                    [sg.Ok()]]

                form = sg.Window("Produtos", layout4)
                
                while True:
                    event4, values4 = form.read()

                    if event4 == 0:
                        form['-TEXT-'].Update(values4[0][0])

                    if event4 == sg.WIN_CLOSED or event4 == 'Cancel':
                        form.close()
                        break
                    
                    if event4 == "Ok":
                        purchaseProducts.append(values4[0][0])
                        form.close()
                        break

                cashiers[0].create_purchase(employee=employee, customer_purchase=customerPurchase, products=purchaseProducts)

            if option == "Cancelar Compra":
                layout2 = [
                    [sg.Listbox(values=cashiers[0].get_purchases(), size=(90, 6), enable_events=True)],
                    [sg.Text(key='-TEXT-')],
                    [sg.Ok()]]

                form = sg.Window("Cancele uma Compra", layout2)
                
                

                while True:
                    event2, values2 = form.read()

                    if event2 == 0:
                        form['-TEXT-'].Update(values2[0][0])

                    if event2 == sg.WIN_CLOSED or event2 == 'Cancel':
                        form.close()
                        break
                    
                    if event2 == "Ok":
                        Purchases.remove(values2[0][0])
                        form.close()


            """Retorna todos os itens do estoque"""
            if option == "Listar itens":
                list_all(stocks[0].get_products())

        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            window.close()
            break


layout = [[sg.Text("Selecione uma categoria:")],[sg.Listbox(values=['Endereço', 'Funcionário', 'Cliente','Produto','Caixa','Estoque'], size=(60, 6))],[sg.Submit(), sg.Cancel()]]

window = sg.Window('Bem-vindo', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break

    if event == "Submit":

        if values[0][0] == "Endereço":
            category_address()

        if values[0][0] == "Funcionário":
            category_employee()

        if values[0][0] == "Cliente":
            category_customer()

        if values[0][0] == "Produto":
            category_product()

        if values[0][0] == "Caixa":
            category_cashier()

        if values[0][0] == "Estoque":
            category_stock()
      

window.close()
