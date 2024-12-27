# Priority CPU Scheduling (Non Pre-emptive)
# Process : [Priority, pid, burst_time, arrival_time]

def priority(process_list):
    gantt = []
    t = 0
    completed = {}
    
    while process_list:
        # Поиск доступных процессов
        available = [p for p in process_list if p[3] <= t]
        
        if not available:
            gantt.append("Idle")
            t += 1
            continue
        
        # Сортировка доступных процессов по приоритету
        available.sort(key=lambda x: x[0])  # Меньшее значение priority означает более высокий приоритет
        process = available[0]
        
        # Удаление процесса из очереди
        process_list.remove(process)
        pid = process[1]
        gantt.append(pid)
        
        # Выполнение процесса
        burst_time = process[2]
        t += burst_time
        ct = t  # Время завершения
        arrival_time = process[3]
        tt = ct - arrival_time  # Время пребывания
        wt = tt - burst_time  # Время ожидания
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
    process_list = [[5, "p1", 6, 2], [4, "p2", 2, 5], [1, "p3", 8, 1], [2, "p4", 3, 0], [3, "p5", 4, 4]]
    priority(process_list)
