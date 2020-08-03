# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        a = "".join([s[c] for c in range(len(s)) if c%2==0])
        b = "".join([s[c] for c in range(len(s)) if c%2==1])
        print(f'{a} {b}')
