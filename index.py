import PySimpleGUI as sg
from employee import Employee
# from customers import Customer

sg.theme('DarkAmber')

employees = [Employee("12345678988","Yasmin Carvalho", "teste","22/09/2002", "Estoquista")]
# customers = [Customer("44455566678", "Victor Rafael", "Teste","13/12/1998")]


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
                    employees.append(Employee(values[0],values[1],values[2],values[3],values[4]))
                    form.close()

            if option == "Listar funcionários":
                layout2 = []
        
                
                for x in employees:
                    layout2.append([sg.Text(x)])
                    layout2.append([sg.Text("------------------------")])

                form = sg.Window(values[0][0], layout2)
                form.read()

            
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
                        print("Funcionário não encontrado!!")

        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            window.close()
            break


def category_customer():
    print("========== Escolha uma função: ==========\n\n1.Criar cliente\n2.Listar clientes\n3.Dados do cliente\n4.Realizar um compra\n5.Pagar uma compra\n6.Cancelar compra\n7.Sair\n\n==========================================")
    option = int(input())

    # if option == 1:


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
