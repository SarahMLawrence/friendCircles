#friendships = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
def bsf(friendships, friends, i):
    queue = [i]
    friends[i] = True
    while queue:
        N = queue.pop(0)
        for M in range(len(friendships)):
            if friendships[N][M] != 1 or N == M or friends[M]:
                continue
            queue.append(M)
            friends[M] = True
        
def csFriendCircles(friendships):
    res = 0
    friends = [False for M in range(len(friendships))]
    for i in range(len(friendships)):
        if friends[i]:
            continue
        else:
            bsf(friendships, friends, i)
            res += 1
    return res