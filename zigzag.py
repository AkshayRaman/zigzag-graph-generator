import random
import matplotlib.pyplot as plt

random.seed(7)

def make_zigzag(A, shift, reverse=False):
    ''' '''
    n = len(A)

    if isinstance(shift, float):
        assert shift <= 1.0
        shift = int(shift*n)
    elif isinstance(shift, int):
        assert shift <= n

    zig_zag = sorted(A, reverse=reverse)

    for i in range(0, n-shift, 2):
        r = random.randint(i+1, i+shift)
        zig_zag[i], zig_zag[r] = zig_zag[r], zig_zag[i]

    return zig_zag

if __name__ == "__main__":
    N = 100
    original_list = [random.randint(0, 100)/100.0 for i in range(N)]
    sorted_list = sorted(original_list)
    reverse_sorted_list = sorted_list[::-1]

    plt.plot(original_list, label='original data')
    plt.plot(sorted_list, label='sorted')
    plt.plot(reverse_sorted_list, label='reverse sorted')
    plt.legend()

    n = 50
    zz1 = make_zigzag(original_list, n)
    plt.plot(zz1, label='random zigzag (%s)' %n)
    plt.legend()

    n = 0.3
    zz2 = make_zigzag(original_list, n, reverse=True)
    plt.plot(zz2, label='random zigzag reversed (%s)' %n)
    plt.legend()

    plt.show()
