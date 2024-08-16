def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_prime_pairs(arr, target):
    result = []
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if i != j and arr[i] + arr[j] == target and is_prime(arr[i]) and is_prime(arr[j]):
                result.append([arr[i], arr[j]])
            elif i == j and arr[i] * 2 == target and is_prime(arr[i]):
                result.append([arr[i], arr[j]])
    return result

def main():
    arr = eval(input("Input array of number (example. [2, 3, 5, 7, 11]): "))
    target = int(input("Input Number: "))
    
    result = find_prime_pairs(arr, target)
    
    print(result)

if __name__ == "__main__":
    main()
