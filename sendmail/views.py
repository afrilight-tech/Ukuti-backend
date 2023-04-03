from django.core.mail import send_mail
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from backend_api import settings

@csrf_exempt
def sendmail(request):
    if request.method == 'POST':
        name = request.POST['name'] or '--*--'
        phone = request.POST['phone'] or '--*--'
        email = request.POST['email'] or '--*--'
        message = request.POST['message'] or '--*--'
        # recipient_list = [request.POST.get('to_email')]
        if name and email and phone and message:
          deliver = "Hello, " + '\n' + name + ' just reached out to through your contact form, check the response below: \n' + ' ' + '\n' + 'Name: ' + name + '\n' + 'Email: ' + email + '\n' + 'Phone: ' + phone +  '\n' + 'Message: ' + message
          subject = "New Contact Form Entry From " + name
          send_mail(
            subject,
            deliver,
            settings.EMAIL_HOST_USER,
            ['habeeb@afrilight.tech'],           
            fail_silently= False
        )
        return JsonResponse({'message': 'Email sent successfully'})
    else:
      return JsonResponse({'Message': 'You need to make a post request'})    
