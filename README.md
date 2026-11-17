# COMP 2111 Checkoff 3 – Round-Robin CPU Scheduling
## Project Overview
For my Operating Systems Scheduling exploration project, I chose to research Round-Robin CPU Scheduling. The goal of this project was to understand how operating systems share CPU time between multiple processes and why scheduling is important.

I focused on how Round-Robin works, how it compares to First-Come, First-Served (FCFS), and how changing the time quantum affects performance.

## What Is Round-Robin Scheduling?
Round-Robin is a CPU scheduling algorithm that gives each process a fixed amount of CPU time, called a **time quantum**.

Processes wait in a ready queue and take turns using the CPU. If a process does not finish during its time quantum, it goes to the back of the queue and waits for another turn.

This helps prevent one CPU-bound process from keeping the CPU for too long.

## Example
For my presentation, I used three processes:
P1 (5ms)
P2 (3ms)
P3 (7ms)

With a time quantum of 2 ms, the processes take turns until they finish.

The execution order is:

P1  P2 P3 P1 P2 P3 P1 P3 P3

This example helped me understand how a Gantt chart represents the order in which processes use the CPU.

## What I Learned

One of the most interesting things I learned was that a smaller time quantum does not always mean better performance.

A smaller time quantum can improve responsiveness because processes receive CPU time more frequently. However, it can also cause more context switches, which create overhead.

A larger time quantum reduces the number of switches but can make other processes wait longer for their next turn.

I also learned that Round-Robin focuses on fairness and responsiveness, but it does not always give the lowest average waiting time.

## AI Exploration

I used ChatGPT to help me explore CPU scheduling and understand the concepts step by step.

Some of the questions I asked were:

- What is CPU scheduling in an operating system, and why is it necessary?
- What is Round-Robin CPU Scheduling, and how is it different from First-Come, First-Served scheduling?
- Can you explain what a process, ready queue, time quantum, and context switch mean using simple real-world examples?
- Can you create a Gantt chart for that example and explain how to read it?
- What happens if I change the time quantum from 2 ms to 4 ms?

The explanations and examples helped me better understand the topic and prepare my presentation.


## References

- Silberschatz, Galvin, and Gagne, *Operating System Concepts* — CPU Scheduling
- [Operating Systems: Three Easy Pieces](https://pages.cs.wisc.edu/~remzi/OSTEP/) — Scheduling chapters
- [Python Documentation](https://docs.python.org/3/) — Python reference for code examples
- ChatGPT — Used for explanations, examples, finding hte above sources, and exploring scheduling concepts

## Conclusion

This project helped me understand how operating systems manage multiple processes and why CPU scheduling involves trade-offs. Round-Robin is relatively easy to understand, but choosing the right time quantum is important for balancing fairness, responsiveness, and efficiency.
