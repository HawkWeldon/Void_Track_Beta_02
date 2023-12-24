def fx(input):
    input = input.replace("'","")
    input = input.replace("[","")
    input = input.replace("]","")
    ouput = input.split(",")
    return ouput