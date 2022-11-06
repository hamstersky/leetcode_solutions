def getFurthest(dists, values):
    dist = max(dists)
    index = dists.index(dist)
    furthest = {"distance": dist, "value": values[index], "index": index}
    return furthest


def findClosestElements(arr, k, x):
    dists = list(map(lambda a: abs(a - x), arr[:k]))
    values = arr[:k]
    furthest = getFurthest(dists, values)

    for a in arr[k:]:
        dist = abs(a - x)
        if dist < furthest["distance"]:
            dists[furthest["index"]] = dist
            values[furthest["index"]] = a
            furthest = getFurthest(dists, values)
    return sorted(values)


print(findClosestElements([0, 1, 1, 1, 2, 3, 6, 7, 8, 9], 9, 4))

arr = [1, 2, 3, 4, 5]
k = 4
x = 3
# print(findClosestElements(arr, k, x))

dists = {a: a - x for a in arr[:k]}
# print(dists)
