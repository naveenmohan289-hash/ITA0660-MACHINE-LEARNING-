
data = [
    ['Sunny', 'Hot', 'No'],
    ['Sunny', 'Hot', 'No'],
    ['Overcast', 'Hot', 'Yes'],
    ['Rain', 'Mild', 'Yes'],
    ['Rain', 'Cool', 'Yes'],
    ['Rain', 'Cool', 'No'],
    ['Overcast', 'Cool', 'Yes'],
    ['Sunny', 'Mild', 'No']
]

test = [
    ['Sunny', 'Hot', 'No'],
    ['Overcast', 'Hot', 'Yes'],
    ['Rain', 'Cool', 'Yes'],
    ['Sunny', 'Mild', 'No']
]

classes = ['Yes', 'No']

def predict(sample):
    probs = {}

    for c in classes:
        class_rows = [row for row in data if row[-1] == c]
        prob = len(class_rows) / len(data)

        for i in range(len(sample) - 1):
            count = 0
            for row in class_rows:
                if row[i] == sample[i]:
                    count += 1
            prob *= count / len(class_rows)

        probs[c] = prob

    if probs['Yes'] > probs['No']:
        return 'Yes'
    else:
        return 'No'

TP = TN = FP = FN = 0
correct = 0

print("Actual\tPredicted")

for row in test:
    actual = row[-1]
    predicted = predict(row)

    print(actual, "\t", predicted)

    if actual == predicted:
        correct += 1

    if actual == 'Yes' and predicted == 'Yes':
        TP += 1
    elif actual == 'No' and predicted == 'No':
        TN += 1
    elif actual == 'No' and predicted == 'Yes':
        FP += 1
    elif actual == 'Yes' and predicted == 'No':
        FN += 1

accuracy = correct / len(test) * 100

print("\nConfusion Matrix")
print("----------------")
print("TP =", TP, " FP =", FP)
print("FN =", FN, " TN =", TN)

print("\nAccuracy =", accuracy, "%")
