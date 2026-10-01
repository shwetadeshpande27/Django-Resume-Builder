from django.db import models
from django.contrib.auth.models import User


class Resume(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    full_name = models.CharField(max_length=100)
    professional_title = models.CharField(max_length=150, blank=True)

    email = models.EmailField()
    phone = models.CharField(max_length=20)

    location = models.CharField(max_length=150, blank=True)

    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    portfolio = models.URLField(blank=True)

    summary = models.TextField(blank=True)

    # Resume template
    template = models.CharField(
        max_length=100,
        default="classic"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name


class Education(models.Model):
    resume = models.ForeignKey(
        Resume,
        on_delete=models.CASCADE,
        related_name="educations"
    )

    degree = models.CharField(max_length=150)
    institution = models.CharField(max_length=200)
    location = models.CharField(max_length=150, blank=True)

    start_year = models.CharField(max_length=20, blank=True)
    end_year = models.CharField(max_length=20, blank=True)

    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.degree} - {self.institution}"


class Skill(models.Model):
    resume = models.ForeignKey(
        Resume,
        on_delete=models.CASCADE,
        related_name="skills"
    )

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    resume = models.ForeignKey(
        Resume,
        on_delete=models.CASCADE,
        related_name="projects"
    )

    title = models.CharField(max_length=200)
    technologies = models.CharField(max_length=300, blank=True)

    description = models.TextField()

    project_link = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Experience(models.Model):
    resume = models.ForeignKey(
        Resume,
        on_delete=models.CASCADE,
        related_name="experiences"
    )

    company = models.CharField(max_length=200)
    position = models.CharField(max_length=150)

    start_date = models.CharField(max_length=30, blank=True)
    end_date = models.CharField(max_length=30, blank=True)

    description = models.TextField()

    def __str__(self):
        return f"{self.position} - {self.company}"


class Achievement(models.Model):
    resume = models.ForeignKey(
        Resume,
        on_delete=models.CASCADE,
        related_name="achievements"
    )

    description = models.TextField()

    def __str__(self):
        return self.description[:50]