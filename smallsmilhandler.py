#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler (ContentHandler):

    def __init__(self):
        self.width = ""
        self.height = ""
        self.background_color = ""
        self.id = ""
        self.top = ""
        self.bottom = ""
        self.left = ""
        self.right = ""
        self.src = ""
        self.region = ""
        self.begin = ""
        self.dur = ""
        self.tags = []

    def startElement(self, tag, attrs):

        if tag == 'root-layout':

            self.width = attrs.get('width', "")
            self.height = attrs.get('height', "")
            self.background_color = attrs.get
            ('background-color', "")
            self.root_layout = {'width': self.width,
            'height': self.height, 'background-color':
            self.background_color}
            self.tags.append([tag, self.root_layout])

        elif tag == 'region':

            self.id = attrs.get('id', "")
            self.top = attrs.get('top', "")
            self.bottom = attrs.get('bottom', "")
            self.left = attrs.get('left', "")
            self.right = attrs.get('right', "")
            self.region = {'id': self.id, 'top': self.top,
            'bottom': self.bottom, 'left': self.left,
            'right': self.right}
            self.tags.append([tag, self.region])

        elif tag == 'img':

            self.src = attrs.get('src', "")
            self.region = attrs.get('region', "")
            self.begin = attrs.get('begin', "")
            self.dur = attrs.get('dur', "")
            self.img = {'src': self.src, 'region': self.region,
            'begin': self.begin, 'dur': self.dur}
            self.tags.append([tag, self.img])

        elif tag == 'audio':

            self.src = attrs.get('src', "")
            self.begin = attrs.get('begin', "")
            self.dur = attrs.get('dur', "")
            self.audio = {'src': self.src, 'begin': self.begin,
            'dur': self.dur}
            self.tags.append([tag, self.audio])

        elif tag == 'textstream':

            self.src = attrs.get('src', "")
            self.region = attrs.get('region', "")
            self.textstream = {'src': self.src,
            'region': self.region}
            self.tags.append([tag, self.textstream])

    def get_tags(self):
        return self.tags

if __name__ == "__main__":
    parser = make_parser()
    sHandler = SmallSMILHandler()
    parser.setContentHandler(sHandler)
    parser.parse(open('karaoke.smil'))
    lista = sHandler.get_tags()
    print lista
