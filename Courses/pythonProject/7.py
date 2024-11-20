from collections import Counter


def most_frequent_pair(str):
    pairs = [str[i:i + 2] for i in range(len(str) - 1)]

    pair_counts = Counter(pairs)
    max_count = max(pair_counts.values())

    most_frequent = max(pair for pair, count in pair_counts.items() if count == max_count)

    return most_frequent


str = input()
result = most_frequent_pair(str)
print(result)