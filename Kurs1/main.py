# coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press Ctrl+F8 to toggle the breakpoint.

def Med(list):
    return float(sum(list)) / float(len(list))


def ingroup(llist):
    list2 = []
    res = 0
    for list in llist:
        M = Med(list)
        sum = 0
        for j in list:
            sum += (j - M)*(j - M)
        sum /= float(len(llist) - 1)
        res += sum

    return res * 1/float(len(llist))




def intergroup(llist):
    res = 0.0
    list = []
    for i in llist:
        sum = Med(i)
        list.append(sum)
    med = Med(list)
    sum = 0
    for j in list:
        sum += (j - med) * (j - med)
    sum /= float(len(llist) - 1)

    return sum * float(len(list))


def Fisher(llist):
    return float(intergroup(llist)) / float(ingroup(llist))


def broadcasting_app(a, L, S ):  # Window len = L, Stride len/stepsize = S
    result_matrix = np.zeros((S, L))
    for i in range(0, S, 1):
        for j in range(0, L, 1):
            result_matrix[i][j] = a[i*L + j]
    return result_matrix


OutY2 = []
OutY3 = []

f1 = open('wave_ampl.txt')
for i in f1:
    OutY2.append(float(i))

OutY3 = OutY2
for i in range(1, len(OutY2) - 1, 1):
    OutY3[i] = (OutY2[i - 1] + OutY2[i + 1])/2

#fig, ax = plt.subplots()


Cy4 = broadcasting_app(OutY2, 256, 4)
Cy8 = broadcasting_app(OutY2, 128, 8)
Cy16 = broadcasting_app(OutY2, 64, 16)
a = Cy4
for i in range(0, 4):
    f1 = Fisher(broadcasting_app(a[i], 64, 4))
    print(str(f1) + " " + str(i))
    #if f1 > 2:
    #    ax.add_patch(Rectangle((i*256, -1), 256, 1, color="yellow"))
print("______")

a = Cy8
for i in range(0, 8):
    f1 = Fisher(broadcasting_app(a[i], 32, 4))
    print(str(f1) + " " + str(i))
    #if f1 > 2:
    #    ax.add_patch(Rectangle((i*128, -1), 128, 0.9, color="green"))
print("______")
a = Cy16
for i in range(0, 16):
    f1 = Fisher(broadcasting_app(a[i], 16, 4))
    print(str(f1) + "")
    #if f1 > 2:
    #    ax.add_patch(Rectangle((i*64, -1), 64, 0.8, color="blue"))


