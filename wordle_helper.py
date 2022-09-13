from pprint import pprint

class Wordle(object):
    # TODO get the raw input at __init_ and store
    # in the object. Make a nice lil __repr__ an stuff

    def get_inputs(self):
        letters = input("which letters are still possible?")
        known = input("which strings are known?")

        clean_data = self.process_input(letters, known)

        return clean_data


    def process_input(self, *args):
        available_letters = args[0]
        available_letters = available_letters.replace(" ", "")
        available_letters = list(available_letters)

        empty_slots = args[1]
        empty_slots = list(empty_slots)

        # get the index location for the empty letter slots
        index_a = -1
        index_b = -1

        # TODO add the index of the empty spots in the 'empty slots' 
        # array and save to dict. This is a stub...
        for item in empty_slots:
            if (item == '_') & (index_a > 0):
                index_b += 1
                continue
            if item == '_':
                index_a += 1

        return {'available_letters': available_letters, 'empty_slots': empty_slots, 'index_a': index_a, 'index_b': index_b}
        

    def get_combos(self, data_dict):
        """takes a dict and returns a list of 5 char strings
        representing possible solutions to the puzzle"""
        possible_combos = []

        for each_letter_1 in data_dict["available_letters"]:
            possible_combos.append(self.stringify_the_combo(data_dict["empty_slots"], each_letter_1, each_letter_2))
            for each_letter_2 in data_dict["available_letters"]:
                possible_combos.append(self.stringify_the_combo(data_dict["empty_slots"], each_letter_1, each_letter_2))


    def stringify_the_combo(data_dict, index_1, index_2):
        """Takes some list data and does list magic to place strings at the 
        correct index in the list, then stringifies it"""
        # TODO
        return possible_word


    def validate_input():
        # TODO
        # There's no input validation or helpful message returned to user yet
        return 

if __name__ == "__main__":
    wordle = Wordle()
    user_input = wordle.get_inputs()
    pprint(user_input)
    # possible_combos = wordle.get_combos(data_dict=user_input)
    # pprint(possible_combos)