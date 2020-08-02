

def draw_square(size):
    rows = 0
    while rows < size:
        print("* " * size)
        rows += 1
        
def inputInt(message):
    num = input(message)
    return int(num)


draw_square(inputInt("Size 1st square: "))
draw_square(inputInt("Size 2nd square: "))