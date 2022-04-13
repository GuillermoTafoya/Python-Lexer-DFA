class DFA:
    def __init__(self, transition_function:dict, start_state:str, accept_states:set)->None:
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states
        self.current_state = self.start_state

    def is_accepted(self, string:str)->bool:
        current_state = self.start_state
        for char in string:
            current_state = self.transition_function[current_state][char]
        return current_state in self.accept_states

    def __str__(self):
        return "DFA: {}".format(self.transition_function)
    def lexerAritmetico(self, string:str)->list:
        ### EDITAR ESTO ###
        pass

    

def lexerAritmetico(archivo:str,lexer:DFA)->None:
    lexer.lexerAritmetico(archivo)

if __name__ == '__main__':
    
    lexer = DFA(
        transition_function = {
            
            "":{

                **{chr(letter):"Variable" for letter in range(65,91)},      # Capital letters
                **{chr(letter):"Variable" for letter in range(97,123)},     # Lowercase letters
                **{chr(num):"Entero" for num in range(48,58)},              # Numbers
                "+": "Suma",
                "-": "Resta",
                "*": "Multiplicacion",
                "/": "Division",
                "^": "Potencia",
                "(": "Parentesis Izquierdo",
                ")": "Parentesis Derecho",
                "=": "Asignacion"
            }, 

            "Entero":{
                ".":"Flotante", 
                **{chr(num):"Entero" for num in range(48,58)},              # Numbers
                "+": "Suma",
                "-": "Resta",
                "*": "Multiplicacion",
                "/": "Division",
                "^": "Potencia"

            },
            "Flotante":{
                **{chr(num):"Flotante" for num in range(48,58)},              # Numbers
                "+": "Suma",
                "-": "Resta",
                "*": "Multiplicacion",
                "/": "Division",
                "^": "Potencia",
            }, 

            "Asignación":None, 
            "Suma":None, 
            "Resta":None, 
            "Multiplicación":None, 

            "División":{
                "/":"Comentario", 
                **{chr(letter):"Variable" for letter in range(65,91)},      # Capital letters
                **{chr(letter):"Variable" for letter in range(97,123)},     # Lowercase letters
                **{chr(num):"Entero" for num in range(48,58)},              # Numbers
                "+": "Suma",
                "-": "Resta",
                "*": "Multiplicacion",
                "/": "Division",
                "^": "Potencia",
                "(": "Parentesis Izquierdo",
                ")": "Parentesis Derecho",
                "=": "Asignacion"
            },

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
    

