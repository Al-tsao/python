try: #有:後一定要縮排
    number = int(input("Enter a number: "))
    print(f'Your number is {number}')
except ValueError: #也可以直接寫except後面不用加任何東西，這樣任何錯都會被except
    print('輸入格式錯誤，請輸入數字')