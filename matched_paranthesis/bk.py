import os

n = input("enter value for n: ")

final_list = []
ref_dict = {'open':'(', 'close':')'}
opn1 = n
close1 = n
opn2 = n
close2 = n
temp_str = ''
temp_str1 = ''
def type1(opn1,close1):
    global temp_str, final_list
    if opn1 ==0 and close1 == 0:
        final_list.append(temp_str)
        return temp_str
    if opn1 >= close1:
        temp_str += ref_dict['open']
        opn1 = opn1 - 1
        print(temp_str)
        print("pass3")
        # input()
        type1(opn1,close1)
    elif opn1 < close1:
        if opn1:
            temp_str += ref_dict['open']
            opn1 = opn1 - 1
            print(temp_str)
            print("pass2")
            # input()
            type1(opn1,close1)
        elif close1:
            temp_str += ref_dict['close']
            close1 = close1 - 1
            print(temp_str)
            print("otha")
            print(opn1,close1)
            # input()
            type1(opn1,close1)
    

def type2(opn2,close2):
    global temp_str1, final_list
    if opn2 and close2 == 0:
        final_list.append(temp_str1)
        return temp_str1
    if opn2 >= close2:
        val = type1(opn2,close2)
        final_list.append(val)

        # temp_str1 += ref_dict['open']
        opn2 = opn2 - 1
        type2(opn2,close2)
    elif opn2 < close2:
        if opn2:
            type1(int(opn2),int(close2))
        temp_str1 += ref_dict['close']
        close2 = close2 - 1
        type2(opn2,close2)
    

# print(type1(int(opn1),int(close1)))
print(type2(int(opn2), int(close2)))

print(final_list)
