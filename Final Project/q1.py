"""
Kya Miller
LING 539 Assignment 6 - Final Project
Q1 -
"""

goldDataFileIn = open('goldData/index.txt', 'r')
goldDataLines = goldDataFileIn.readlines()
goldDataFileIn.close()

goldDataLabels = []
for line in goldDataLines[:3000]:
    splitLine = line.split(' ', 1)
    label = splitLine[0]
    goldDataLabels.append(label)
