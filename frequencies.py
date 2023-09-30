"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def itemToStr(itemsList):
    for i in range (0, len(itemsList)):
        strItem = str(itemsList[i])
        itemsList[i] = strItem
    return itemsList


def frequencies(items):
    frequencies = {}
    items = itemToStr(items)
    for i in range(0, len(items)):
        if items[i] not in frequencies.keys():
            frequencies[items[i]] = 1
        else:
            frequencies[items[i]] += 1
    return frequencies
