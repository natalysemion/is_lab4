from time import time
from heuristics import *


def print_schedule(solution: Schedule):
    for day in week_schedule:
        print("\n" + "*" * 69)
        print(f"{week_schedule[day]}", end="")
        for time in time_schedule:
            print("\n\n" + time_schedule[time])
            for c in classrooms:
                print(f"\n{c}", end="     ")
                for i in range(len(solution.lessons)):
                    if (solution.times[i].weekday == day and
                        solution.times[i].time == time and
                        solution.classrooms[i].room == c.room):
                        print(solution.lessons[i], end="")


def main():
    solution = run(mrv)
    print_schedule(solution)

    start_time = time()
    run(mrv)
    print('\n')
    print(f"MRV: {time() - start_time}")

    start_time = time()
    run(lcv)
    print(f"LCV: {time() - start_time}")

    start_time = time()
    run(degree)
    print(f"Degree: {time() - start_time}")

    start_time = time()
    run(forward_checking)
    print(f"Forward checking: {time() - start_time}")


if __name__ == "__main__":
    main()