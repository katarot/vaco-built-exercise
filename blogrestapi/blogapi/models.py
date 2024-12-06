from django.db import models


# CATEGORY MODEL
# [ General, Technology, and Random ]
# Blog posts are associated to and grouped by Categories, 
class Category(models.Model):
    name = models.CharField("Name", max_length=100) # category name


# BLOG POST MODEL
class BlogPost(models.Model):
    # id: a unique id
    title = models.CharField("Name", max_length=240) # the post title
    contents = models.CharField("Contents", max_length=350) # the post contents
    timestamp = models.DateField(auto_now_add=True) # the time at which the post was originally created
    category = models.ForeignKey(Category, on_delete = models.CASCADE) # a grouping for the post

    def __str__(self):
        return self.name


