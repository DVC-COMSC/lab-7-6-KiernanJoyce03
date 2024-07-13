
def getInput():
    """
    ########################################
    Code Your Program here
    ########################################
    """
    userInput = input("Input a list of numbers ")
    numbers = list(userInput.split())
    for i in range (len(numbers)):
        numbers[i] = int(numbers[i])
    
    return numbers
    

def makeReverse(numbers):
    """
    ########################################
    Code Your Program here
    ########################################
    """
    N = len(numbers)
    ret = []
    for i in range (N ):
        
        ret.insert(0,numbers[0])
        numbers.pop(0)
        

        
    
    return ret
    


def main():
    numbers = getInput()
    ret = makeReverse(numbers)
    print(f'The result values are: {ret}')


if __name__ == '__main__':
    main()
