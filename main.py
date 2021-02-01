def nthLetter (w, n):
    if len(w) >= n:
        return w[(n - 1)]
    else:
        return False
print (nthLetter("cat", 2))
