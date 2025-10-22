# tasks/task5.py

def solve():
# Ниже пишите решение задачи
    chars = input().split()
    for c in chars:
        print("Код символа", c, "равен", ord(c))
   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()