from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = '''
    vars: oci_shapes
    version_added: "2.6"
    short_description: In charge of creating the Slurm config for each compute instance
'''

from ansible.plugins.vars import BaseVarsPlugin

FOUND = {}


class VarsModule(BaseVarsPlugin):

    def get_vars(self, loader, path, entities, cache=True):
        ''' parses the inventory file '''

        super(VarsModule, self).get_vars(loader, path, entities)

        nodes = loader.load_from_file('~/nodes.yaml')
        shapes = loader.load_from_file('~/shapes.yaml')

        nodelist = {}
        for hostname, shape in zip(nodes['names'], nodes['shapes']):
            nodelist[hostname] = shapes[shape]

        data = {"slurm_compute_nodelists": nodelist}
        return data