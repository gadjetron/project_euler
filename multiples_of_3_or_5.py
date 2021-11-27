UPBOUND = 1000

print(
    sum(
        (
            i for i in range(1, UPBOUND) 
            if (i % 3 == 0) or (i % 5 == 0)
        )
    )
)
