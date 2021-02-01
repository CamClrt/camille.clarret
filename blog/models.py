from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)


class Tag(models.Model):
    name = models.CharField(max_length=50)


class Author(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    email = models.EmailField()


class Article(models.Model):
    title = models.CharField(max_length=150)
    body_text = models.TextField(null=False)
    publication_date = models.DateTimeField(auto_now_add=True)
    edition_date = models.DateTimeField(auto_now=True)
    authors = models.ManyToManyField(Author, through="Writing")
    categories = models.ManyToManyField(Category, related_name="category")
    tags = models.ManyToManyField(Tag, related_name="tag")


class Writing(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    main_author = models.BooleanField(default=False)


class Commentaire(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    email = models.EmailField()
    body_text = models.TextField(null=False)
    publication_date = models.DateTimeField(auto_now_add=True)
