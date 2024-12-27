# SJF shortest job first
# Process : [burst_time, arrival_time, pid]

def sjf(process_list):
    t = 0
    gantt = []
    completed = {}
    while process_list:
        # Поиск доступных процессов
        available = [p for p in process_list if p[1] <= t]
        
        if not available:
            t += 1
            gantt.append("Idle")
            continue
        
        # Сортировка доступных процессов по времени выполнения
        available.sort()
        process = available[0]
        
        # Получение данных процесса
        burst_time = process[0]
        arrival_time = process[1]
        pid = process[2]
        
        # Обработка процесса
        t += burst_time
        gantt.append(pid)
        ct = t  # Время завершения
        tt = ct - arrival_time  # Время пребывания
        wt = tt - burst_time  # Время ожидания
        
        # Удаление процесса из очереди
        process_list.remove(process)
        completed[pid] = [ct, tt, wt]

    # Вывод результатов
    print("Диаграмма Ганта:", gantt)
    print("Результаты выполнения процессов:")
    print("PID\tCT\tTT\tWT")
    for pid, metrics in completed.items():
        print(f"{pid}\t{metrics[0]}\t{metrics[1]}\t{metrics[2]}")

    # Средние метрики
    total_wt = sum([metrics[2] for metrics in completed.values()])
    total_tt = sum([metrics[1] for metrics in completed.values()])
    print(f"Среднее время ожидания: {total_wt / len(completed):.2f}")
    print(f"Среднее время пребывания: {total_tt / len(completed):.2f}")

if __name__ == "__main__":
    process_list = [[6, 2, "p1"], [2, 5, "p2"], [8, 1, "p3"], [3, 0, "p4"], [4, 4, "p5"]]
    sjf(process_list)
