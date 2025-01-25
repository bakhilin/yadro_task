# task python YADRO devOps

def count_s(str1):
    count_str = ""
    count = 1
    for i in range(1, len(str1)):
        if str1[i] == str1[i-1]:
            count += 1
        else:
            count_str += str1[i-1] + str(count)
            count = 1

    print(count_str+str1[-1] + str(count))
        
        
count_s("АААБББ3333А")