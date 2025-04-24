"""Utility classes, functions etc."""


class Context(dict):

    """Store context information for a fixture."""

    # pylint: disable=too-few-public-methods

    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)
        self.__dict__ = self

    def __repr__(self):
        kwarg_str = ", ".join("%s=%r" % kv for kv in sorted(self.items()))
        return "%s(%s)" % (self.__class__.__name__, kwarg_str)
