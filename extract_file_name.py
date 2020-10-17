def extract_file_name(str):
    str = list(str)
    cpy = str[:]
    dot_count = 0
    dash_count = 0

    for i in range(0,len(str)):
        
        if str[i] == '_': dash_count +=1
        if dash_count == 1:
            cpy = cpy[i+1::]
            break
    print(cpy, "\n")


    for e in range(0,len(cpy)): 
        if cpy[e] == ".": dot_count +=1
        if dot_count == 2:
            cpy = cpy[:e]
            break

    return ''.join(cpy)
