from gero.app.iam.group.service import GroupService


def get_group(context, group_id):
    group_service = context.get_instance(GroupService)
    return group_service.one_by_id(group_id)


def create_group(context, data):
    group_service = context.get_instance(GroupService)
    return group_service.create(data)


def update_group(context, data):
    group_service = context.get_instance(GroupService)
    return group_service.update(data)


def delete_group(context, group_id):
    group_service = context.get_instance(GroupService)
    group_service.delete(group_id)


def bootstrap(app):
    app.include('.service')
