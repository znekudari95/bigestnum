


def createNum(numbers):
    k = ''.join(numbers)
    print(k)

def biggestchar(first_char, strings):
    candidate = []
    big = 9
    while len(candidate) == 0:
        # print(big)
        for i in range(len(first_char)):
            # print(first_char[i])
            if first_char[i] == str(big):
                candidate.append(strings[i])
        big = big - 1
    return candidate

def biggest_num(number):
    total = []
    numbers = [1, 95, 90, 76, 24, 300, 9, 9, 87, 8, 8, 800, 89, 0]
    strings = [str(x) for x in numbers]

    while len(strings) != 0 :
        first_char = [x[0] for x in strings]
        candidate = biggestchar(first_char, strings)
        # print("candidate",candidate)
        # print(strings)
        while len(candidate) != 0 :
            maxlen = max([len(x) for x in candidate])
            revisedcandidate = [x for x in candidate if len(x) == maxlen]
            revisedcandidate_index = [candidate.index(x) for x in candidate if len(x) == maxlen]
            for i in range(len(candidate)):
                for j in range(len(candidate)):
                    if i != j :
                        new = candidate[i] + candidate[j]
                        if len(new) == maxlen:
                            revisedcandidate.append(new)
                            revisedcandidate_index.append([i, j])
            # print(revisedcandidate)
            # print(revisedcandidate_index)
            max_value = revisedcandidate.index(max([x for x in revisedcandidate]))
            total.append(revisedcandidate[max_value])
            delitemval = []
            if isinstance(revisedcandidate_index[max_value], list):
                delitemval = [candidate[x] for x in revisedcandidate_index[max_value]]
            else:
                delitemval .append( candidate[revisedcandidate_index[max_value]])
            # print("delval",delitemval)
            for i in delitemval:
                # print(i)
                # print(candidate)
                candidate.remove(i)
                strings.remove(i)
            del(revisedcandidate[max_value])
            del(revisedcandidate_index[max_value])
            # print(revisedcandidate)
            # print(revisedcandidate_index)
            # print(total)
    createNum(total)