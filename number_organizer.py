
# ask user to input numbers and name
while True: #loop1: asking users name and number
    try: 
        name = input("Enter your name (LETTERS ONLY): ")
        if not name.isalpha():
            raise ValueError ("letters only")
 
        num_range = {
            "1-10" : 0,
            "11-20" : 0,
            "21-30" : 0,
            "31-40" : 0,
            "41-50" : 0
            }
            
        while True: #loop2: for user entering number
            try: 
                num = int(input("Enter a number (1 to 50 only): "))
                if (num>=1) and (num<=50): #putting the numbers in range using if else
                    if (num>=1) and (num<=10):
                        num_range["1-10"] += 1 
                    elif (num>=11) and (num<=20):
                        num_range["11-20"] += 1
                    elif (num>=21) and (num<=30):
                        num_range["21-30"] += 1
                    elif (num>=31) and (num<=40):
                        num_range["31-40"] += 1
                    elif (num>=41) and (num<=50):
                        num_range["41-50"] += 1
                else:
                    break

            except:
                print("invalid input")
                break
            
        #printing all the numbers total
        print("Numbers for:", name)
        print("1-10:", num_range["1-10"])
        print("11-20:", num_range["11-20"])
        print("21-30:", num_range["21-30"])
        print("31-40:", num_range["31-40"])
        print("41-50:", num_range["41-50"])
        break

    except ValueError as error:
        print ("invalid:", error)
