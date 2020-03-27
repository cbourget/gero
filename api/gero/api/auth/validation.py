def validate_login(login):
    if not login:
        raise ValidationError('login', 'Required')
    return login


def validate_password(password):
    if not password:
        raise ValidationError('password', 'Required')
    return password
