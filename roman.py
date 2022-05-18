# Keys for str of roman digits
dict = {
"I" : 1,
"V" : 5,
"X" : 10,
"L" : 50,
"C" : 100,
"D" : 500,
"M" : 1000
}
rez = []
rez2 = []
def roman(str):
    for i in range(0, len(str)):
        if str[i] in dict.keys():
            rez.append(dict[str[i]])
    if len(str) == 1:
        return dict[str]
    for i in range(0, len(rez)):
        j = i + 1
        if j <= len(rez) - 1:
            if rez[i] > rez[j]:
                rez2.append(rez[i])
                if j == len(rez) - 1:
                    rez2.append(rez[j])
            elif rez[i] < rez[j]:
                rez2.append(rez[j]-rez[i])
                del(rez[j])
                # append for limit index of rez
                rez.append(0)
            elif rez[i] == rez[j]:
                rez2.append(rez[i])
                if j == len(rez) - 1:
                    rez2.append(rez[j])
        else:
            break
    return sum(rez2)

str ="XIV"
print(roman(str))