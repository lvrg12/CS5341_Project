import os
import math
import csv

def main():

    vocabulary = []
    tf_vector = []
    vector_space = []
    doc_classes = {}
    doc = 0
    with open('vector_space.csv', newline='') as csv_td:
        reader = csv.reader(csv_td)
        for row in reader:
            if row[0].isdigit():
                vector = [ int(c) for c in row if c.isdigit() ]
                doc_classes[doc] = row[-1]
                doc+=1
                tf_vector.append(vector)
            else:
                vocabulary = [ w for w in row ]

    classes = ["real democrat","real republican","fake democrat","fake republican"]


    rd = {}

    rr = {}

    fd = {}

    fr = {}

    for c in classes:
        for d in 


if __name__ == "__main__":
    main()