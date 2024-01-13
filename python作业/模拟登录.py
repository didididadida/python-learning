

dic = {"aaa": ["123456", 10000], "bbb": ["888888", 5000], "ccc": ["333333", 3000]}
# dic.keys()
# print(dic.keys())
# print(dic.values())

i = 0
use = input()
if use not in dic.keys():
    print('Wrong User')
else:
    for i in range(0, 3):
        i += 1

        na = input()
        if dic[use][0] == na:
            print("Success")
            break
        else:
            ga: int = 3 - i
            if ga == 0:
                print("Login Denied")
            else:
                print("Fail," + str(ga) + ' Times Left')

