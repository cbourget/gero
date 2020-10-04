from gero.app.domain.data.service import DataSourceService


def get_data_source(context, data_source_id):
    data_source_service = context.get_instance(DataSourceService)
    return data_source_service.one_by_id(data_source_id)


def create_data_source(context, data):
    data_source_service = context.get_instance(DataSourceService)
    return data_source_service.create({
        'id': data['id'],
        'type': 'postgis'
    })


def update_data_source(context, data):
    data_source_service = context.get_instance(DataSourceService)
    return data_source_service.update(data)


def delete_data_source(context, data_source_id):
    data_source_service = context.get_instance(DataSourceService)
    data_source_service.delete(data_source_id)


def bootstrap(app):
    app.include('.service')
