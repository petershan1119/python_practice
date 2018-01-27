def accepts(*types):
    def check_accepts(f):
        assert len(types) == f.__code__.co_argcount

        def new_f(*args, **kwargs):
            for (a, t) in zip(args, types):
                assert isinstance(a, t), f'arg {a} does not match {t}'
            return f(*args, **kwargs)
        new_f.__name__ = f.__name__

        return new_f
    return check_accepts

