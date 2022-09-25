def read_all():
    token = open('token.txt', "r")
    read_all = token.readlines()
    total_token = len(read_all)
    print(total_token)

read_all()

#credit Meoaw
