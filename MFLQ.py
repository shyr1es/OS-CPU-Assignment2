def mlfq(process_list, time_quanta_list):
    t = 0
    gantt = []
    completed = {}
    burst_times = {p[2]: p[1] for p in process_list}
    queues = [[] for _ in time_quanta_list]
    process_list.sort()  # Сортируем по времени прибытия
    while process_list or any(queues):
        # Добавляем процессы в очередь на основе их времени прибытия
        while process_list and process_list[0][0] <= t:
            queues[0].append(process_list.pop(0))

        idle = True
        # Проходим по очередям с разными квантами времени
        for i, tq in enumerate(time_quanta_list):
            queue = queues[i]
            if queue:
                idle = False
                process = queue.pop(0)
                pid = process[2]
                arrival_time = process[0]
                remaining_time = process[1]

                if remaining_time <= tq:
                    gantt.extend([pid] * remaining_time)
                    t += remaining_time
                    ct = t
                    tt = ct - arrival_time
                    wt = tt - burst_times[pid]
                    completed[pid] = [ct, tt, wt]
                else:
                    gantt.extend([pid] * tq)
                    t += tq
                    process[1] -= tq
                    # Перемещаем процесс в очередь с более высоким приоритетом (если есть)
                    if i + 1 < len(queues):
                        queues[i + 1].append(process)
                    else:
                        queue.append(process)  # Если на последнем уровне, оставляем в той же очереди
                break

        # Если не было запущено ни одного процесса, добавляем Idle
        if idle:
            gantt.append("Idle")
            t += 1

        # Добавляем новые процессы в очередь, если они пришли
        while process_list and process_list[0][0] <= t:
            queues[0].append(process_list.pop(0))

    print("Gantt Chart:", gantt)
    print("Process Completion Info:")
    for pid, info in completed.items():
        ct, tt, wt = info
        print(f"Process {pid}: Completion Time = {ct}, Turnaround Time = {tt}, Waiting Time = {wt}")

if __name__ == "__main__":
    process_list = [[0, 8, "p1"], [1, 4, "p2"], [2, 9, "p3"], [3, 5, "p4"]]
    time_quanta_list = [4, 8, 16]
    mlfq(process_list, time_quanta_list)
