class SimpleExample():
    def __init__(self):
        return None

    def run(self):
        print("start program")
        a = True
        count = 0
        phrase = ""
        while(a == True):
            input1 = input("enter q to quit,i for info,d to display, anything else to be stored\n")
            count = count + 1
            if input1 == "q":
                a = False
            elif input1 == "i":
                print(str(count))
            elif input1 == "d":
                print(phrase)
            else:
                phrase = phrase + input1 + " "
        print("End program")


def __main__():
    Example = SimpleExample()
    Example.run()

if __name__ == "__main__":
    __main__()
    
             
        
            
