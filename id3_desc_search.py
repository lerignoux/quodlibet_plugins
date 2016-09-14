import re

from quodlibet.util.dprint import print_d, print_, print_e, print_w, print_exc
from quodlibet.plugins.query import QueryPlugin
from quodlibet.formats.mp3 import MP3File


class Id3DescSearch(QueryPlugin):
    PLUGIN_ID = "id3_desc_search"
    PLUGIN_NAME = _("ID3 Description Search")
    PLUGIN_DESC = _("Enable to search for text within the ID3 Description field of songs. Syntax is '@(id3d: text)'.")
    key = 'id3d'

    def search(self, data, body):
    	try:
    		if body.match(data['comment']):
    			return True
    	except KeyError:
    		pass

    	try:
    		if body.match(data['comment_other']):
    			return True
    	except KeyError:
    		pass

        return False

    def parse_body(self, body):
    	return re.compile('^.*' + body.strip() + '.*$', flags=re.IGNORECASE)