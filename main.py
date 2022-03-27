while True:
    main = input("足し算なら1 引き算なら2\n掛け算なら3 割り算なら4 と入力してください")
    if main == "1":
        first = int(input("最初の数字を入力してください"))
        second = int(input("二つ目の数字を入力してください"))
        print(first + second)
    elif main == "2":
        first = int(input("最初の数字を入力してください"))
        second = int(input("二つ目の数字を入力してください"))
        print(first - second)
    elif main == "3":
        first = int(input("最初の数字を入力してください"))
        second = int(input("二つ目の数字を入力してください"))
        print(first * second)
    elif main == "4":
        first = int(input("最初の数字を入力してください"))
        second = int(input("二つ目の数字を入力してください"))
        print(first / second)
