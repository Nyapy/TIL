import sys

sys.stdin = open("전기버스_input.txt")
sys.stdout = open("전기버스_output.txt", "w")
T = int(input())
for tc in range(T):
    move, stop, charger = map(int, input().split())
    bus_stop = [0] * (stop+1)
    charge_count = 0
    stop_list = list(map(int, input().split()))
    for i in range(1, stop):
        if i in stop_list:
            bus_stop[i] += 1
    for j in range(len(bus_stop)):
        if j == 0:
            charge = move
            charge -= 1
        else:
            if len(bus_stop) - j > move :
                li = []
                for k in range(1, charge + 1):
                    if bus_stop[j + k] == 1:
                        li += [1]
                    else:
                        li += [0]
                if bus_stop[j] == 0:
                    charge -= 1
                elif bus_stop[j] == 1 and 1 in li :
                    charge -= 1
                elif bus_stop[j] == 1 and 1 not in li :
                    charge = move -1
                    charge_count += 1
            else:
                if bus_stop[j] == 1 and charge < len(bus_stop)-j:
                    charge = move -1
                    charge_count += 1
            if charge < 0:
                charge_count = 0
                break
    print("#{} {}" .format(tc+1, charge_count))
