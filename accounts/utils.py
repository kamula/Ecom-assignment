'''app utilities files'''
from rest_framework_simplejwt.tokens import RefreshToken
from . models import Account

# get user token
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return str(refresh.access_token)

# validate email
def validate_email(email):
    account = None
    try:
        account = Account.objects.get(email=email)
    except Account.DoesNotExist:
        return None
    if account != None:
        return email

