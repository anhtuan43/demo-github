from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.html import mark_safe
from markdown import markdown  # Install Markdown library if not installed

# Create your models here.
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name', 'password1','password2'] 

class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cover_image = models.ImageField(upload_to='blog_covers/', null=True, blank=True)
    tags = models.ManyToManyField('Tag', related_name='blogs')

    def __str__(self):
        return self.title

class BlogContent(models.Model):
    blog = models.OneToOneField(Blog, on_delete=models.CASCADE, related_name='content')
    content = models.TextField()
    formatted_content = models.TextField(blank=True)
    image_url = models.URLField(blank=True)  # New field for image URL

    def save(self, *args, **kwargs):
        self.formatted_content = mark_safe(markdown(self.content))
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Content of {self.blog.title}"