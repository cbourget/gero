def hook(func):
    def _hook(self, *args, **kwargs):
        before = []
        after = []
        func_name = func.__name__
        for middleware in getattr(self, '_middlewares', []):
            before_func = getattr(middleware, 'before_{}'.format(func_name), None)
            if before_func:
                before.append(before_func)

            after_func = getattr(middleware, 'after_{}'.format(func_name), None)
            if after_func:
                after.append(after_func)

        for f in before:
            f(*args, **kwargs)

        result = func(self, *args, **kwargs)

        for f in after:
            result = f(result, *args, **kwargs)

        return result
    return _hook
