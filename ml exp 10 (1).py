import math

data = [1, 2, 3, 8, 9, 10]

mean1 = 2
mean2 = 9
std1 = 1
std2 = 1
w1 = 0.5
w2 = 0.5

def gaussian(x, mean, std):
    return (1 / (math.sqrt(2 * math.pi) * std)) * math.exp(-((x - mean) ** 2) / (2 * std ** 2))

for iteration in range(5):
    r1 = []
    r2 = []

    for x in data:
        p1 = w1 * gaussian(x, mean1, std1)
        p2 = w2 * gaussian(x, mean2, std2)

        total = p1 + p2
        r1.append(p1 / total)
        r2.append(p2 / total)

    sum_r1 = sum(r1)
    sum_r2 = sum(r2)

    mean1 = sum(r1[i] * data[i] for i in range(len(data))) / sum_r1
    mean2 = sum(r2[i] * data[i] for i in range(len(data))) / sum_r2

    std1 = math.sqrt(sum(r1[i] * (data[i] - mean1) ** 2 for i in range(len(data))) / sum_r1)
    std2 = math.sqrt(sum(r2[i] * (data[i] - mean2) ** 2 for i in range(len(data))) / sum_r2)

    w1 = sum_r1 / len(data)
    w2 = sum_r2 / len(data)

    print("Iteration", iteration + 1)
    print("Mean 1:", round(mean1, 2), "Mean 2:", round(mean2, 2))
    print("Weight 1:", round(w1, 2), "Weight 2:", round(w2, 2))
    print("--------------------------------")

print("Final Cluster Means:")
print("Cluster 1 Mean:", round(mean1, 2))
print("Cluster 2 Mean:", round(mean2, 2))
