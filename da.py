def decode(message_file):
    with open(message_file,"r") as file:
        data=file.readlines()
    dict={}
    for line in data:
        num,message=int(line.split()[0]), line.split()[1]
        dict[num]=message
    sorted_numbers=sorted(dict.keys())
    message_of_words=""
    i,index=0, 0
    while i<len(sorted_numbers):
        message_of_words+=dict[sorted_numbers[i]]+" "
        index+=1
        i+=index+1
    return message_of_words[:-1]

file_name = "input.txt"
decoded_message = decode("C:\\Users\\rmink\\Documents\\C#\\MovieFiles\\input.txt")
print(decoded_message)