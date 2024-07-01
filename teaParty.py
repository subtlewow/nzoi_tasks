from collections import Counter

n, k = map(int, input().split())
partygoers_fav = [input().strip().split() for _ in range(n)]
partygoers_stock_temp = [input().strip().split() for _ in range(n)]
hosts = [input().strip() for _ in range(k)]

partygoers_stock = {
    partygoers_stock_temp[i][0]: list(map(int, partygoers_stock_temp[i][1:]))
    for i in range(n)
}

teaDemands = Counter(fav[1] for fav in partygoers_fav)

idx = {"G": 0, "C": 1, "E": 2, "P": 3, "L": 4, "S": 5}

for host in hosts:
    hostStock = partygoers_stock[host]
    partyStatus = sum(max(0, teaDemands[tea] - hostStock[idx[tea]]) for tea in idx)

    if partyStatus == 0:
        print(f"{host} Successful")
    elif partyStatus > 0 and partyStatus <= 2:
        print(f"{host} Mildly Successful ({partyStatus})")
    elif partyStatus > 2:
        print(f"{host} Disaster ({partyStatus})")
