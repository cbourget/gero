from gero.app.iam.principal.service import PrincipalService
from gero.app.iam.user.service import UserService


def get_user(context, user_id):
    user_service = context.get_instance(UserService)
    return user_service.one_by_id(user_id)


def create_user(context, data):
    principal_service = context.get_instance(PrincipalService)
    user_service = context.get_instance(UserService)

    principal = principal_service.create({
        'id': data['id'],
        'type': 'user'
    })
    return user_service.create({
        'id': principal.id
    })


def update_user(context, data):
    user_service = context.get_instance(UserService)
    return user_service.update(data)


def delete_user(context, user_id):
    principal_service = context.get_instance(PrincipalService)
    user_service = context.get_instance(UserService)
    user_service.delete(user_id)
    principal_service.delete(user_id)


def bootstrap(app):
    app.include('.service')
