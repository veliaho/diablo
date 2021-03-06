#  -*- coding: utf-8 -*-
# yamlmapper.py ---
#
# Created: Wed Apr 11 15:40:26 2012 (-0600)
# Author: Patrick Hull
#

from diablo.datamapper import DataMapper
from diablo import http

class YamlMapper(DataMapper):
    """YAML mapper
    """
    content_type = 'application/yaml'

    def __init__(self, default_flow_style=True):
        self.default_flow_style = default_flow_style

    def _format_data(self, data, charset):
        import yaml
        try:
            return yaml.dump(data)
        except TypeError:
            raise http.InternalServerError('unable to encode data')

    def _parse_data(self, data, charset):
        import yaml
        return yaml.load(data)


