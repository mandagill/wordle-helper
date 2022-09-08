from pprint import pprint

class Wordle(object):
    # TODO get the raw input at __init_ and store
    # in the object. Make a nice lil __repr__ an stuff

    def get_inputs(self):
        letters = input("which letters are still possible?")
        known = input("which strings are known?")

        unused_letters, known_combos = self.process_input(letters, known)

        return {'unused_letters': unused_letters, 'known_combos': known_combos}

    def get_combos(self, data_dict):
        """takes a dict and returns a list of 5 char strings
        representing possible solutions to the puzzle"""
        
        pass


    def process_input(self, *args):
        available_letters = args[0]
        available_letters.replace(" ", "")
        available_letters = list(available_letters)

        empty_slots = args[1]
        empty_slots = list(empty_slots)

        return available_letters, empty_slots

    def validate_input():
        # TODO
        # There's no input validation or helpful message returned to user yet
        return 

if __name__ == "__main__":
    wordle = Wordle()
    user_input = wordle.get_inputs()
    pprint(user_input)
    possible_combos = wordle.get_combos(data_dict=user_input)
    pprint(possible_combos)