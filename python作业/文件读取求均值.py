with open("sensor-data-1k.txt","r") as f:
    sum, cnt = 0, 0
    for line in f:
        ls = line.split()
        cnt += 1
        sum += eval(ls[4])
    print(f"{sum / cnt:.2f}")