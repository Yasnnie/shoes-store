import PySimpleGUI as sg
from employee import Employee
from customer import Customer
from product import Product
from cashier import Cashier
from stock import Stock

sg.theme('DarkAmber')

products = [Product(200,"tênis", "Nike", "Jordan 4", 39)]
stocks = [Stock()]
cashiers = [Cashier(stocks[0],2000)]
employees = [Employee("12345678988","Yasmin Carvalho", "teste","22/09/2002", "Estoquista")]
customers = [Customer("44455566678", "Victor Rafael", "Teste","13/12/1998")]

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
    print("Endereço")

def category_product():
    print("Produto")

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
                [sg.Text("Endereço:"),sg.InputText()],
                [sg.Text("Data de aniversário:"),sg.InputText()],
                [sg.Text("Cargo:"),sg.InputText()],
                [sg.Ok()]]

                form = sg.Window(values[0][0], layout2)
                
                event2, values2 = form.read()

                if event2 == "Ok":
                    employees.append(Employee(values2[0],values2[1],values2[2],values2[3],values2[4]))
                    form.close()

            if option == "Listar funcionários":
                list_all(employees)

            
            if option == "Comissão de um funcionário": 
                layout2 = [[sg.Text("Digite o CPF do funcionário:"),sg.InputText()],
                [sg.Text( key='-TEXT-')],
                [sg.Ok()]]

                form = sg.Window(values[0][0], layout2)
                
                event2, values2 = form.read()
                if event2 == "Ok":
                    find = find_option(employees, values2[0])

                    if find != None:
    
                        form['-TEXT-'].Update(find.comission())

                    else:
                        form['-TEXT-'].Update("Funcionário não encontrado!!")

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
                [sg.Text("Endereço:"),sg.InputText()],
                [sg.Text("Data de aniversário:"),sg.InputText()],
                [sg.Ok()]]

                form = sg.Window(values[0][0], layout2)
                
                event2, values2 = form.read()

                if event2 == "Ok":
                    customers.append(Customer(values2[0],values2[1],values2[2],values2[3]))
                    form.close()

            if option == "Listar clientes":
                list_all(customers)

            if option == "Visualizar Cliente":
                layout2 = [[sg.Text("Digite o CPF do cliente:"),sg.InputText()],
                [sg.Text( key='-TEXT-')],
                [sg.Ok()]]

                form = sg.Window(values[0][0], layout2)
                
                event2, values2 = form.read()
                if event2 == "Ok":
                    find = find_option(customers, values2[0])

                    if find != None:
                        form['-TEXT-'].Update(find.get_all_information())

                    else:
                        form['-TEXT-'].Update("Cliente não encontrado!!")

            if option == "Comprar":
                layout2 = [[sg.Listbox(values=customers,size=(90, 6))],
                [sg.Listbox( values=cashiers,size=(90, 6))],
                [sg.Listbox( values=employees,size=(90, 6))],
                [sg.Listbox( values=products,size=(90, 6),select_mode='extended')],
                [sg.Button("Comprar"),sg.Cancel()]]

                form = sg.Window(values[0][0], layout2)

                
                event2, values2 = form.read()
                if event2 == "Comprar":
                    if values2[0][0] and values2[1][0] and values2[2][0] and values2[3][0]:
                        values2[0][0].new_purchase(values2[3][0],values2[1][0],values2[2][0])
                    else:
                        print("error")

                if event2 == sg.WIN_CLOSED or event2 == 'Cancel': # if user closes window or clicks cancel
                    form.close()
                    

            if option == "Pagar compra" or option == "Cancelar compra":
                layout2 = [[sg.Listbox(values=customers),sg.Button("Selecionar")],
                [sg.Listbox( values=[],key='-LIST-PRODUCTS-',visible=False),sg.Button(option, key="-BUTTON-VER-", visible=False)],
                [sg.Cancel()]]

                form = sg.Window(values[0][0], layout2)

                while True:
                    event2, values2 = form.read()

                    if event2 == "Selecionar":
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
                layout2 = [[sg.Listbox(values=customers),sg.Button("Selecionar")],
                [sg.Listbox( values=[],key='-LIST-PRODUCTS-',visible=False),sg.Button(option, key="-BUTTON-VER-", visible=False)],
                [sg.Text(key="-TEXT-")],
                [sg.Cancel()]]

                form = sg.Window(values[0][0], layout2)

                while True:
                    event2, values2 = form.read()

                    if event2 == "Selecionar":
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
    print("Estoque")

def category_cashier():
    print("Caixa")

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
