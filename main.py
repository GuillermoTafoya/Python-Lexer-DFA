""" 
Actividad 3.2 Programando un DFA

Integrantes:
Guillermo Tafoya Milo - A01633790
Engels Emiliano Miranda Palacios - A01423398
Jorge Hernández Montero - A01733616

Fecha: 13 de marzo del 2022 
"""

""" 
NOTA IMPORTANTE: Profe, no pudimos subir ni el
PDF con la documentación ni el test.txt ni el
resultados.txt porque solo deja subir archivos
.py, pero aquí le dejamos el link del git con
todo lo anteriormente mencionado:

https://github.com/GuillermoTafoya/Python-Lexer-DFA

Sin más, gracias por su atención, todo quedó como
pidió así que esperamos nuestro 100 :D
 """

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
        tokens = []
        pastStates = []
        idx = 0
        currentSubString = ""
        self.current_state = self.transition_function[self.current_state][string[idx]]
        while idx < len(string):

            if string[idx] in self.transition_function[self.current_state]:
                currentSubString += string[idx]
                
                self.current_state = self.transition_function[self.current_state][string[idx]]
                idx += 1
                pastStates.append(self.current_state)
            elif string[idx] == " " or string[idx] == "":
                if self.current_state == "Comentario":
                    currentSubString += string[idx]
                idx += 1
            else:
                if currentSubString:
                    tokens.append((self.current_state, currentSubString))
                self.current_state = self.start_state
                currentSubString = ""
                if string[idx] == "\n":
                    idx += 1
        if currentSubString:
                    tokens.append((self.current_state, currentSubString))
        return tokens


    

def lexerAritmetico(archivo:str,lexer:DFA)->None:
    lexer.lexerAritmetico(archivo)

import sys
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
                ".":"Real", 
                **{chr(num):"Entero" for num in range(48,58)},      # Numbers

            },
            "Real":{
                **{chr(num):"Real" for num in range(48,58)},    # Numbers
                "E": "Exponente",
                "e": "Exponente"
            }, 
            "Exponente":{
                "-": "Real",
                **{chr(num):"Real" for num in range(48,58)}     # Numbers
            },


            # Operadores y parentesis
            "Asignacion":dict(), 
            "Suma":dict(), 
            "Resta":dict(), 
            "Multiplicacion":dict(), 
            "Division":{
                "/":"Comentario"
            },
            "Potencia":dict(),
            "Parentesis Izquierdo":dict(), 
            "Parentesis Derecho":dict(),
            
            "Variable":{
                **{chr(letter):"Variable" for letter in range(65,91)},      # Capital letters
                **{chr(letter):"Variable" for letter in range(97,123)},     # Lowercase letters
                **{chr(num):"Variable" for num in range(48,58)},            # Numbers
                "_": "Variable"

            }, 
            
            "Comentario":{
                **{chr(letter):"Comentario" for letter in range(65,91)},      # Capital letters
                **{chr(letter):"Comentario" for letter in range(97,123)},     # Lowercase letters
                **{chr(num):"Comentario" for num in range(48,58)},            # Numbers
                "+": "Comentario",
                "-": "Comentario",
                "*": "Comentario",
                "/": "Comentario",
                "^": "Comentario",
                "(": "Comentario",
                ")": "Comentario",
                "=": "Comentario"
            },

            "Fin de Estado":None
        },

        start_state="",

        accept_states={"Fin de Estado"}
    )
    
    _, ifile, ofile = sys.argv
    
    with open(ifile, "r") as file:
        result = lexer.lexerAritmetico(file.read())
    # Save the result in a text file as string pairs
    with open(ofile, "w") as file:
        file.write("Token,Tipo\n")
        for token in result:
            file.write("{},{}\n".format(token[1], token[0]))

