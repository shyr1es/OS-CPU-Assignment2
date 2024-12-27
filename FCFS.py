# FCFS first come first serve
# Process : [arrival_time, burst_time, pid]

def fcfs(process_list):
    t = 0
    gantt = []
    completed = {}
    process_list.sort()  # Сортировка по времени прибытия
    while process_list:
        if process_list[0][0] > t:
            t += 1
            gantt.append("Idle")
            continue
        else:
            process = process_list.pop(0)
            gantt.append(process[2])
            t += process[1]
            pid = process[2]
            ct = t  # Время завершения
            tt = ct - process[0]  # Время пребывания
            wt = tt - process[1]  # Время ожидания
            completed[pid] = [ct, tt, wt]

    # Вывод результатов
    print("Диаграмма Ганта:", gantt)
    print("Результаты выполнения процессов:")
    print("PID\tCT\tTT\tWT")
    for pid, metrics in completed.items():
        print(f"{pid}\t{metrics[0]}\t{metrics[1]}\t{metrics[2]}")

    # Среднее время ожидания
    total_wt = sum([metrics[2] for metrics in completed.values()])
    print(f"Среднее время ожидания: {total_wt / len(completed):.2f}")

if __name__ == "__main__":
    process_list = [[2, 6, "p1"], [5, 2, "p2"], [1, 8, "p3"], [0, 3, "p4"], [4, 4, "p5"]]
    fcfs(process_list)
