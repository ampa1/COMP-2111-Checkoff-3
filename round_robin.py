
from collections import deque

# Round-Robin CPU Scheduling Simulation
# COMP 211 - Checkoff 3

# Process name: CPU burst time in milliseconds
processes = {
    "P1": 5,
    "P2": 3,
    "P3": 7
}

time_quantum = 2

# Keep track of remaining execution time
remaining_time = processes.copy()

# FIFO ready queue
ready_queue = deque(processes.keys())

current_time = 0
completion_time = {}
gantt_chart = []

print("ROUND-ROBIN CPU SCHEDULING")
print(f"Time Quantum: {time_quantum} ms\n")

while ready_queue:
    # Take the first process from the queue
    process = ready_queue.popleft()

    # Run for the quantum or remaining time
    execution_time = min(
        time_quantum,
        remaining_time[process]
    )

    start_time = current_time
    current_time += execution_time

    remaining_time[process] -= execution_time

    # Record the execution for the Gantt chart
    gantt_chart.append(
        (process, start_time, current_time)
    )

    print(
        f"{process}: {start_time} ms -> "
        f"{current_time} ms"
    )

    if remaining_time[process] > 0:
        # Unfinished process goes to back of queue
        ready_queue.append(process)
    else:
        # Process has finished
        completion_time[process] = current_time

print("\nPROCESS RESULTS")
print("Process | Burst | Completion | Waiting")

for process, burst_time in processes.items():
    completion = completion_time[process]

    # All processes arrive at time 0
    turnaround = completion
    waiting = turnaround - burst_time

    print(
        f"{process:7} | "
        f"{burst_time:5} | "
        f"{completion:10} | "
        f"{waiting:7}"
    )

print(f"\nTotal execution time: {current_time} ms")
print("(Context-switch overhead not included)")
