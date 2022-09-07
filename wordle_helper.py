from pprint import pprint

class Wordle(object):

    def get_inputs(self):
        letters = input("which letters are still possible?")
        unused_letters = list(letters)

        slots = input("which letters have unknown values, between 1 and 5?")
        unknown_slots = tuple(slots)

        known_combos = input("which strings are known?")

        return {'unused_letters': unused_letters, 'unknown_slots': unknown_slots, 'known_combos': known_combos}

    def possible_combos(self):
        # TODO
        pass


    def validate_input(args):
        # TODO
        return 



if __name__ == "__main__":
    wordle = Wordle()
    user_input = wordle.get_inputs()
    pprint(user_input)
    # possible_combos = return_combos(user_input)
    # pprint(possible_combos)