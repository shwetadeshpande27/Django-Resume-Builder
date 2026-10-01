from django.shortcuts import render, redirect, get_object_or_404

from .forms import (
    ResumeForm,
    EducationFormSet,
    SkillFormSet,
    ProjectFormSet,
    ExperienceFormSet,
    AchievementFormSet,
)

from .models import Resume


# =========================================================
# HOME
# =========================================================

def home(request):
    return render(
        request,
        "resume/home.html"
    )


# =========================================================
# CREATE NEW RESUME
# =========================================================

def create_resume(request):

    if request.method == "POST":

        resume_form = ResumeForm(
            request.POST
        )

        education_formset = EducationFormSet(
            request.POST,
            prefix="education"
        )

        skill_formset = SkillFormSet(
            request.POST,
            prefix="skill"
        )

        project_formset = ProjectFormSet(
            request.POST,
            prefix="project"
        )

        experience_formset = ExperienceFormSet(
            request.POST,
            prefix="experience"
        )

        achievement_formset = AchievementFormSet(
            request.POST,
            prefix="achievement"
        )

        if (
            resume_form.is_valid()
            and education_formset.is_valid()
            and skill_formset.is_valid()
            and project_formset.is_valid()
            and experience_formset.is_valid()
            and achievement_formset.is_valid()
        ):

            # Save main resume
            resume = resume_form.save()

            # Save education
            education_formset.instance = resume
            education_formset.save()

            # Save skills
            skill_formset.instance = resume
            skill_formset.save()

            # Save projects
            project_formset.instance = resume
            project_formset.save()

            # Save experience
            experience_formset.instance = resume
            experience_formset.save()

            # Save achievements
            achievement_formset.instance = resume
            achievement_formset.save()

            return redirect(
                "resume_preview",
                resume_id=resume.id
            )

    else:

        resume_form = ResumeForm()

        education_formset = EducationFormSet(
            prefix="education"
        )

        skill_formset = SkillFormSet(
            prefix="skill"
        )

        project_formset = ProjectFormSet(
            prefix="project"
        )

        experience_formset = ExperienceFormSet(
            prefix="experience"
        )

        achievement_formset = AchievementFormSet(
            prefix="achievement"
        )

    context = {
        "resume_form": resume_form,

        "education_formset": education_formset,

        "skill_formset": skill_formset,

        "project_formset": project_formset,

        "experience_formset": experience_formset,

        "achievement_formset": achievement_formset,

        "edit_mode": False,
    }

    return render(
        request,
        "resume/create_resume.html",
        context
    )


# =========================================================
# EDIT EXISTING RESUME
# =========================================================

def edit_resume(request, resume_id):

    # Find existing resume
    resume = get_object_or_404(
        Resume,
        id=resume_id
    )

    # -----------------------------------------------------
    # POST - SAVE EDITED RESUME
    # -----------------------------------------------------

    if request.method == "POST":

        resume_form = ResumeForm(
            request.POST,
            instance=resume
        )

        education_formset = EducationFormSet(
            request.POST,
            instance=resume,
            prefix="education"
        )

        skill_formset = SkillFormSet(
            request.POST,
            instance=resume,
            prefix="skill"
        )

        project_formset = ProjectFormSet(
            request.POST,
            instance=resume,
            prefix="project"
        )

        experience_formset = ExperienceFormSet(
            request.POST,
            instance=resume,
            prefix="experience"
        )

        achievement_formset = AchievementFormSet(
            request.POST,
            instance=resume,
            prefix="achievement"
        )

        # Validate everything
        if (
            resume_form.is_valid()
            and education_formset.is_valid()
            and skill_formset.is_valid()
            and project_formset.is_valid()
            and experience_formset.is_valid()
            and achievement_formset.is_valid()
        ):

            # Update main resume
            resume_form.save()

            # Update education
            education_formset.instance = resume
            education_formset.save()

            # Update skills
            skill_formset.instance = resume
            skill_formset.save()

            # Update projects
            project_formset.instance = resume
            project_formset.save()

            # Update experience
            experience_formset.instance = resume
            experience_formset.save()

            # Update achievements
            achievement_formset.instance = resume
            achievement_formset.save()

            # Go back to preview
            return redirect(
                "resume_preview",
                resume_id=resume.id
            )

    # -----------------------------------------------------
    # GET - LOAD EXISTING RESUME
    # -----------------------------------------------------

    else:

        # Main resume data
        resume_form = ResumeForm(
            instance=resume
        )

        # Existing education records
        education_formset = EducationFormSet(
            instance=resume,
            prefix="education"
        )

        # Existing skill records
        skill_formset = SkillFormSet(
            instance=resume,
            prefix="skill"
        )

        # Existing project records
        project_formset = ProjectFormSet(
            instance=resume,
            prefix="project"
        )

        # Existing experience records
        experience_formset = ExperienceFormSet(
            instance=resume,
            prefix="experience"
        )

        # Existing achievement records
        achievement_formset = AchievementFormSet(
            instance=resume,
            prefix="achievement"
        )

    context = {
        "resume": resume,

        "resume_form": resume_form,

        "education_formset": education_formset,

        "skill_formset": skill_formset,

        "project_formset": project_formset,

        "experience_formset": experience_formset,

        "achievement_formset": achievement_formset,

        "edit_mode": True,
    }

    return render(
        request,
        "resume/create_resume.html",
        context
    )


# =========================================================
# RESUME PREVIEW
# =========================================================

def resume_preview(request, resume_id):

    resume = get_object_or_404(
        Resume,
        id=resume_id
    )

    return render(
        request,
        "resume/resume_preview.html",
        {
            "resume": resume
        }
    )