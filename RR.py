# Round Robin CPU Scheduling Algorithm
# Process: [arrival_time, burst_time, pid]

def round_robin(process_list, time_quanta):
    t = 0
    gantt = []
    completed = {}
    
    # Сортировка процессов по arrival_time
    process_list.sort()
    burst_times = {p[2]: p[1] for p in process_list}  # Сохраняем исходное burst_time
    
    # Циклическая очередь процессов
    queue = process_list.copy()
    
    while queue:
        # Проверка доступных процессов
        available = [p for p in queue if p[0] <= t]
        
        if not available:
            gantt.append("Idle")
            t += 1
            continue
        
        # Выполнение процесса
        process = available.pop(0)
        queue.remove(process)
        gantt.append(process[2])
        
        rem_burst = process[1]
        if rem_burst <= time_quanta:
            # Процесс завершен
            t += rem_burst
            ct = t
            pid = process[2]
            arrival_time = process[0]
            burst_time = burst_times[pid]
            tt = ct - arrival_time
            wt = tt - burst_time
            completed[pid] = [ct, tt, wt]
        else:
            # Процесс частично выполняется
            t += time_quanta
            process[1] -= time_quanta
            queue.append(process)  # Добавляем процесс обратно в очередь
    
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
    time_quanta = 2
    round_robin(process_list, time_quanta)
    