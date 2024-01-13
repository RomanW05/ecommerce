from django.core.mail import send_mail

def send_registration_email(user_email):
    send_mail(
        "Welcome",
        "Welcome to our ecommerce",
        "from@example.com",
        [user_email],
        fail_silently=False,
    )