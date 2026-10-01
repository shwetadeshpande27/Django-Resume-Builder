from django import forms
from django.forms import inlineformset_factory

from .models import (
    Resume,
    Education,
    Skill,
    Project,
    Experience,
    Achievement,
)


class ResumeForm(forms.ModelForm):

    class Meta:
        model = Resume

        fields = [
            "full_name",
            "professional_title",
            "email",
            "phone",
            "location",
            "linkedin",
            "github",
            "portfolio",
            "summary",
        ]

        widgets = {
            "full_name": forms.TextInput(
                attrs={
                    "placeholder": "Enter your full name"
                }
            ),

            "professional_title": forms.TextInput(
                attrs={
                    "placeholder": "e.g. Software Developer"
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "placeholder": "example@gmail.com"
                }
            ),

            "phone": forms.TextInput(
                attrs={
                    "placeholder": "+91 XXXXX XXXXX"
                }
            ),

            "location": forms.TextInput(
                attrs={
                    "placeholder": "City, State"
                }
            ),

            "linkedin": forms.URLInput(
                attrs={
                    "placeholder": "https://linkedin.com/in/your-profile"
                }
            ),

            "github": forms.URLInput(
                attrs={
                    "placeholder": "https://github.com/username"
                }
            ),

            "portfolio": forms.URLInput(
                attrs={
                    "placeholder": "https://yourportfolio.com"
                }
            ),

            "summary": forms.Textarea(
                attrs={
                    "placeholder": "Write a short professional summary...",
                    "rows": 5
                }
            ),
        }


class EducationForm(forms.ModelForm):

    class Meta:
        model = Education

        fields = [
            "degree",
            "institution",
            "location",
            "start_year",
            "end_year",
            "description",
        ]

        widgets = {
            "degree": forms.TextInput(
                attrs={
                    "placeholder": "B.Tech Information Technology"
                }
            ),

            "institution": forms.TextInput(
                attrs={
                    "placeholder": "Walchand Institute of Technology"
                }
            ),

            "location": forms.TextInput(
                attrs={
                    "placeholder": "Solapur, Maharashtra"
                }
            ),

            "start_year": forms.TextInput(
                attrs={
                    "placeholder": "2023"
                }
            ),

            "end_year": forms.TextInput(
                attrs={
                    "placeholder": "2027"
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "placeholder": "CGPA, achievements, coursework...",
                    "rows": 3
                }
            ),
        }


class SkillForm(forms.ModelForm):

    class Meta:
        model = Skill

        fields = [
            "name",
            "category",
        ]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Python"
                }
            ),

            "category": forms.TextInput(
                attrs={
                    "placeholder": "Programming Language"
                }
            ),
        }


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project

        fields = [
            "title",
            "technologies",
            "description",
            "project_link",
        ]

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "placeholder": "Online Resume Builder"
                }
            ),

            "technologies": forms.TextInput(
                attrs={
                    "placeholder": "Python, Django, HTML, CSS"
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "placeholder": "Describe your project...",
                    "rows": 4
                }
            ),

            "project_link": forms.URLInput(
                attrs={
                    "placeholder": "https://github.com/username/project"
                }
            ),
        }


class ExperienceForm(forms.ModelForm):

    class Meta:
        model = Experience

        fields = [
            "company",
            "position",
            "start_date",
            "end_date",
            "description",
        ]

        widgets = {
            "company": forms.TextInput(
                attrs={
                    "placeholder": "Company Name"
                }
            ),

            "position": forms.TextInput(
                attrs={
                    "placeholder": "Software Developer Intern"
                }
            ),

            "start_date": forms.TextInput(
                attrs={
                    "placeholder": "June 2026"
                }
            ),

            "end_date": forms.TextInput(
                attrs={
                    "placeholder": "August 2026"
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "placeholder": "Describe your responsibilities...",
                    "rows": 4
                }
            ),
        }


class AchievementForm(forms.ModelForm):

    class Meta:
        model = Achievement

        fields = [
            "description",
        ]

        widgets = {
            "description": forms.Textarea(
                attrs={
                    "placeholder": "Won coding competition...",
                    "rows": 3
                }
            ),
        }


EducationFormSet = inlineformset_factory(
    Resume,
    Education,
    form=EducationForm,
    extra=1,
    can_delete=True
)


SkillFormSet = inlineformset_factory(
    Resume,
    Skill,
    form=SkillForm,
    extra=1,
    can_delete=True
)


ProjectFormSet = inlineformset_factory(
    Resume,
    Project,
    form=ProjectForm,
    extra=1,
    can_delete=True
)


ExperienceFormSet = inlineformset_factory(
    Resume,
    Experience,
    form=ExperienceForm,
    extra=1,
    can_delete=True
)


AchievementFormSet = inlineformset_factory(
    Resume,
    Achievement,
    form=AchievementForm,
    extra=1,
    can_delete=True
)