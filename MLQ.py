# MLQ (Multi-Level Queue Scheduling)
# Process: [arrival_time, burst_time, pid, queue]

def mlq(queues):
    t = 0
    gantt = []
    completed = {}
    
    # Сортировка процессов внутри каждой очереди по времени прибытия
    for queue in queues:
        queue.sort(key=lambda x: x[0])
    
    while any(queues):
        idle = True
        for queue in queues:
            # Поиск доступных процессов
            ready = [p for p in queue if p[0] <= t]
            if ready:
                idle = False
                # Выбор первого доступного процесса
                process = ready.pop(0)
                queue.remove(process)
                
                # Выполнение процесса
                pid = process[2]
                arrival_time = process[0]
                burst_time = process[1]
                t += burst_time
                gantt.append(pid)
                
                # Расчет метрик
                ct = t  # Время завершения
                tt = ct - arrival_time  # Время пребывания
                wt = tt - burst_time  # Время ожидания
                completed[pid] = [ct, tt, wt]
                break
        
        if idle:
            gantt.append("Idle")
            t += 1
    
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
    queues = [
        [[0, 4, "p1", 1], [2, 3, "p2", 1]],
        [[1, 5, "p3", 2], [3, 6, "p4", 2]],
        [[2, 8, "p5", 3], [4, 2, "p6", 3]]
    ]
    mlq(queues)
