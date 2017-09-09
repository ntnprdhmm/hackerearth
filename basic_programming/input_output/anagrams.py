dic_a = {}
dic_b = {}

def string_to_dic(str):
    d = {}
    for c in str:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    return d

def count_letter_to_delete(d1, d2):
    counter = 0
    for k, v in d1.items():
        if k in d2:
            counter += d2[k] - v if v < d2[k] else v - d2[k]
        else:
            counter += v
    for k, v in d2.items():
        if k not in d1:
            counter += v
    return counter

for _ in range(int(input())):
    dic_a = string_to_dic(raw_input())
    dic_b = string_to_dic(raw_input())
    print(count_letter_to_delete(dic_a, dic_b))
