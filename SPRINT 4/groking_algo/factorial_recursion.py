def factorilal(x):
    if x == 1:
        return 1
    else:
        return x * factorilal(x-1)
    
print(factorilal(3))
