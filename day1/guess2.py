age = 20

count = 0


while count<3:

    guess_age = int(input("you guess age: "))

    if guess_age == age:
        print("win")
        break
    elif guess_age > age:
        print("bigger")
    else:
        print("smaller")

    count+=1

else:
    print("次数用完了")


