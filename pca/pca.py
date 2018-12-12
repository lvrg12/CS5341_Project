import os
import math
import csv
import string
from sklearn.decomposition import PCA

def main():

    vs = []

    # Vector Space
    with open('../vector_space.csv', 'r', newline='') as csv_td:
        reader = csv.reader(csv_td)
        for row in reader:
            if not row[0].isdigit():
                continue
            else:
                vs.append( [ i for i in row if i.isdigit()] )

    model = PCA(n_components=1600)
    model.fit(vs)
    print(len(model.explained_variance_ratio_))
    print(model.explained_variance_ratio_)


if __name__ == "__main__":
    main()