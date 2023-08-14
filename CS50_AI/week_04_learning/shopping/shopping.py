import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4
filename = "shopping.csv"

def main1():
    #sys.setrecursionlimit(5000)
    load_data(filename)
    #print(sys.getrecursionlimit())

def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        *0 - Administrative, an integer
        *1 - Administrative_Duration, a floating point number
        *2 - Informational, an integer
        *3 - Informational_Duration, a floating point number
        *4 - ProductRelated, an integer
        *5 - ProductRelated_Duration, a floating point number
        *6 - BounceRates, a floating point number
        *7 - ExitRates, a floating point number
        *8 - PageValues, a floating point number
        *9 - SpecialDay, a floating point number
        * 10 - Month, an index from 0 (January) to 11 (December)
        *11- OperatingSystems, an integer
        *12- Browser, an integer
        *13- Region, an integer
        *14- TrafficType, an integer
        * 15- VisitorType, an integer 0 (not returning) or 1 (returning)
        * 16- Weekend, an integer 0 (if false) or 1 (if true)
        * 17 - Revenue

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """

    #starts evidence and label lists to return
    evidence, labels = list(), list()
    #starts dataset
    my_dataset = list()
    lines_to_remove = set() #set of lines to remove during data cleaning

    # read file
    with open(filename) as file:
        dataset = csv.reader(file, delimiter=",")

        next(dataset) # skips the first row as column names

        # populates evidence and labels
        for row in dataset:
                my_dataset.append(row)


    # processing the data
    index_int = (0, 2, 4, 11, 12, 13, 14) #helper for indexes that should be int
    index_float = (1, 3, 5, 6, 7, 8, 9) #helper for indexes that should be float
    dic_month =  {"Jan":0, "Feb":1, "Mar":2, "Apr":3, "May":4, "Jun":5,
                    "Jul":6, "Aug":7, "Sep": 8, "Oct":9, "Nov":10, "Dec":11}


    for index, row in enumerate(my_dataset):

        #print("Processing row:", index)

        # try to convert values that should be int to int,
        # if fails, add to list of index to remove
        for i in index_int:
            try:
                row[i] = int(row[i])
            except ValueError:
                lines_to_remove.add(index)
                break #once a line is marked to be removed, not need to continue checking it

        # same for float values
        for i in index_float:
            try:
               row[i] = float(row[i])
            except ValueError:
                lines_to_remove.add(index)
                break #once a line is marked to be removed, not need to continue checking it

        # treats month, column 10
        try:
            row[10] = dic_month[row[10]]
        except KeyError:
            lines_to_remove.add(index)
            break


        # treats visitor_type, column 15
        if  row[15] == "Returning_Visitor":
            row[15] = 1
        elif row[15] == "New_Visitor":
            row[15] = 0
        else: #if doesn't comply with values, mark to remove from list
            lines_to_remove.add(index)

        # treats weekend, column 16
        if row[16] == "TRUE":
            row[16] = 1
        elif row[16] == "FALSE":
            row[16] = 0
        else: #if doesn't comply with values, mark to remove from list
            lines_to_remove.add(index)

        # treats revenue, column 17
        if row[17] == "TRUE":
            row[17] = 1
        elif row[17] == "FALSE":
            row[17] = 0
        else: #if doesn't comply with values, mark to remove from list
            lines_to_remove.add(index)

    #print(len(my_dataset[0]))

    # clean main data_set
    # Use list comprehension to filter out rows that are not in the set of rows to remove
    my_dataset_filtered = [row for idx, row in enumerate(my_dataset) if idx not in lines_to_remove]

    # remove duplicates from my_dataset_filtered
    # since the order of the elements matter, use list comprehension to remove duplicates
    cleaned_dataset = []
    [cleaned_dataset.append(row) for row in my_dataset_filtered if row not in cleaned_dataset ]

    #print(f"lenghts {len(my_dataset)}, {len(lines_to_remove)}, {len(cleaned_dataset)}")

    evidence = [row[:-1] for row in cleaned_dataset]  # take all columns except the last column as evidence
    label = [row[-1] for row in cleaned_dataset]

    #print(len(cleaned_dataset))
    #print(len(evidence))
    #print(len(label))


    #print(my_dataset_filtered[5457])
   # print(evidence)

    # only returning first 5000 rows as computer crashes if more
    # unfortunately I was unable to find help to solve this :(
    return evidence[:5000], label[:5000]

def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    # creates a k-nearest neighbor classifier with k=1
    classifier = KNeighborsClassifier(n_neighbors=1)

    print(f"size evidence {len(evidence)}, label: {len(labels)} ")
    # fits the classifier on the training data - evidence and labels
    return classifier.fit(evidence, labels)


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    # Code from the lecture to compute how well we performed
    total_positive, correct_positive = 0, 0
    total_negative, correct_negative = 0, 0

    for actual, predicted in zip(labels, predictions):

        if actual == 1:
            total_positive += 1
            if actual == predicted:
                correct_positive += 1
        elif actual ==0:
            total_negative += 1
            if actual == predicted:
                correct_negative += 1

    sensitivity = correct_positive / total_positive
    specificity = correct_negative / total_negative

    return (sensitivity, specificity)


if __name__ == "__main__":
    main()
