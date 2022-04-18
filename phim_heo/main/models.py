from django.db import models

# Create your models here.

class ToDoList(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.title + '-' + self.description

class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    completed = models.BooleanField()

    def __str__(self):
        return self.title

class User(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name