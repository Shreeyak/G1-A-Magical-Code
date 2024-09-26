from math import factorial


MAX_MSG_LEN = 5

def base_x(base, num):
    ret = ""
    length = 0

    while num:
        length += 1
        remainder = num%base
        ret = str(remainder) + ", " + ret
        num = num // base

    return ret, length


def eq(x, coefficients):
    y = 0
    if len(coefficients) != MAX_MSG_LEN:
        print("ERROR: STRING NOT MAX_MSG_LEN SIZED")
        return

    for i in range(MAX_MSG_LEN):
        c = coefficients[i]
        y += c * x**(MAX_MSG_LEN - 1 - i)

    return y


# space = 0
# char = 1 thru 26

def test(string):
    seen_dict = {}
    for i in range(10):
        seen_dict[str(i)] = 0

    if len(string) > MAX_MSG_LEN:
        print("ERROR: STRING TO BIG")
        return
    
    str_as_num = []
    for ch in string:
        num = ord(ch)
        
        if num == 32:
            num = 0
        else:
            num -= 96
        
        str_as_num.append(num)
    
    str_as_num += [1 for _ in range(MAX_MSG_LEN - len(string))]

    over_4_set = set()
    free_digits_left = 40

    cntr = 0

    tot_len = 0

    for i in range(50):
        num = str(eq(i, str_as_num))
        if len(num) > free_digits_left:
            break

        skip_num = False

        temp_dict_for_word = {}

        for digit in num:
            if digit not in temp_dict_for_word:
                temp_dict_for_word[digit] = 0
            
            temp_dict_for_word[digit] += 1

            if digit in over_4_set or temp_dict_for_word[digit] + seen_dict[digit] > 4:
                skip_num = True
                break
        
        if not skip_num:
            for digit in temp_dict_for_word.keys():
                seen_dict[digit] += temp_dict_for_word[digit]
                free_digits_left -= temp_dict_for_word[digit]

                if seen_dict[digit] >= 4:
                    over_4_set.add(digit)

                if len(over_4_set) >= 10:
                    '''print("here")
                    print("--------------------------------------------------------")
                    print("card_encoding_len = " + str(tot_len + cntr - 1))
                    print("valid cords = " + str(cntr))'''
                    return tot_len + cntr - 1, cntr # card_encoding_len, valid cord count

        if not skip_num:
            # print(num)
            tot_len += len(num)
            cntr += 1
        # else:
            # print("skip for x = " + str(i) + " | ----> " + num)
        
    '''print("--------------------------------------------------------")
    print("card_encoding_len = " + str(tot_len + cntr - 1))
    print("valid cords = " + str(cntr))'''
    return tot_len + cntr - 1, cntr # card_encoding_len, valid cord count

if __name__ == "__main__":
    ret, length = base_x(20, (26) ** 8)
    #print(ret)
    #print(length)
    letters = ["a", "b", "c", "d", 'e', "f", "g", "h", 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    cord_count_more_than_5_count = 0
    cord_count_less_than_5_count = 0

    for length in range(MAX_MSG_LEN):
        test_str = ""
        for ch1 in letters:
            for ch2 in letters:
                for ch3 in letters:
                    for ch4 in letters:
                        for ch5 in letters:
                            test_str = ch1 + ch2 + ch3 + ch4 + ch5
                            print(test_str[:length + 1])
                            encoding_len, cord_count = test(test_str[:length + 1])
                            if cord_count >= MAX_MSG_LEN:
                                cord_count_more_than_5_count += 1
                            else:
                                cord_count_less_than_5_count += 1


                            if length + 1 < 5:
                                break
                        
                        if length + 1 < 4:
                            break
                    
                    if length + 1 < 3:
                        break

                if length + 1 < 2:
                        break

    print(cord_count_more_than_5_count / (cord_count_more_than_5_count + cord_count_less_than_5_count))

    





