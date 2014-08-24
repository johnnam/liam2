from __future__ import (absolute_import, division, print_function,
                        unicode_literals)


class EntityRegistry(dict):
    def add(self, entity):
        self[entity.name] = entity

entity_registry = EntityRegistry()
