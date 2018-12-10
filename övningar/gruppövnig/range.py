def range_prod(n_min, n_max):
    if n_min > n_max:
        return 0
        print("noll")
    
    if n_min == n_max:
        return n_min

    elif n_min < n_max:
        return n_max * range_prod(n_min, n_max - 1)
        
        
p = range_prod(5, 10)
print(p)
