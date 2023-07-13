from django.http import HttpResponse
from django.shortcuts import render
from .models import Speciality, Subject


def speciality_detail(request, pk):
    speciality = Speciality.objects.all().get(pk=pk)
    return render(request, "courses/speciality_detail.html", {
        "speciality": speciality,
    })
def speciality_list(request):
    search = request.GET.get('search', '')
    if search is None:
        specialities = Speciality.objects.all()
    else:
        specialities = Speciality.objects.filter(name__icontains=search)
    if not specialities:
        return HttpResponse("Yo'nalishlar yo'q")
    return render(request, 'courses/speciality.html', {
        'specialities': specialities, 'search': search,
    })


def subject_detail(request, pk):
    subject = Subject.objects.all().get(pk=pk)
    return render(request, 'courses/subject.html', {
        'subject': subject,
    })
def subjects_list(request):
    search = request.GET.get('search', '')
    if search is None:
        subjects = Subject.objects.all()
    else:
        subjects = Subject.objects.filter(name__icontains=search)
    if not subjects:
        return HttpResponse("No Subject")
    return render(request, 'courses/subjects.html', {
        'subjects': subjects, 'search': search,
    })