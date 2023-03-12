class Jar:
    def __init__(self, capacity=12):
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if self._size + n > self._capacity:
            raise ValueError("cookies more than capacity")
        self._size += n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError("no more cookies you can withdraw it")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

def main():
    jar = Jar(12)
    jar.deposit(1)
    print(jar)


if __name__ == "__main__":
    main()
