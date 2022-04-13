class DFA:
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states

    def is_accepted(self, string):
        current_state = self.start_state
        for char in string:
            current_state = self.transition_function[current_state][char]
        return current_state in self.accept_states

    def __str__(self):
        return "DFA: \n\tStates: {}\n\tAlphabet: {}\n\tTransition Function: {}\n\tStart State: {}\n\tAccept States: {}".format(
            self.states, self.alphabet, self.transition_function, self.start_state, self.accept_states)

    

def lexerAritmetico(archivo:str)->None:
    pass


if __name__ == '__main__':
    lexerAritmetico("test.txt")
    

