orderd=["a","b","k","d","e","g","h","i","l","m","n","c","o","p","r","s","t","u","w","y"]

N = int(input())
arr = [input().replace("ng", "c") for _ in range(N)]

arr.sort(key=lambda x: [orderd.index(i) for i in x])

for i in arr:
    print(i.replace("c", "ng"))
