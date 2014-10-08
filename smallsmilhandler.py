#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler (ContentHandler):

    def __init__(self):
        self.width = ""
        self.height = ""
        self.background_color = ""
        self.region_id = ""
        self.region_top = ""
        self.region_bottom = ""
        self.region_left = ""
        self.region_right = ""
        self.img_src = ""
        self.img_region = ""
        self.img_begin = ""
        self.img_dur = ""
        self.audio_src = ""
        self.audio_begin = ""
        self.audio_dur = ""
        self.textstream_src = ""
        self.textstream_region = ""
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

            self.region_id = attrs.get('id', "")
            self.region_top = attrs.get('top', "")
            self.region_bottom = attrs.get('bottom', "")
            self.region_left = attrs.get('left', "")
            self.region_right = attrs.get('right', "")
            self.region = {'id': self.region_id, 'top': self.region_top,
            'bottom': self.region_bottom, 'left': self.region_left,
            'right': self.region_right}
            self.tags.append([tag, self.region])

        elif tag == 'img':

            self.img_src = attrs.get('src', "")
            self.img_region = attrs.get('region', "")
            self.img_begin = attrs.get('begin', "")
            self.img_dur = attrs.get('dur', "")
            self.img = {'src': self.img_src, 'region': self.img_region,
            'begin': self.img_begin, 'dur': self.img_dur}
            self.tags.append([tag, self.img])

        elif tag == 'audio':

            self.audio_src = attrs.get('src', "")
            self.audio_begin = attrs.get('begin', "")
            self.audio_dur = attrs.get('dur', "")
            self.audio = {'src': self.audio_src, 'begin': self.audio_begin,
            'dur': self.audio_dur}
            self.tags.append([tag, self.audio])

        elif tag == 'textstream':

            self.textstream_src = attrs.get('src', "")
            self.textstream_region = attrs.get('region', "")
            self.textstream = {'src': self.textstream_src,
            'region': self.textstream_region}
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
