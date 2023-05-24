def sumNumbers(sp, ep):
    s = int(sp)
    e = int(ep)
    retural = 0
    for s in range(e+1):
        retural = retural + s
    return retural

print(sumNumbers(1,100))