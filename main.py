class DFA:
    def __init__(self, transition_function:dict, start_state:str, accept_states:set)->None:
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states

    def is_accepted(self, string:str)->bool:
        current_state = self.start_state
        for char in string:
            current_state = self.transition_function[current_state][char]
        return current_state in self.accept_states

    def __str__(self):
        return "DFA: {}".format(self.transition_function)
    def lexerAritmetico(self, string:str)->list:
        """
        Las expresiones aritméticas sólo podrán contener los siguientes tipos de tokens:

        Enteros
        Flotantes (Reales)
        Operadores:
        Asignación
        Suma
        Resta
        Multiplicación
        División
        Potencia
        Identificadores:
        Variables
        Símbolos especiales:
        (
        )
        Comentarios:
        // seguido de caracteres hasta que se acabe el renglón
        """
        pass

    

def lexerAritmetico(archivo:str,lexer:DFA)->None:
    lexer.lexerAritmetico(archivo)

import string

if __name__ == '__main__':
    lexer = DFA(
        transition_function = {
            
            "":{**{chr(letter):"Variable" for letter in range(65,91)},**{chr(letter):"Variable" for letter in range(97,123)}, #Capital and lowercase letters
            **{chr(num):"Entero" for num in range(48,58)} #Numbers
            }, 
            "Entero":{".":"Flotante", **{chr(num):"Entero" for num in range(48,58)}},
            "Flotante":None, 
            "Asignación":None, 
            "Suma":None, 
            "Resta":None, 
            "Multiplicación":None, 
            "División":None, 
            "Potencia":None, 
            "Variables":None, 
            "Paréntesis Izquierdo":None, 
            "Paréntesis Derecho":None,
            "Comentario":None
        },
        start_state="",
        accept_states={"Entero","Flotante", "Asignación", "Suma", "Resta", "Multiplicación", 
        "División", "Potencia", "Variables", "Paréntesis Izquierdo", "Paréntesis Derecho","Comentario"}
    )
    from pprint import pprint
    pprint(lexer.transition_function)
    

