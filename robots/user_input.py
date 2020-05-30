

def user_input():


    def ask_and_return_prefix():
        prefixes = ['Who is','What is','The history of']
        choice = int(input(
                """Which one do you choose:
                    [1] Who is
                    [2] What is 
                    [3] The history of """))

        return prefixes[choice - 1]

    def join_contents() -> dict:

        content = {
                'searchTerm': input('Type a Wikepedia term: '),
                'prefix': ask_and_return_prefix()
                }

        return content

    return join_contents()

