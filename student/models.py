class ExamMark(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    cia_marks = models.IntegerField()
    semester = models.IntegerField()
