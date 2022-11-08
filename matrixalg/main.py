import random


def get(arr, size):
    result = []
    for i in range(size - 1):
        j = i + 1
        result.append(arr[i][j])
    return result


def main(size):
    n = int(size)
    arr = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            arr[i][j] = random.randint(10, 99)
    diagonal = get(arr, n)
    result = ''
    for row in arr:
        result += ' '.join(map(str, row)) + '\n'
    result += 'Диагональ массива, параллельная главной диагонали: \n'
    for value in diagonal:
        result += str(value) + ' '
    return result


if __name__ == '__main__':
    main()