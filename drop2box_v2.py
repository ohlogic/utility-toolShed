#!/usr/bin/python3
#
# Copyright 2019 Stan S
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# You may contact Stan S via electronic mail with the address vfpro777@yahoo.com


import gi
gi.require_version('WebKit2', '4.0')
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk as gtk, WebKit2 as webkit, Gdk
import urllib.request
import re

from gi.repository import GObject
import json

class SimpleBrowser(webkit.WebView):
    # Create custom signals
    __gsignals__ = {
        "js-finished" : (GObject.SignalFlags.RUN_LAST, GObject.TYPE_NONE,())
    }
    
    def __init__(self):
        webkit.WebView.__init__(self)

        self.js_value = None

        s = self.get_settings()
        s.set_property('enable_javascript', True)

    def js_run(self, function_name, js_return=True):
        run_js_finish = self._js_finish if js_return else None
        self.run_javascript(function_name, None, run_js_finish, None)

    def _js_finish(self, webview, result, user_data=None):
        js_result = self.run_javascript_finish(result)
        if js_result is not None:
            value = js_result.get_js_value()
            self.js_value = value.to_string()
            self.emit('js-finished')
            #print((self.js_value))
            
            get_element_values_after_javascript()
        
def generate_genres():
    html = """
            <select id="genre">
            <option value="an">Animated,Cartoon,Family</option>
            <option value="cl">Classics</option>
            <option value="co">Comedy</option>
            <option value="m">Musical</option>
            <option value="s" selected>Sci-Fi</option>
            <option value="ac">Action</option>
            <option value="av">Adventure</option>
            <option value="r">Romance</option>
            <option value="w">Westerm</option>
            <option value="d">Drama</option>
            <option value="sp">Sports</option> 
            <option value="h">Horror</option> 
            </select>
            """
    return html

def drop_cb(wid, context, x, y, time):
    t = "Received file"
    l.set_text(t)
    context.finish(True, False, time)
    return True

def get_element_values(self, element_name):
    print ('button was clicked')
    webview.js_run(f"get_it('{element_name}')")
    
def get_element_values_after_javascript():
    print (webview.js_value)
    pyobj = json.loads(webview.js_value)
    print ("title:" + pyobj["title"])
    print ("genre:" + pyobj["genre"])
    print ("quality:" + pyobj["quality"])
    print ("year:" + pyobj["year"])
    print ("sort_by:" + pyobj["sort_by"])
    print ("filename:" + pyobj["filename"])
    print ("path_full:" + pyobj["path_full"])
    
def on_drag_data_received(widget, drag_context, x, y, data, info, time):

    text = "".join( chr(x) for x in bytearray(data.get_data() ) )
    text = text.replace('file://','').replace('\r\n','')
    
    path = urllib.request.url2pathname(text)
    print("Received path: %s" % path)
    
    path_full = path
    path = path[path.rfind('/')+1:]
    filename = path
    title = path
    
    
    q = re.search(r'\d{4}p',path)
    if q:
        checked1080p = "checked=\"checked\""
        checked720p = ""
    else:
        checked720p = "checked=\"checked\""
        checked1080p = ""
    checked360p = ""
        
    m = re.search(r'\.\d{4}\.',path)
    if m:
        year = m.group(0)[1:-1]
        title = path[0:path.find(m.group())].replace('.', ' ')
        sort_by = title.replace('.', ' ')
    else:
        year = "default"
        sort_by = "default"
    
    genres = generate_genres()
    
    
    html = """
    <html>
    <script>
    function get_it(pstrval) {
        alert(pstrval);
        myObj = {
          title: document.getElementById('title').value,
          sort_by: document.getElementById('sort_by').value,
          genre: document.getElementById('genre').value,
          quality: document.querySelector('input[name="quality"]:checked').value,
          year: document.getElementById('year').value,
          filename: document.getElementById('filename').value,
          path_full: document.getElementById('path_full').value
        };
        var myJSON = JSON.stringify(myObj);
        return myJSON;
    }
    </script>
    
    <style>
    textarea {
        width: 100%;
    }
    input {
        width:80%;
    }
    input[type="radio"] {
        display:inline;
        white-space:nowrap;
        width:10%
    }
    </style>
    
   </head>
   <body>
   """ + f"""      
    <textarea id="path_full">{path_full}</textarea><br>
    <br>
    title:<input id="title" type="text" name="title" value="{title}"><br>
    sort by:<input id="sort_by" type="text" name="sort_by" value="{sort_by}"><br>
    year:<input id="year" type="text" name="year" value="{year}"><br>
    filename:<input id="filename" type="text" name="filename" value="{filename}"><br>
    {genres}
    <form onsubmit="return false;">
    <div style="width:100%">
    <input type="radio" name="quality" value="1080p" {checked1080p}>1080p
    </div>
    <div style="width:100%">
    <input type="radio" name="quality" value="720p" {checked720p}>720p
    </div>
    <div style="width:100%">
    <input type="radio" name="quality" value="360p" {checked360p}>360p
    </div>    
    </form>
    </body></html>
   """

    webview.load_html(html, "file:///")
    
    
w = gtk.Window()
w.set_size_request(400, 250)
w.drag_dest_set(0, [], 0)
w.connect('drag-drop', drop_cb)
w.connect("drag-data-received", on_drag_data_received)
w.drag_dest_set( gtk.DestDefaults.MOTION|
                  gtk.DestDefaults.HIGHLIGHT | gtk.DestDefaults.DROP,
                  [gtk.TargetEntry.new("text/uri-list", 0, 80)], Gdk.DragAction.COPY)      
w.connect('destroy', lambda w: gtk.main_quit())

box = gtk.VBox(spacing=6)

l = gtk.Label("drop file here")
l.set_size_request(200, 150)
box.add(l)


webkit_ver = webkit.get_major_version(), webkit.get_minor_version(), \
webkit.get_micro_version()
webkit_ver = '.'.join(map(str, webkit_ver))
print(f"WebKit2 Version: {webkit_ver}")

webview = SimpleBrowser()

webview.set_size_request(200,315)
box.add(webview)


button = gtk.Button.new_with_label("Click Me")
button.connect("clicked", get_element_values, 'chktst')
button.set_size_request(100,50)
box.add(button)


w.add(box)

w.show_all()
gtk.main()

