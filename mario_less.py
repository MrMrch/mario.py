while True:
    try:
        answer = int(input("Height: "))
        if answer >=1 and answer <= 8:
            for i in range(answer, 0, -1):
                print(f" "*(i-1), end = '')
                print("#"*(answer-(i-1)))
            break
    except:
        continue
