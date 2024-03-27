import matplotlib.pyplot as plt

def collatz(n):
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1
    return count

def main():
    start = 1
    end = 10000
    x = []
    y = []
    for i in range(start, end + 1):
        x.append(i)
        y.append(collatz(i))
    plt.plot(y, x, 'ro')
    plt.xlabel('Número de iteraciones')
    plt.ylabel('Número de inicio de la secuencia')
    plt.title('Conjetura de Collatz')
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()
