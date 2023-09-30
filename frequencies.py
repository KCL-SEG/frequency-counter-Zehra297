"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def itemToStr(itemsList):
    for i in range (0, len(itemsList)):
        strItem = str(itemsList[i])
        itemsList[i] = strItem
    return itemsList

def itemCounter(item, itemList):
    count = 0
    for i in range (0, len(itemList)):
        if item == itemList[i]:
            count += 1
    return count


def frequencies(items):
    frequencies = {}
    items = itemToStr(items)
    for i in range(0, len(items)):
        key = items[i]
        val = itemCounter(items[i], items)
        frequencies[key] = val
    return frequencies
