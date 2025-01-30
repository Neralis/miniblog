from django.db import models
from django.urls import reverse

class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return self.name

class Blog(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_publish = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('blog-detail', args=[str(self.id)])

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_publish']

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, related_name="comments")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    date_publish = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author}: {self.content}"

    class Meta:
        ordering = ['-date_publish']