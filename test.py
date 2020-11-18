import matplotlib.pyplot as plt
import re

def scatter(x, y):
    plt.scatter(x,y)
    plt.show()


def sets():
    set1 = set(["aap", "koe", "bos"])
    set2 = set(["monkey", "cow", "bos"])
    print(set1)
    print(set2)
    print(set1.union(set2))
    print(set1.difference(set2))
    print(set1.intersection(set2))
    print(set1.symmetric_difference(set2))

def regular():

if __name__=="__main__":
    x = [1,2,3,4,5,6]
    y = [1,2,3,4,5,6]
    scatter(x, y)
    sets()
