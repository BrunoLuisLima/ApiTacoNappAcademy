from extracty import ApiExtracty
from tkinter import *

menu_principal = Tk()
menu_principal.title("MyETL")
menu_principal.geometry("500x300")

# Input Name
label_1 = Label(menu_principal,
    text="Nome do Paciente:"
).pack()

def getTextInput_1():
    result=textbox_1.get("1.0", "end-1c")
    return result

textbox_1=Text(menu_principal, height=1, width=30)
textbox_1.pack()

btnRead_1=Button(menu_principal, height=1, width=10, text="Ok!", 
                    command=getTextInput_1)
btnRead_1.pack()


# Input id food
label_2 = Label(menu_principal,
    text="Id do Alimento"
).pack()

list_test = []
def getTextInput_2():
    result = textbox_2.get("1.0", "end-1c")
    list_test.append(result)
    # print(list_test)
    return list_test

textbox_2=Text(menu_principal, height=1, width=30)
textbox_2.pack()

btnRead_2=Button(menu_principal, height=1, width=10, text="Adicionar",
                    command=getTextInput_2)
btnRead_2.pack()


# Salvar Food
def getTextInput_3():
    print(list_test)
    objeto = ApiExtracty(list_test, getTextInput_1())
    return objeto.generate_csv()

btnRead_3=Button(menu_principal, height=1, width=10, text="Salvar", 
                    command=getTextInput_3)
btnRead_3.pack()

# Button Delete
def getTextInput_4():
    new_list = list_test.clear()
    print(list_test)
    return new_list

btnRead_4=Button(menu_principal, height=1, width=10, text="Deletar", 
                    command=getTextInput_4)
btnRead_4.pack()

menu_principal.mainloop()