from statistics import mode
import  model
import UI

def button_click():
    a = UI.get_value()
    b = UI.get_value()
    model.init(a, b)
    result = UI.get_op()
    print("Результат операции: ", result)
    print()
