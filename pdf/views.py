from django.shortcuts import render
from .models import Profile
from django.contrib import messages
# Create your views here.


def detail_form(request):
    if request.method == 'POST':
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        summary = request.POST.get('summary','')
        degree = request.POST.get('degree','')
        school = request.POST.get('school','')
        university = request.POST.get('university','')
        work_experience = request.POST.get('work','')
        skills = request.POST.get('skills','')

        details = Profile(name = name, email = email, phone = phone, summary = summary, degree = degree, school = school, university = university, work_experience = work_experience, skills = skills)
        details.save()
        # Add success message
        messages.success(request, 'Resume created successfully')

        # Clear messages after rendering
        storage = messages.get_messages(request)
        storage.used = True
    return render(request, 'pdf/user_details.html')

def resume(request, id):
    user_details = Profile.objects.get(pk = id)
    skill_list = user_details.skills.split('.')
    return render(request, 'pdf/resume.html', {'user_details':user_details, 'skill_list': skill_list})