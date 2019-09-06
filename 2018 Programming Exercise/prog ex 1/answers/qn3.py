# calculates the distance given 3 numbers u, a, t.
def dist(u, a, t):
    return (u * t) + (a * (t ** 2) / 2)

def main():
    u = input("Enter the initial velocity here: ")
    a = input("    Enter the acceleration here: ")
    t = print("   Enter the time interval here: ")

    u = int(u)
    a = int(a)
    t = int(t)
    for i in range(5):
        
