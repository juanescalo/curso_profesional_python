import time

def fibo_gen(max:int) -> int:
    n1 = 0
    n2 = 1
    counter = 0
    while True:
        if n2 <= max:
            if counter == 0:
                counter += 1
                yield n1
            elif counter == 1:
                counter += 1
                yield n2
            else:
                aux = n1 + n2
                n1, n2 = n2, aux
                counter += 1
                yield aux
        else:
            break


if __name__ == "__main__":
    max_value = int(input("Ingrese el valor máximo a visualizar: "))
    fibonacci = fibo_gen(max_value)
    for element in fibonacci:
        print(element)
        time.sleep(1)