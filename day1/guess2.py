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

    if count == 3:
        continue_confirm  = input("do you want to keep guessing?")
        if continue_confirm != "n":
            count = 0

else:
    print("次数用完了")


