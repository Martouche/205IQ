#!/usr/bin/env python3

import sys, math, time
from sys import stdin
from math import factorial, sqrt, exp, floor, pi

def print_help():
    print("USAGE")
    print("\t./205IQ u s [IQ1] [IQ2]\n")
    print("DESCRIPTION")
    print("\tu mean")
    print("\ts standard deviation")
    print("\tIQ1 minimum IQ")
    print("\tIQ2 maximum IQ")

def first_calcul(x, tab):
    res = (1 / (float(tab[1]) * sqrt(2 * pi))) * exp(-0.5 * pow((float(tab[0]) - float(x)) / float(tab[1]), 2))
    print(x, format(round(res, 5), ".5f"))
    return res

def test_percent(tab, index):
    
def inferior_percent(tab):
    i = 0.0
    res = 0.0
    while (i < tab[2]):
        res = res + (1 / (float(tab[1]) * sqrt(2 * pi))) * exp(-0.5 * pow((float(i) - float(tab[0])) / float(tab[1]), 2))
        i = i + 0.01
    print (format(res, ".1f"), "% of people have an IQ inferior to ", tab[2], sep="")

def middle_percent(tab):
    i = float(tab[2])
    res = 0.0
    while (i < tab[3]):
        res = res + (1 / (float(tab[1]) * sqrt(2 * pi))) * exp(-0.5 * pow((float(i) - float(tab[0])) / float(tab[1]), 2))
        i = i + 0.01
    print (format(res, ".1f"), "% of people have an IQ  between ", tab[2]," and ", tab[3], sep="")

def error_handling():
    tab = []
    i = 1
    try:
        while (i < len(sys.argv)):
            tab.append(int(sys.argv[i]))
            if (tab[i-1] < 0 or tab[i-1] > 200):
                sys.exit(84)
            i += 1
    except:
        print_help()
        exit(84)
    return tab

def loopIQ(tab):
    x = 0
    if len(tab) == 2:
        print(tab)
        while (x <= 200):
            first_calcul(x, tab)
            x += 1
    elif len(tab) == 3:
        inferior_percent(tab)
    elif len(tab) == 4:
        middle_percent(tab)
    i = 0

def main():
    if len(sys.argv) >= 3 and len(sys.argv) <= 5:
        arg = error_handling()
    else:
        return 84
    loopIQ(arg)
    return 0

main()
