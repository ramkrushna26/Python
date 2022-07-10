
from datetime import datetime
start = datetime.now()
 
def anagram(st):
    st_len = int(len(st)/2)
    
    first_half = st[:st_len]
    sec_half = st[st_len:]
    first_dict = {}
    sec_dict = {}
    counter = 0

    for i in first_half:
        if i in first_dict.keys():
            first_dict[i] += 1
        else:
            first_dict[i] = 1

    for i in sec_half:
        if i in sec_dict.keys():
            sec_dict[i] += 1
        else:
            sec_dict[i] = 1

    for i,j in sec_dict.items():
        if i in first_dict.keys():
            if first_dict[i] > j:
                continue
            else:
                counter += j - first_dict[i]
        else:
            counter += j

    return counter


if __name__ == '__main__':
    
    print("===Anagram Digits===")
    s = '12345644'

    print(anagram(s))
    print("===Time taken: {} microseconds===".format((datetime.now()-start).microseconds))
