class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    # Getter - Return Capacity
    @property
    def capacity(self):
        return self._capacity


    # define setter for capacity
    @capacity.setter
    def capacity(self, capacity):
        # test if capacity is a positive integer
        if int(capacity) < 0:
            raise ValueError("Capacity must be a non-negative integer.")

        # sets the capacity, if not specified, it will default of 12
        self._capacity = capacity


    # Getter - Return Size (getter needs to come before setter)
    @property
    def size(self):
        return self._size

    # define setter for size
    @size.setter
    def size(self, size):
        self._size = size


    def __str__(self):
        # prints the number of cookies
        return "🍪" * self.size


    def deposit(self, n):
        # check if possible to deposit the cookies based on capacity
        if int(n) > self._capacity - self._size:
            raise ValueError("Too many cookies, get a bigger jar!")

        if int(n) < 0:
            raise ValueError("Hey silly, negative cookies don't exist!")

        # if passed check above, deposit cookies
        self._size += int(n)

    def withdraw(self, n):
        if int(n) > self._size:
            raise ValueError("Not enough cookies in the jar!")
        self._size -= int(n)


def main():
    # creates a new jar
    jar = Jar()
    # deposits 10 cookies
    jar.deposit(10)

    print(jar.size)
    print(str(jar))



if __name__ == "__main__":
    main()

