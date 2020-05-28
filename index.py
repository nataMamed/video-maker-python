

def start():
    content = {}

    def askAndReturnSearchTerm():
        return input('Type a Wikepedia term: ')

    def askAndReturnPrefix():
        prefixes = ['Who is','What is','The history of']
        choice = int(input("""Which one do you choose:
        [1] Who is
        [2] What is 
        [3] The history of """))

        return prefixes[choice - 1]

    content['serchTerm'] = askAndReturnSearchTerm()
    content['prefix'] = askAndReturnPrefix()
    print(content)


start()