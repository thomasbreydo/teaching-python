user_n = int(input("What's ur n? "))  # 3
user_n_multiples = int(input("What's ur n_multiples? "))  # 7

def func(n, n_multiples):
    for i in range(1, n_multiples + 1):
        print(n * i)


func(user_n, user_n_multiples)