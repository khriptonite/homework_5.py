

def get_user_friends():
    num = int(input("The number of friends you want to put?: "))
    friends = ""
    sep     = ""
    friend  = ""
    n = 1
    while n <= num:
        if n == num:
            sep = "."
        else:
            sep = ", "
        friend   = input("Input a name of your friend: ")
        friends += friend + sep
        n += 1
    print("Here's the list of your friends: ", friends)

get_user_friends()