from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import EmailMessage
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, 'index.html')

@csrf_exempt
def submit_contact(request):
    if request.method == 'POST':
        name = f"{request.POST.get('first_name', '')} {request.POST.get('last_name', '')}"
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        subject_interest = request.POST.get('interest', 'General Inquiry')
        message = request.POST.get('message', '')

        email_content = f"""
New Client Inquiry Received:

Name: {name}
Email: {email}
Phone: {phone}
Domain/Track: {subject_interest}

Requirement:
{message}
        """

        try:
            email_msg = EmailMessage(
                subject=f"New Lead: {subject_interest} - {name}",
                body=email_content,
                from_email='joksolutionspvtltd@gmail.com',
                to=['joksolutionspvtltd@gmail.com'],
                reply_to=[email]
            )
            email_msg.send(fail_silently=False)
            return JsonResponse({'status': 'success', 'message': 'Message sent successfully! Our team will reach out shortly.'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    return JsonResponse({'status': 'invalid'}, status=400)

@csrf_exempt
def submit_career(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name', '')
        age = request.POST.get('age', '')
        qualification = request.POST.get('qualification', '')
        role = request.POST.get('role', '')
        location = request.POST.get('location', '')
        resume = request.FILES.get('resume', None)

        email_content = f"""
New Career / Internship Application Received:

Full Name: {full_name}
Age: {age}
Qualification: {qualification}
Target Role: {role}
Preferred Location: {location}
        """

        try:
            email_msg = EmailMessage(
                subject=f"Job/Internship Application: {full_name} ({role})",
                body=email_content,
                from_email='joksolutionspvtltd@gmail.com',
                to=['joksolutionspvtltd@gmail.com']
            )

            if resume:
                email_msg.attach(resume.name, resume.read(), resume.content_type)

            email_msg.send(fail_silently=False)
            return JsonResponse({'status': 'success', 'message': 'Application & Resume submitted successfully!'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    return JsonResponse({'status': 'invalid'}, status=400)