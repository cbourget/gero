class EntityMiddleware:

    def __init__(
        self,
        database,
        entity_principals_table,
        entity_principals_table_entity_id):

        self._database = database
        self._entity_principal_table = entity_principals_table
        self._entity_principals_table_entity_id = entity_principals_table_entity_id

    def before__prepare_query(self, query, identity, *args, **kwargs):
        return query

    def after__prepare_query(self, query, identity, *args, **kwargs):
        return query
