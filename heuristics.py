from copy import copy
from classes import *


def run(heuristic):
    return backtrack(heuristic, init_domains(), Schedule([], [], []))


def backtrack(heuristic, domains, schedule):
    if not domains:
        return schedule
    pos = heuristic(domains)
    if pos == -1:
        return None
    for d in domains[pos]:
        sch_copy = copy(schedule)
        sch_copy.times.append(Time(d.day, d.time))
        sch_copy.classrooms.append(d.room)
        sch_copy.lessons.append(lessons[pos])

        dom_copy = copy(domains)
        dom_copy.pop(pos)
        dom_copy = update_domains(dom_copy, lessons[pos], d.day, d.time, d.room)

        res = backtrack(heuristic, dom_copy, sch_copy)
        if res:
            return res
    return None


def update_domains(domains, lesson, day, time, room):
    updated_domains = {}
    for key, values in domains.items():
        updated_values = [
            d for d in values if not (
                (d.day, d.time, d.room) == (day, time, room) or
                (d.day, d.time) == (day, time) and (
                    lesson.teacher == lessons[key].teacher or
                    set(map(str, lesson.group)) & set(map(str, lessons[key].group))
                )
            )
        ]
        updated_domains[key] = updated_values
    return updated_domains


def init_domains():
    domains = {}
    buf = []
    buf_lecture = []
    for day in week_schedule.keys():
        for time_slot in time_schedule.keys():
            for room in classrooms:
                buf.append(Domain(day, time_slot, room))
                if room.is_big:
                    buf_lecture.append(Domain(day, time_slot, room))
    for i in range(len(lessons)):
        if lessons[i].is_lecture:
            domains[i] = copy(buf_lecture)
        else:
            domains[i] = copy(buf)
    return domains


def mrv(domains):
    min_len = len(week_schedule) * len(classrooms) * len(time_schedule) * 2
    pos = list(domains.keys())[0]
    for key, value in domains.items():
        if len(value) < min_len:
            min_len = len(value)
            pos = key
    return pos


def degree(domains):
    counts = {}
    for key in domains:
        counts[key] = 0 if lessons[key].is_lecture else 1
        for i in domains:
            if i == key:
                continue
            if lessons[key].teacher == lessons[i].teacher:
                counts[key] += 1
            counts[key] += len(
                set(map(str, lessons[key].group)) & set(map(str, lessons[i].group))
            )
    pos = list(counts.keys())[0]
    max = 0
    for key, value in counts.items():
        if value > max:
            max = value
            pos = key
    return pos


def lcv(domains):
    counts = {}
    for i in domains:
        counts[i] = 0
        for key in domains:
            if i == key:
                continue
            for d in domains[key]:
                if not (
                    d.day == domains[i][0].day
                    and d.time == domains[i][0].time
                    and d.room == domains[i][0].room
                ) and not (
                    d.day == domains[i][0].day
                    and d.time == domains[i][0].time
                    and (
                        lessons[key].teacher == lessons[i].teacher
                        or set(map(str, lessons[key].group))
                        & set(map(str, lessons[i].group))
                    )
                ):
                    counts[i] += 1

    pos = list(counts.keys())[0]
    max = 0
    for key, value in counts.items():
        if value > max:
            max = value
            pos = key
    return pos


def forward_checking(domains):
    return list(domains.keys())[0]