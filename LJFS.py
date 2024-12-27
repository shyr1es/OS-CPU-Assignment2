# LJFS (Longest Job First Scheduling)
# Process : [arrival_time, burst_time, pid]

def ljfs(process_list):
    t = 0
    gantt = []
    completed = {}
    # Сортировка по времени прибытия, затем по убыванию burst_time
    process_list.sort(key=lambda x: (x[0], -x[1]))
    
    while process_list:
        # Выбор доступных процессов
        ready = [p for p in process_list if p[0] <= t]
        if not ready:
            gantt.append("Idle")
            t += 1
            continue
        
        # Выбор процесса с максимальным burst_time
        process = max(ready, key=lambda x: x[1])
        process_list.remove(process)
        
        # Обработка процесса
        gantt.append(process[2])
        t += process[1]
        pid = process[2]
        ct = t  # Время завершения
        tt = ct - process[0]  # Общее время пребывания
        wt = tt - process[1]  # Время ожидания
        
        # Запись результатов
        completed[pid] = [ct, tt, wt]

    # Вывод результатов
    print("Диаграмма Ганта:", gantt)
    print("Результаты выполнения процессов:")
    print("PID\tCT\tTT\tWT")
    for pid, metrics in completed.items():
        print(f"{pid}\t{metrics[0]}\t{metrics[1]}\t{metrics[2]}")

    # Средние значения
    total_wt = sum([metrics[2] for metrics in completed.values()])
    total_tt = sum([metrics[1] for metrics in completed.values()])
    print(f"Среднее время ожидания: {total_wt / len(completed):.2f}")
    print(f"Среднее время пребывания: {total_tt / len(completed):.2f}")

if __name__ == "__main__":
    process_list = [[2, 6, "p1"], [5, 2, "p2"], [1, 8, "p3"], [0, 3, "p4"], [4, 4, "p5"]]
    ljfs(process_list)
