import pandas as pd
import numpy as np

# -------------------------------
# 1. DEFINE DATASET (IMPORTANT!)
# -------------------------------
data = [
    ['Sunny','Hot','High','Weak','No'],
    ['Sunny','Hot','High','Strong','No'],
    ['Overcast','Hot','High','Weak','Yes'],
    ['Rain','Mild','High','Weak','Yes'],
    ['Rain','Cool','Normal','Weak','Yes'],
    ['Rain','Cool','Normal','Strong','No'],
    ['Overcast','Cool','Normal','Strong','Yes'],
    ['Sunny','Mild','High','Weak','No'],
    ['Sunny','Cool','Normal','Weak','Yes'],
    ['Rain','Mild','Normal','Weak','Yes'],
    ['Sunny','Mild','Normal','Strong','Yes'],
    ['Overcast','Mild','High','Strong','Yes'],
    ['Overcast','Hot','Normal','Weak','Yes'],
    ['Rain','Mild','High','Strong','No']
]

columns = ['Outlook','Temperature','Humidity','Wind','PlayTennis']

# -------------------------------
# 2. CREATE DATAFRAME
# -------------------------------
df = pd.DataFrame(data, columns=columns)

# -------------------------------
# 3. ENTROPY FUNCTION
# -------------------------------
def entropy(target_col):
    values, counts = np.unique(target_col, return_counts=True)
    ent = 0
    for i in range(len(values)):
        p = counts[i] / sum(counts)
        ent += -p * np.log2(p)
    return ent

# -------------------------------
# 4. INFORMATION GAIN
# -------------------------------
def info_gain(df, attr, target="PlayTennis"):
    total_entropy = entropy(df[target])
    values, counts = np.unique(df[attr], return_counts=True)

    weighted_entropy = 0
    for i in range(len(values)):
        subset = df[df[attr] == values[i]]
        weighted_entropy += (counts[i] / sum(counts)) * entropy(subset[target])

    return total_entropy - weighted_entropy

# -------------------------------
# 5. ID3 ALGORITHM
# -------------------------------
def id3(df, attributes, target="PlayTennis"):

    if len(np.unique(df[target])) == 1:
        return df[target].iloc[0]

    if len(attributes) == 0:
        return df[target].mode()[0]

    gains = [info_gain(df, attr, target) for attr in attributes]
    best_attr = attributes[np.argmax(gains)]

    tree = {best_attr: {}}

    for value in np.unique(df[best_attr]):
        subset = df[df[best_attr] == value]
        subtree = id3(subset, [a for a in attributes if a != best_attr], target)
        tree[best_attr][value] = subtree

    return tree

# -------------------------------
# 6. BUILD TREE
# -------------------------------
attributes = columns[:-1]
tree = id3(df, attributes)

print("Decision Tree:\n", tree)

# -------------------------------
# 7. PREDICTION FUNCTION
# -------------------------------
def predict(sample, tree):
    for root in tree:
        value = sample[root]
        subtree = tree[root][value]

        if isinstance(subtree, dict):
            return predict(sample, subtree)
        else:
            return subtree

# -------------------------------
# 8. TEST SAMPLE
# -------------------------------
sample = {
    'Outlook': 'Sunny',
    'Temperature': 'Hot',
    'Humidity': 'High',
    'Wind': 'Weak'
}

result = predict(sample, tree)

print("\nNew Sample:", sample)
print("Prediction:", result)
