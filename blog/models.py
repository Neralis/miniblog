from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Posts(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_publish = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_publish']

class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    date_publish = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['-date_publish']