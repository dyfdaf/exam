from .models import *
from django.http import HttpResponse

def sort_ranking():
    student = Student.objects.filter(isDeleted=False).exclude(test_score=None)
    lis = []
    for s in student:
        lis.append((s.id,s.test_score))

    b = sorted(lis, key=lambda stu:stu[1])
    b.reverse()
    for i in range(len(b)):
        temp = Student.objects.get(id=str(b[i][0]))
        temp.ranking = i+1
#        temp = Student(id=str(b[i][0]), ranking= i,grades=str(b[i][1]))
        temp.save()


def scoring():
    testings = Testing.objects.filter(is_deleted=False)
    students = Student.objects.filter(isDeleted=False)
    standards = Standard.objects.all()

    stems = Stem.objects.all()

    perf = 0
    good = 0
    passab = 0

    for standard in standards:
        perf = standard.perfectly
        good = standard.good
        passab = standard.passably

    all_score = 0
    for stem in stems:
        all_score += stem.score

    all_score = all_score / len(testings)
    for stu in students:
        scores = Score.objects.filter(student=stu)
        if len(scores) == len(testings):
            score = 0
            for sco in scores:
                score += int(sco.score)
            score = score / len(scores)

            if score >= all_score * perf / 100:
                stu.test_score = 5
            elif score >= all_score * good / 100:
                stu.test_score = 4
            elif score >= all_score * passab / 100:
                stu.test_score = 3
            else:
                stu.test_score = 2
        stu.save()
