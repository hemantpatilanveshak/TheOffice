from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in, user_logged_out,user_login_failed
from django.dispatch import receiver

@receiver(user_logged_in,sender=User)
def login_success(sender, request, user , **kwargs):
    print("Function working")
    print("Sender: ",sender)
    print("Request: ",request)
    print("User: ",user)
    print(f"Kwargs: {kwargs}")

    
# user_logged_in.connect(login_success,sender=User)

@receiver(user_logged_out,sender = User)
def logout_success(sender , request , user , **kwargs):
    print("-----Log out --------")
    print("Sender :",sender)
    print("Request: ", request)
    print("User: ", user)
    print(f"Kwargs {kwargs}")

@receiver(user_login_failed,sender= User)
def logout_failed(sender, request , user , **kwargs):
    print("--LogIn Failed--")
    print("Sender: ",sender)
    print("Request: ",request)
    print("User: ",user)
    print(f"Kwargs: {kwargs}")


