from gero.app.iam.identity.service import IdentityService


def get_user_identity(context, user):
    identity_service = context.get_instance(IdentityService)
    return identity_service.get_user_identity(user)

def bootstrap(app):
    app.include('.service')
