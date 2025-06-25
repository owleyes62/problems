numUnique = int(input('Digite um numero: '))
num = input('Digite numeros: ')

numStrings = num.split()
numbers = [int(numbers) for numbers in numStrings]


def twoSum(nums: list[int], target: int) -> list[int]:
    prevMap = {}

    for i, n in enumerate(nums):
        print(prevMap)
        print(i, n)
        diff = target - n

        if diff in prevMap:

            print(f'parabens {diff} + {n} é igual a {numUnique}')
        prevMap[n] = i
    else:
        print(f'numeros da lista não batem com {numUnique}')


twoSum(numbers, numUnique)
