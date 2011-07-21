# coding: utf8

#  WeasyPrint converts web documents (HTML, CSS, ...) to PDF.
#  Copyright (C) 2011  Simon Sapin
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as
#  published by the Free Software Foundation, either version 3 of the
#  License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.


import lxml.html


class Document(object):
    def __init__(self, dom):
        assert getattr(dom, 'tag') == 'html', (
            'HTML document expected, got %r.' % (dom,))
        #: lxml HtmlElement object
        self.dom = dom

        #: dict of (element, pseudo_element_type) -> StyleDict
        #: StyleDict: a dict of property_name -> PropertyValue,
        #:    also with attribute access
        self.computed_styles = None

        #: The Box object for the root element.
        self.formatting_structure = None

        #: Layed-out pages and boxes
        self.pages = None

    @classmethod
    def from_string(cls, source):
        """
        Make a document from an HTML string.
        """
        return cls(lxml.html.document_fromstring(source))

    @classmethod
    def from_file(cls, file_or_filename):
        """
        Make a document from a filename or open file object.
        """
        return cls(lxml.html.parse(file_or_filename).getroot())

    def style_for(self, element, pseudo_type=None):
        """
        Convenience method to get the computed styles for an element.
        """
        return self.computed_styles[(element, pseudo_type)]
