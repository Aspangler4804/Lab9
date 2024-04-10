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
        Pswrd = (input("Please enter an 8 digit password:"))

        try:
            if len(Pswrd) == 8:
                break
            else:
                print("Please enter a valid password")
        except ValueError:
            print("Please enter a valid size")
    Encode(Pswrd)

