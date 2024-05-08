def job_sequencing():
    n = int(input("Enter the number of jobs: "))

    job = []
    deadline = []
    profit = []

    for i in range(n):
        print("\nJob ",i+1)
        job.append(input("Enter job name: "))
        deadline.append(int(input("Enter deadline for job : ")))
        profit.append(int(input("Enter profit for job : ")))

    max_deadline = max(deadline)

    sorted_jobs = sorted(zip(job, deadline, profit), key=lambda x: x[2], reverse=True)

    schedule = [None] * max_deadline
    total_profit = 0

    for j in sorted_jobs:
        current_deadline = j[1]
        slot = current_deadline - 1

        while slot >= 0:
            if schedule[slot] is None:
                schedule[slot] = j[0]
                total_profit += j[2]
                break
            slot -= 1

    return schedule, total_profit

# Example usage
schedule, total_profit = job_sequencing()

print("Job Schedule:")
for i in range(len(schedule)):
    if schedule[i] is not None:
        print("Time Slot", i+1, ":", schedule[i])

print("Total Profit:", total_profit)
