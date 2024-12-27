# Priority CPU Scheduling (Pre-emptive)
# Process = [priority, pid, burst_time, arrival_time]

def priority(process_list):
    t = 0
    gantt = []
    completed = {}
    
    # Сохраняем начальное burst_time
    burst_times = {p[1]: p[2] for p in process_list}
    
    while process_list:
        # Поиск доступных процессов
        available = [p for p in process_list if p[3] <= t]
        
        if not available:
            gantt.append("Idle")
            t += 1
            continue
        
        # Сортировка по приоритету
        available.sort(key=lambda x: x[0])  # Чем меньше priority, тем выше приоритет
        process = available[0]
        
        # Выполнение процесса
        gantt.append(process[1])
        process_list.remove(process)
        process[2] -= 1  # Уменьшаем оставшееся время выполнения
        t += 1
        
        if process[2] == 0:
            # Если процесс завершен, рассчитываем метрики
            pid = process[1]
            arrival_time = process[3]
            burst_time = burst_times[pid]
            ct = t  # Время завершения
            tt = ct - arrival_time  # Общее время пребывания
            wt = tt - burst_time  # Время ожидания
            completed[pid] = [ct, tt, wt]
        else:
            # Если процесс не завершен, возвращаем его в очередь
            process_list.append(process)
    
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
    process_list = [[5, "p1", 6, 2], [2, "p2", 2, 5], [4, "p3", 8, 1], [1, "p4", 3, 0], [3, "p5", 4, 4]]
    priority(process_list)
