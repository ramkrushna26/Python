
# Write a code to find all possible pairs of number in list having sum = 2
# Time complexity should be less O(n^2)

def tuples_with_target_sum(input_list, target_sum):
    target_pairs = []
    complement_num = 0
    set_list = set(input_list)
    
    for num in input_list:
        complement_num = target_sum - num

        if complement_num in set_list:
            target_pairs.append((num, complement_num))
            set_list.remove(num)
            if complement_num in set_list:
                set_list.remove(complement_num)

    return target_pairs


input_list = [2,1,4,-1,0,-2,-1,2,1,3]
target_sum = 2

print(tuples_with_target_sum(input_list, target_sum))
