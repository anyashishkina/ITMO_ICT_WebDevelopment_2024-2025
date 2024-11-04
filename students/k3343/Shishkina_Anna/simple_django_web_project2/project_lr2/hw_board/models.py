from django.db import models
from django.contrib.auth.models import User

class Homework(models.Model):
    subject = models.CharField(max_length=100)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name="homework_teacher")
    date_assigned = models.DateField()
    due_date = models.DateField()
    description = models.TextField()
    penalty_info = models.TextField()

    def __str__(self):
        return f"{self.subject} - {self.description[:20]}..."

class HwSubmission(models.Model):
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="homework_student")
    submission_text = models.TextField()
    submission_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} - {self.homework.subject}"

class Grade(models.Model):
    submission = models.OneToOneField(HwSubmission, on_delete=models.CASCADE)
    grade = models.IntegerField()
    comments = models.TextField(blank=True)

    def __str__(self):
        return f"{self.submission.student.username} - {self.grade}"
