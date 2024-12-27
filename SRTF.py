# SRTF Shortest Remaining Time First
# Process [burst_time, arrival_time, pid]

def srtf(process_list):
    gantt = []
    burst_times = {i[2]: i[0] for i in process_list}  # Сохраняем исходные burst_times
    completion = {}
    t = 0

    while process_list:
        # Поиск доступных процессов
        available = [p for p in process_list if p[1] <= t]
        
        if not available:
            gantt.append("Idle")
            t += 1
            continue
        
        # Сортировка по оставшемуся времени выполнения
        available.sort(key=lambda x: x[0])
        process = available[0]
        
        # Выполнение процесса
        gantt.append(process[2])
        process[0] -= 1  # Уменьшаем оставшееся время
        t += 1
        
        # Проверка завершения процесса
        if process[0] == 0:
            process_list.remove(process)
            process_name = process[2]
            arrival_time = process[1]
            burst_time = burst_times[process_name]
            ct = t  # Время завершения
            tt = ct - arrival_time  # Общее время пребывания
            wt = tt - burst_time  # Время ожидания
            completion[process_name] = [ct, tt, wt]
    
    # Вывод результатов
    print("Диаграмма Ганта:", gantt)
    print("Результаты выполнения процессов:")
    print("PID\tCT\tTT\tWT")
    for pid, metrics in completion.items():
        print(f"{pid}\t{metrics[0]}\t{metrics[1]}\t{metrics[2]}")

    # Средние значения
    total_wt = sum([metrics[2] for metrics in completion.values()])
    total_tt = sum([metrics[1] for metrics in completion.values()])
    print(f"Среднее время ожидания: {total_wt / len(completion):.2f}")
    print(f"Среднее время пребывания: {total_tt / len(completion):.2f}")

if __name__ == "__main__":
    process_list = [[6, 2, "p1"], [2, 5, "p2"], [8, 1, "p3"], [3, 0, "p4"], [4, 4, "p5"]]
    srtf(process_list)
