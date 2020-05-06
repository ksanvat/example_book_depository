class ReadWriteSerializerMixin:
    read_serializer_class = None
    write_serializer_class = None

    def get_serializer_class(self):
        action = getattr(self, 'action', None)
        assert action is not None, f'Instance of {self.__class__.__name__} should have "action" attribute'

        if action in {'create', 'update', 'partial_update', 'destroy'}:
            return self.get_write_serializer_class()
        else:
            return self.get_read_serializer_class()

    def get_read_serializer_class(self):
        assert self.read_serializer_class is not None, (
            f'{self.__class__.__name__} should either include a "read_serializer_class" attribute,'
            'or override the "get_read_serializer_class" method.'
        )
        return self.read_serializer_class

    def get_write_serializer_class(self):
        assert self.write_serializer_class is not None, (
            f'{self.__class__.__name__} should either include a "write_serializer_class" attribute,'
            'or override the "get_write_serializer_class" method.'
        )
        return self.write_serializer_class
