salary = int(input("your salary: "))
quit_confirm = ''
goods_items = ["apple","orange","banana"]
price_items = [30,40,50]
select_items = []
while True:
    print(
       "---------- goods --------------" +"\n"+
       "1 apple  30"+"\n"+
       "2 orange  40" + "\n" +
       "3 apple  50" + "\n"
    )
    number = input("请按菜单输入您需要的货号,退出请按'q'键")
    if number!="q":
        number = int(number)
        try:
            select_items.append(price_items[number-1])
        except Exception as e:
            print("您输入的货号不存在,请重新输入!~")
            continue
        all = sum(select_items)
        if all > salary:
            print("余额不足,请删除后重试!~")
            remove_number = input("您想删除的货号是:")
            select_items.remove(price_items[int(remove_number)])
    else:
        print("------",select_items,"________")
        for i in select_items:
            print(goods_items[select_items.index(i)])
        break



