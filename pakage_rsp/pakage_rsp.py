CHOICE_LIST = ['r','s','p']

def get_user_choice():
    choice =input("Enter your choice between r s p :")
    if choice not in CHOICE_LIST:
        print('invalid choice again:')
        return get_user_choice()
    return choice  