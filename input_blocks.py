try:
    from keywords import keywords,blocknames
except ImportError:
    print("No keywords.py module found! Check your installation")
    exit(1)





class WrongKeywordError(Exception):
    def __init__(self, message, wrong_keyword):
        self.wrong_keyword = wrong_keyword
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message} {self.wrong_keyword} !!!'


def check_keyword(input, kws = keywords):
    if not isinstance(input, str):
        input = str(input)
    for kw in kws:
        if kw[0] == input.lower():
            return kw
        else:
            continue
    raise WrongKeywordError("Wrong keyword: ", input)



class InputBlock:
    def __init__(self, args):
        self.args, self.block = args, []
        if self.args[0] not in blocknames:
            raise WrongKeywordError("Wrong block name: ", self.args[0])
        else:
            self.block.append(f"%{self.args[0]}\n")


    def make_block(self):
        enum = enumerate(self.args[1:])
        for i, a in enum:

            if check_keyword(a, keywords)[1] == 0:
                self.block.append(f"\t{a} {self.args[i + 2]}\n")
                next(enum)

            elif check_keyword(a, keywords)[1] == 1:
                counter = 1
                while counter > 0:
                    try:
                        try:
                            if check_keyword(self.args[i + 1 + counter], keywords):
                                self.block.append(f"\t{a}\n")
                                for indx in range(i+2, i+1+counter):
                                    self.block.append(f"\t\t{self.args[indx]}\n")
                                    next(enum)
                                counter = 0
                        except IndexError:
                            # Add levenstein check for more elaborate wrong keyword interception
                            print(f"Watch out! Some of keywords in the %{self.args[0]} block are wrong!!!")
                            exit(1)
                    except WrongKeywordError:
                        counter += 1
                self.block.append("\t\tend\n")

            elif check_keyword(a, keywords)[1] == 3:
                print("Sorry! This keyword is not supported yet :(")

        self.block.append("\tend\n")
        return self.block






