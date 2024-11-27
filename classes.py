week_schedule = {
    1: "MONDAY", 
    2: "TUESDAY", 
    3: "WEDNESDAY", 
    4: "THURSDAY", 
    5: "FRIDAY"
}

time_schedule = {
    1: "8:40",
    2: "10:35",
    3: "12:20"
}


class Classroom:
    def __init__(self, room, is_big):
        self.room = room
        self.is_big = is_big

    def __repr__(self):
        return f"{self.room} ({'big' if self.is_big else 'small'})"


class Time:
    def __init__(self, weekday, time):
        self.weekday = weekday
        self.time = time


class Teacher:
    def __init__(self, name, max_hours):
        self.name = name
        self.max_hours = max_hours

    def __repr__(self):
        return f"{self.name}"


class Subject:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.name}"


class Group:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.name}"


class Lesson:
    def __init__(self, teacher, subject, group, is_lecture, per_week):
        self.teacher = teacher
        self.subject = subject
        self.group = group
        self.is_lecture = is_lecture
        self.per_week = per_week

    def __repr__(self):
        return (
            f"{self.teacher} | {self.subject} | {self.group} | "
            f"{'Lecture' if self.is_lecture else 'Laboratories'}"
        )


class Schedule:
    def __init__(self, lessons, classrooms, times):
        self.lessons = lessons
        self.classrooms = classrooms
        self.times = times
    
    def __repr__(self):
        return self.gen_repr()

    def gen_repr(self):
        output = ""
        for i in range(len(self.lessons)):
            output += f"{self.lessons[i]},   {self.classrooms[i]},   {self.times[i]}\n"
        return output


class Domain:
    def __init__(self, day, time, room):
        self.day = day
        self.time = time
        self.room = room


teachers = [
    Teacher("Tkachenko", 10),
    Teacher("Bashuk", 8),
    Teacher("Shyshatska", 9),
    Teacher("Polyshcuk", 8),
    Teacher("Trotsenko", 9),
    Teacher("Taranukha", 8),
    Teacher("Fedorus", 7),
    Teacher("Korobova", 8),
    Teacher("Krasovska", 6),
    Teacher("Kulyabko", 8),
    Teacher("Derevyanchenko", 9),
    Teacher("Mysechko", 7),
    Teacher("Vergunova", 6),
    Teacher("Kryvolap", 8),
    Teacher("Ryabokon", 9),
    Teacher("Pashko", 10)
]

subjects = [
    Subject("IT"),
    Subject("IS"),
    Subject("SDMP"),
    Subject("English"),
    Subject("MMS"),
    Subject("DMT"),
    Subject("PM"),
    Subject("MPC"),
    Subject("Quants"),
    Subject("IR")
]

groups = [
    Group("TTP-41"),
    Group("TTP-42"),
    Group("TK-41"),
    Group("MI-1"),
    Group("MI-2"),
]

classrooms = [
    Classroom(101, True),
    Classroom(104, True),
    Classroom(108, True),
    Classroom(219, False),
    Classroom(214, False),
    Classroom(320, False)
]

schedule = [
    Time(w, n)
    for w in range(1, len(week_schedule.keys()) + 1)
    for n in range(1, len(week_schedule.keys()) + 1)
]

lessons = [
    Lesson(teachers[0], subjects[0], [groups[0]], False, 1),
    Lesson(teachers[1], subjects[1], groups[0:4], True, 1),
    Lesson(teachers[2], subjects[2], [groups[0]], False, 2),
    Lesson(teachers[2], subjects[2], [groups[0]], False, 2),
    Lesson(teachers[3], subjects[3], [groups[0]], False, 1),
    Lesson(teachers[4], subjects[4], groups[0:4], True, 1),
    Lesson(teachers[5], subjects[4], [groups[0]], False, 1),
    Lesson(teachers[5], subjects[6], [groups[0]], False, 1),
    Lesson(teachers[9], subjects[6], groups[0:5], True, 1),
    Lesson(teachers[13], subjects[1], [groups[0]], False, 1),
    Lesson(teachers[13], subjects[5], [groups[0]], False, 2),
    Lesson(teachers[13], subjects[0], [groups[0]], False, 2),
    Lesson(teachers[5], subjects[4], [groups[1]], False, 1),
    Lesson(teachers[5], subjects[4], [groups[2]], False, 1),
    Lesson(teachers[6], subjects[4], [groups[1]], False, 1),
    Lesson(teachers[7], subjects[4], [groups[2]], False, 1),
    Lesson(teachers[8], subjects[3], groups[1:3], True, 1),
    Lesson(teachers[10], subjects[7], [groups[1]], False, 2),
    Lesson(teachers[10], subjects[7], [groups[1]], False, 2),
    Lesson(teachers[10], subjects[7], [groups[2]], False, 2),
    Lesson(teachers[10], subjects[7], [groups[2]], False, 2),
    Lesson(teachers[11], subjects[8], groups[1:3], True, 2),
    Lesson(teachers[11], subjects[8], groups[1:3], True, 2),
    Lesson(teachers[12], subjects[9], groups[1:3], True, 2),
    Lesson(teachers[12], subjects[9], groups[1:3], True, 2),
    Lesson(teachers[5], subjects[4], [groups[3]], False, 1),
    Lesson(teachers[5], subjects[4], [groups[4]], False, 1),
    Lesson(teachers[6], subjects[4], [groups[3]], False, 1),
    Lesson(teachers[6], subjects[4], [groups[4]], False, 1),
    Lesson(teachers[7], subjects[1], groups[3:4], True, 1)
]