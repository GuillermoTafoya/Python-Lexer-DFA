class DFA:
    def __init__(self, states:set, alphabet:list, transition_function:dict, start_state:int, accept_states:set)->None:
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states

    def is_accepted(self, string:str)->bool:
        current_state = self.start_state
        for char in string:
            current_state = self.transition_function[current_state][char]
        return current_state in self.accept_states

    def __str__(self):
        return "DFA: \n\tStates: {}\n\tAlphabet: {}\n\tTransition Function: {}\n\tStart State: {}\n\tAccept States: {}".format(
            self.states, self.alphabet, self.transition_function, self.start_state, self.accept_states)

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


if __name__ == '__main__':
    #lexer = DFA(
    
    
    lexerAritmetico("test.txt",lexer)
    

