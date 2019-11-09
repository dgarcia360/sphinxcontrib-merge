# -*- encoding: utf-8 -*-
#
# (c) 2018-present David Garcia (@dgarcia360)
# This code is licensed under MIT license (see LICENSE.md for details)

import requests
from docutils.statemachine import ViewList
from docutils.parsers.rst import directives, Directive, nodes
from sphinx.util.nodes import nested_parse_with_titles

class Merge(Directive):

    has_content = True
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {
        'format': directives.unchanged,
    }

    def run(self):
        lines = requests.get(self.arguments[0]).text.splitlines()
        content = ViewList()
        count = 0
        for line in lines:
            content.append(line, None, count)
            count +=1
        node = nodes.section()
        nested_parse_with_titles(self.state, content, node)
        return node.children

def setup(app):
    app.add_directive('merge', Merge)
