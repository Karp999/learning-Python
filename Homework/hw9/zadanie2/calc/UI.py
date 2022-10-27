import model

def get_value():  
    value = int(input("\nВведите переменную: "))
    return value

def get_op():

    m = input('''\nМЕНЮ КАЛЬКУЛЯТОРА:
            \nДля операции сложение введите 1: 
            \nДля операции вычитание введите 2: 
            \nДля операции деление введите 3: 
            \nДля операции умножение введите 4: 
            \nВыход: введите 0.\n''')
    match m:
        case '1':
            return model.sum()
        case '2':
            return model.sub()
        case '3':
            return model.div()
        case '4':
            return model.prod()   
        case '0': 
            return
    return 


            
