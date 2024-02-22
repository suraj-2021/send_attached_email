from django.shortcuts import render, HttpResponse
from django.conf import settings
from .email_utils import send_email_with_attachment

def my_email_with_attachment_view(request):
    subject = "Email With Files and Images Attachment"
    message = 'Please find all the Attached file in this email'
    from_email = 'myemail@gmail.com'
    recipient_list = ['youremail@gmail.com']
    
    #Attach the Files from the sibling folder "documents" of the templates folder
    attachment_path = 'documents/sample.pdf'
    file_path = settings.BASE_DIR / attachment_path

    send_email_with_attachment(subject,message,from_email,recipient_list,attachment_path)
    return HttpResponse("Email with Attachment Sent Successfully!!")