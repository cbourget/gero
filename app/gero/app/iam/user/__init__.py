from gero.app.iam.user.service import UserService


def get_user(context, user_id):
    user_service = context.get_instance(UserService)
    return user_service.one_by_id(user_id)


def create_user(context, data):
    user_service = context.get_instance(UserService)
    return user_service.create(data)


def update_user(context, data):
    user_service = context.get_instance(UserService)
    return user_service.update(data)


def delete_user(context, user_id):
    user_service = context.get_instance(UserService)
    user_service.delete(user_id)


def bootstrap(app):
    app.include('.service')
