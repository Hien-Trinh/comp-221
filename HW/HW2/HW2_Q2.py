def getTopology(A):
    n = len(A)
    isRing = True
    isStar = True
    isFullyConnectedMesh = True
    isCentralNode = False

    for i in range(n):
        totalAdjacent = 0
        for j in range(n):
            if A[i][j]:
                totalAdjacent += 1

        if isFullyConnectedMesh and totalAdjacent != n - 1:
            isFullyConnectedMesh = False
        if isStar:
            if totalAdjacent == n - 1:
                isCentralNode = True
            elif totalAdjacent != 1:
                isStar = False
        if isRing and totalAdjacent != 2:
            isRing = False

    if isRing:
        return "Ring"
    elif isFullyConnectedMesh:
        return "Fully Connected Mesh"
    elif isStar and isCentralNode:
        return "Star"
    else:
        return "None of the above"


def test_topology_detection():
    test_cases = [
        # Test Case 1: Ring Topology
        (
            [[0, 1, 0, 0, 1],
             [1, 0, 1, 0, 0],
             [0, 1, 0, 1, 0],
             [0, 0, 1, 0, 1],
             [1, 0, 0, 1, 0]],
            "Ring"
        ),
        # Test Case 2: Star Topology
        (
            [[0, 1, 1, 1, 1],
             [1, 0, 0, 0, 0],
             [1, 0, 0, 0, 0],
             [1, 0, 0, 0, 0],
             [1, 0, 0, 0, 0]],
            "Star"
        ),
        # Test Case 3: Fully Connected Mesh Topology
        (
            [[0, 1, 1, 1],
             [1, 0, 1, 1],
             [1, 1, 0, 1],
             [1, 1, 1, 0]],
            "Fully Connected Mesh"
        ),
        # Test Case 4: None of the above
        (
            [[0, 1, 0, 1],
             [1, 0, 1, 0],
             [0, 1, 0, 0],
             [1, 0, 0, 0]],
            "None of the above"
        )
    ]

    for i, (matrix, expected) in enumerate(test_cases):
        result = getTopology(matrix)
        print(f"Test Case {i+1}: {'Pass' if result == expected else 'Fail'}")
        print(result)


test_topology_detection()
