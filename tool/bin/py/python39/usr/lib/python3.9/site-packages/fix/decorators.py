"""Decorators."""

from functools import wraps
from fix.util import Context


def null():
    """Do nothing."""


def with_fixture(create_fixture, **kwargs):
    """Decorate a callable with a fixture."""
    context = Context()
    fixture = create_fixture(context, **kwargs)
    if isinstance(fixture, tuple):
        setup, teardown = fixture
    else:
        setup = fixture
        teardown = null

    def wrap(func):
        """Wrap the callable."""
        @wraps(func)
        def call(*args, **kwargs):
            """Call `setup` and `teardown` before and after `func`."""
            try:
                setup()
                result = func(context, *args, **kwargs)
            finally:
                try:
                    teardown()
                finally:
                    context.clear()
            return result
        return call

    return wrap
