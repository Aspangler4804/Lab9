#Austin Spangler

if __name__ == '__main__':
    def Encode():
        EncodedPswrd = ""
        for i in Pswrd:
            update = int(i) + 3
            if update < 10:
                update = str(update)
            else:
                if update == 10:
                    update = "1"
                if update == 11:
                    update = "2"
                if update == 12:
                    update = "3"
            EncodedPswrd += (update)
        print(EncodedPswrd)

    while True:

        print("Menu")
        print("_____________")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        userchoice = input("Please enter an option:")
        if userchoice == 1:
            Pswrd = (input("Please enter an 8 digit password:"))

            try:
                if len(Pswrd) == 8:
                    break
                else:
                    print("Please enter your password to encode:")
            except ValueError:
                print("Please enter a valid password")
            print("Your password has been encoded and stored!")
            Encode(Pswrd)


        if userchoice == 3:



