 #!/usr/bin/python3
class A(object):
    field = 5


if __name__ == "__main__":
    a1 = A()
    a2 = A()
    print(a1.field)

    a1.field = 10
    print(a1.field)

    print(a2.field)

    A.field = 7
    print(a1.field)
    print(a2.field) 

  