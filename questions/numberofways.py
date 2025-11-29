def numberOfWays(queries):
    res = []

    for r,c in queries:
        limit = min(r,c)
        total = 0
        for a in range(1,limit+1):
            total += (r-a+1)*(c-a+1)
        res.append(total)

    return res
    






if __name__ == "__main__":
    q = int(input())  
    queries = []

    for _ in range(q):
        r, c = map(int, input().split())
        queries.append((r, c))

    answers = numberOfWays(queries)

    for ans in answers:
        print(ans)
