"""
Kya Miller
LING 539 Assignment 3
Q2 - Simulates a simple Hidden Markov Model for a 3 word, 3 POS tag language. {w1, w2, w3}, {tag1, tag2, tag3}
Finds all possible 3 word sentences. Finds most probable tag sequence for each sentence.
Saves output and emission/transmission probabilities to hmm_output.txt.

transitions matrix
        tag1  tag2  tag3
start   0.3   0.5   0.2
tag1    0.2   0.6   0.2
tag2    0.3   0.3   0.4
tag3    0.1   0.8   0.1

emissions matrix
        w1  w2  w3
tag1    0.3 0.1 0.6
tag2    0.5 0.3 0.2
tag3    0.1 0.7 0.2
"""

import itertools


def getAllSentences():
    # the words list needs to have w1 and w2 repeated after w3, or else itertools won't consider a combination where
    # w1 or w2 can appear after w3
    words = ['w1', 'w2', 'w3', 'w2', 'w1']
    allSentencesObject = itertools.combinations_with_replacement(words, 3)

    # however, because it still counts those repeated w1 and w2 as separate objects, you will get repeats. So filter
    # out the repeats.
    allSentencesFilteredList = []
    for sentence in allSentencesObject:
        if sentence not in allSentencesFilteredList:
            allSentencesFilteredList.append(sentence)

    return allSentencesFilteredList


def getAllPossiblePaths():
    # this works exactly the same as the getAllSentences function, just has a different list.
    states = ['tag1', 'tag2', 'tag3', 'tag2', 'tag1']
    allPathsObject = itertools.combinations_with_replacement(states, 3)

    allPathsFiltered = []
    for path in allPathsObject:
        if path not in allPathsFiltered:
            allPathsFiltered.append(path)

    return allPathsFiltered


transitionsMatrix = [
    [0.2, 0.6, 0.2],
    [0.3, 0.3, 0.4],
    [0.1, 0.8, 0.1]
]

emissionsMatrix = [
    [0.3, 0.1, 0.6],
    [0.5, 0.3, 0.2],
    [0.1, 0.7, 0.2]
]

transitionsMappingDictionary = {'tag1': 0, 'tag2': 1, 'tag3': 2}
emissionsMappingDictionary = {'tag1': 0, 'tag2': 1, 'tag3': 2, 'w1': 0, 'w2': 1, 'w3': 2}

allSentences = getAllSentences()
allPossiblePaths = getAllPossiblePaths()

for sentence in allSentences:
    pathProbs = []
    for path in allPossiblePaths:
        # get transitions probability
        pathTransitionProb = 1

        if path[0] == 'tag1':
            pathTransitionProb *= 0.3
        elif path[0] == 'tag2':
            pathTransitionProb *= 0.5
        else:
            pathTransitionProb *= 0.2

        for i in range(len(path) - 1):
            currentState = path[i]
            currentStateIndex = transitionsMappingDictionary[currentState]
            nextState = path[i + 1]
            nextStateIndex = transitionsMappingDictionary[nextState]
            transitionProb = transitionsMatrix[currentState][nextState]
            pathTransitionProb *= transitionProb

        # get emissions probability
        pathEmissionsProb = 1