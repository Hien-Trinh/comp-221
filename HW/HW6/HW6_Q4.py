from collections import deque


def buildGraph(filename):
    validWords = {}
    f = open(filename, "r")
    for word in f:
        validWords[word.strip('\n')] = []

    f.close()

    for key, value in validWords.items():
        for letter_idx in range(len(key)):
            for letter in "abcdefghijklmnopqrstuvwxyz":
                neighbor = key[:letter_idx] + letter + key[letter_idx + 1:]
                if neighbor in validWords:
                    validWords[neighbor].append(key)
                    value.append(neighbor)

    return validWords


def getPath(validWords, source, destination):
    if source not in validWords or destination not in validWords:
        return

    path = [source]
    queue = deque()
    queue.append((source, path))

    while queue:
        for _ in range(len(queue)):
            word, path = queue.popleft()
            if word == destination:
                return " -> ".join(path)
            for neighbor in validWords[word]:
                queue.append((neighbor, path + [neighbor]))


validWords = buildGraph("threeletterwords.txt")
# print(validWords)
print(getPath(validWords, "dog", "cat"))
