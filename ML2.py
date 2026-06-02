import csv

def candidate_elimination(data):
    n = len(data[0]) - 1
    S = ['0'] * n
    G = [['?'] * n]

    for row in data:
        x, label = row[:-1], row[-1]

        if label == "Yes":  # Positive
            G = [g for g in G if all(g[i] == '?' or g[i] == x[i] for i in range(n))]
            for i in range(n):
                if S[i] == '0':
                    S[i] = x[i]
                elif S[i] != x[i]:
                    S[i] = '?'

        else:  # Negative
            new_G = []
            for g in G:
                if all(g[i] == '?' or g[i] == x[i] for i in range(n)):
                    for i in range(n):
                        if g[i] == '?':
                            h = g.copy()
                            h[i] = S[i]
                            new_G.append(h)
                else:
                    new_G.append(g)
            G = new_G

    return S, G


# Read CSV
with open("data.csv") as f:
    data = list(csv.reader(f))[1:]  # skip header

S, G = candidate_elimination(data)

print("S:", S)
print("G:", G)
