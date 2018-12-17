from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# class ScoreManager(models.Manager):
#     def get_queryset(self):
#         s = Student()
#         return super(ScoreManager, self).get_queryset().

class Student(models.Model):
    name = models.CharField('Ф.И.О.',max_length=60, unique=True)   #Ф.И.О.
    quantityOfTask = models.IntegerField('количество задач',default=0)
    test_score = models.IntegerField('оценка',null=True,blank=True)
    ranking = models.IntegerField('ранкинг',blank=True, null=True)
    isDeleted = models.BooleanField(default=False)
    last_updated_time = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'student'
        ordering = ['name']
    def __str__(self):
        return self.name

 #   studentInfo = StudentManager()



class Stem(models.Model):
    title = models.CharField('заглавие',max_length=40,default="")
    number = models.IntegerField('номер',null=True)
    is_choicequestion = models.BooleanField(default=False)
    score = models.IntegerField('балл')
  #  content = models.TextField(blank=True)
    content = RichTextUploadingField('содержание',blank=True)
    answer = models.CharField('правильный ответ(для вопроса с выбором)',max_length=40, null=True, blank=True)
    testing = models.ForeignKey('Testing', on_delete=False)
    class Meta:
        unique_together = ('number','testing')

    def __str__(self):
        return self.title

class Option(models.Model):
    comment = models.CharField('комментарий',max_length=40, default="пишите описание выбора")
    content = models.CharField('содержание',max_length=100,null=True)
    stem = models.ForeignKey('Stem',on_delete=False)
    def __str__(self):
        return self.comment

class Fillin(models.Model):
    number = models.IntegerField('номер')
    stem = models.ForeignKey('Stem', on_delete=False)
    content = models.CharField('содержание',max_length=100, null=True, blank=True)
    answer = models.CharField('правильный ответ',max_length=50, null=True)
    class Meta:
        unique_together = ('number','stem')
    def __str__(self):
        return "<%s %s>" %(self.number,self.stem)

class Testing(models.Model):
    title = models.CharField('заглавие',max_length=50, unique=True)
  #  content = RichTextUploadingField()
#    checkout = RichTextUploadingField(blank=True,null=True)
    comment = models.TextField('комментарий',null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    start_testing_time = models.DateTimeField('время начала тестирования',blank=True,null=True, editable=True)
    end_testing_time = models.DateTimeField('время окончания тестирования',blank=True, null=True, editable=True)

    def __str__(self):
        return self.title

class Score(models.Model):
    test = models.ForeignKey(Testing, to_field='id', on_delete=False)
    score = models.IntegerField('балл')
    student = models.ForeignKey(Student, to_field='id',on_delete=False)
    last_updated_time = models.DateTimeField(auto_now=True)
    answer = models.TextField('ответ студента   ',null=True,blank=True)

    class Meta:
        unique_together = ('test','student')

class Standard(models.Model):
    perfectly = models.IntegerField('отлично')
    good = models.IntegerField('хорошо')
    passably = models.IntegerField('удовлетворительно')