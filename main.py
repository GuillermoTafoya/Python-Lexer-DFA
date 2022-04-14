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
                **{chr(num):"Entero" for num in range(48,58)},      # Numbers

            },
            "Flotante":{
                **{chr(num):"Flotante" for num in range(48,58)},    # Numbers
                "E": "Exponente"
            }, 
            "Exponente":{
                "-": "Flotante",
                **{chr(num):"Flotante" for num in range(48,58)}     # Numbers
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
    with open("test.txt", "r") as file:
        result = lexer.lexerAritmetico(file.read())
    # Save the result in a text file as string pairs
    with open("result.txt", "w") as file:
        for token in result:
            file.write("{},{}\n".format(token[0], token[1]))

