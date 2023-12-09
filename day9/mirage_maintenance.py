from functools import lru_cache

@lru_cache(maxsize=None)
def extrapolate(sequence, count = 0):
    if all(x == 0 for x in sequence):
        return count
    count += sequence[-1]
    return extrapolate(tuple(sequence[i + 1] - sequence[i] for i in range(len(sequence) - 1)), count)

if __name__ == "__main__":

    with open("data/input_9.txt", "r") as file:
        items = file.read().rstrip().split('\n')

    sequences = [[int(n) for n in item.split()] for item in items]

    #part 1
    print(sum([extrapolate(tuple(sequence)) for sequence in sequences]))

    #part 2
    print(sum([extrapolate(tuple(sequence[::-1])) for sequence in sequences]))

