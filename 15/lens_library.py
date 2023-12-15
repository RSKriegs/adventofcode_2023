if __name__=="__main__":

    with open("data/input_15.txt", "r") as file:
        items = file.read().rstrip().split(',')
    
    result = 0 
    for item in items:
        temp = 0
        for string in item:
            temp = (temp + ord(string)) * 17 % 256
        result += temp
    
    # Part 1
    print(result)