from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.core import serializers
from .models import *
from . import my_method
import json
import datetime
import time


def testing_list(request):
    uname = request.session.get('myname', 'анонимный человек')
    if uname == 'анонимный человек':
        return HttpResponseRedirect('/')
    test = Testing.objects.filter(is_deleted=False)
    stem = Stem.objects.all().values('testing','content')
    context = {'test': test, 'uname': uname, 'stem':stem}

 #   ti = {'haha',datetime.datetime.now()}

    context['time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    try:
        my_method.sort_ranking()
        my_method.scoring()
    except:
        pass


    return render(request, 'testing_list.html', context)


def testing_detail(request,list_pk):
    uname = request.session.get('myname', 'анонимный человек')
    if uname == 'анонимный человек':
        return HttpResponseRedirect('/')
    context = {}
    context['testing'] = get_object_or_404(Testing, pk=list_pk)
    context['uname'] = uname

  #  context['count'] = Testing.objects.get(pk=2)
    context['stem'] = Stem.objects.filter(testing=list_pk).order_by('number')
    context['option'] = Option.objects.filter(stem=list_pk)

 #   context['fillin'] = Fillin.objects.filter(stem=list_pk)
  #  context['fillin'] = Fillin.objects.all().order_by('stem').order_by('number')


##########################################################################################
    context['fillin'] = Fillin.objects.all().values('stem','content')
    context['option'] = Option.objects.all().values('stem','content')

#    return JsonResponse(data2)


    testing = Testing.objects.filter(id=list_pk)
    data = {}
    data['list'] = json.loads(serializers.serialize("json", testing))


    st_time = data['list'][0]['fields']['start_testing_time']
    ed_time = data['list'][0]['fields']['end_testing_time']

    if st_time != None and ed_time != None:
        st_time = st_time.replace('T',' ')
        ed_time = ed_time.replace('T', ' ')

        t0 = datetime.datetime.strptime(st_time, "%Y-%m-%d %H:%M:%S")

        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


        t1 = datetime.datetime.strptime(now, "%Y-%m-%d %H:%M:%S")
        t2 = datetime.datetime.strptime(ed_time, "%Y-%m-%d %H:%M:%S")
        t_left = str(t2-t1)
        t_start = str(t1-t0)

        time_remaining = t_left.split(':')
        time_started = t_start.split(':')
        t = 0


##   status --> 0:考试正在进行  1:考试结束    2:考试时间还未到 3:考试时间设置错误
        if time_started[0][0] != '-':
            if time_remaining[0][0] != '-':
                t += int(time_remaining[0]) * 60 * 60
                t += int(time_remaining[1]) * 60
                t += int(time_remaining[2])
                context['time'] = t
                context['status'] = 0
            else:
                context['time'] = 0
                context['status'] = 1
        else:
            t_on = str(t0 - t1)
            t_until_start = t_on.split(':')
            t += int(t_until_start[0]) * 60 * 60
            t += int(t_until_start[1]) * 60
            t += int(t_until_start[2])
            context['time'] = t
            context['status'] = 2
    else:
        context['time'] = 0
        context['status'] = 3
  #  return JsonResponse(data)


    return render(request ,'testing_detail.html', context)

def score_submit(request):
    if request.is_ajax():
        getData = json.loads(request.body.decode())
        getAnswer = getData['answers']
        getTest = int(getData['testing'])
        getType = getData['type']

        uname = request.session.get('myname', 'анонимный человек')
        if uname == 'анонимный человек':
           return HttpResponseRedirect('/')


        stu = Student.objects.get(name=uname)
        tes = Testing.objects.get(id=getTest)

        b = Stem.objects.filter(testing=tes)

        data = {}

        data['list'] = json.loads(serializers.serialize("json", b))


   #     types = [2,2,2, 2, 2]
        types = getType

        score = 0

        answer = []
        dict_answer = {}
        correct_answer = {}
        c = ''
        for i in range(len(data['list'])):
            if types[i] == 1:  # 如果是选择题
                answer.append(Stem.objects.filter(id=data['list'][i]['pk']))
            else:
                answer.append(Fillin.objects.filter(stem=data['list'][i]['pk']).order_by('number'))

        for i in range(len(types)):
            dict_answer[str(i)] = json.loads(serializers.serialize("json", answer[i]))
            if types[i] == 1:
                correct_answer[str(i)] = dict_answer[str(i)][0]['fields']['answer']
            else:
                if len(dict_answer[str(i)]) != 1:
                    for j in range(len(dict_answer[str(i)])):
                        c += dict_answer[str(i)][j]['fields']['answer'] + '|'
                        if '\xa0' in c:
                            c = c.replace('\xa0', ' ')
                        correct_answer[str(i)] = c
                else:
                    c = dict_answer[str(i)][0]['fields']['answer']
                    if '\xa0' in c:
                        c = c.replace('\xa0', ' ')
                    correct_answer[str(i)] = c
     #               correct_answer[str(i)] = out
      #              correct_answer[str(i)] = c
            c = ''


        ss = Stem.objects.filter(testing=tes)
        stem_score = {}
        stem_score['list'] = json.loads(serializers.serialize("json", ss))

     #  stem_score['list'][0]['fields']['score']

        for i in range(len(getAnswer)):
            getans = getAnswer[i].split('|')
            st_score = stem_score['list'][i]['fields']['score']
            if len(getans) == 1:     #如果这一题的答案只有一个，则直接和正确答案集对比
                qwe = getans[0].split(' ')
                c = ''
                for q in qwe:
                    if q != '':
                        c += str(q) + ' '
                getans[0] = c[:-1]
                if getans[0] == correct_answer[str(i)]:
                    score += st_score      #分数待定
            else:                    #如果一题有多个小题，则先把正确答案集拆分，再分别比较
                corans = correct_answer[str(i)].split('|')
                corans = corans[:-1]
                sp_score = st_score / len(getans)
                for j in range(len(getans)):
                    if getans[j] == corans[j]:
                        score += sp_score

        stu_answer = ''
        for ans in getAnswer:
            qwe = ans.split(' ')
            c = ''
            for q in qwe:
                if q != '':
                    c += str(q) + ' '
            ans = c[:-1]
            stu_answer += ans + '\n'


        sc = Score.objects.create(student=stu, score=score, test=tes, answer=stu_answer)

    #    return JsonResponse(stem_score)

     #   sc = Option.objects.create(comment=p,content=q,stem_id=3)

   #     return JsonResponse()
        return HttpResponse('haha')
     #   return render(request,'testing_list.html')
 #   s = Student(name="haha", score="18", ranking="1")
 #   s.save()
    my_method.sort_ranking()
    return HttpResponse("yeye")
