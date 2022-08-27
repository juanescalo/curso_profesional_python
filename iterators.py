import time

class FiboIter():
    max = int

    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if not self.max or self.n2 <= self.max:
            if self.counter == 0:
                self.counter += 1
                return self.n1
            elif self.counter == 1:
                self.counter += 1
                return self.n2
            else:
                self.aux = self.n1 + self.n2
                # self.n1 = self.n2
                # self.n2 = self.aux
                self.n1, self.n2 = self.n2, self.aux
                self.counter += 1
                return self.aux
        else:
            raise StopIteration


def run():
    max_value = int(input("Ingresa el valor máximo a visualizar: "))
    fibonachi = FiboIter(max_value)
    for element in fibonachi:
        print(element)
        time.sleep(1)


if __name__ == "__main__":
    run()
