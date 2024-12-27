# LRTF (Longest Remaining Time First)
# Process : [arrival_time, burst_time, pid]

def lrtf(process_list):
    t = 0
    gantt = []
    completed = {}
    
    # Добавляем remaining_time в список процессов
    process_list = [[p[0], p[1], p[1], p[2]] for p in process_list]
    
    while process_list:
        # Определение доступных процессов
        ready = [p for p in process_list if p[0] <= t]
        
        if not ready:
            gantt.append("Idle")
            t += 1
            continue
        
        # Выбор процесса с наибольшим remaining_time
        process = max(ready, key=lambda x: x[2])
        gantt.append(process[3])
        
        # Обработка процесса
        process[2] -= 1  # Уменьшаем оставшееся время
        t += 1
        
        if process[2] == 0:
            # Если процесс завершен, вычисляем метрики
            ct = t
            tt = ct - process[0]
            wt = tt - process[1]
            completed[process[3]] = [ct, tt, wt]
            process_list.remove(process)
    
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
    lrtf(process_list)
