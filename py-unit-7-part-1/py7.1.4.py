#Represent number in terms of powers.
#Example: n=64
#Output: 2^6, 4^3, 8^2
#If not possible to represent in powers, display as false..



#1

def represent_powers(n):
    results = []
    # Try all possible bases from 2 up to n
    for base in range(2, n+1):
        exp = 1
        value = base
        while value <= n:
            if value == n:
                results.append(f"{base}^{exp}")
                break
            exp += 1
            value = base ** exp
    if results:
        return ", ".join(results)
    else:
        return "false"

# Example
print(represent_powers(64))   # 2^6, 4^3, 8^2
print(represent_powers(20))   # false



