#!/usr/bin/python3

import gi
gi.require_version('WebKit', '3.0')
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk as gtk, WebKit as webkit, Gdk
import urllib.request

def drop_cb(wid, context, x, y, time):
    #t = '\n'.join([str(t) for t in context.list_targets()])
    t = "Received file"
    l.set_text(t)
    context.finish(True, False, time)
    return True

def on_clicked(button):
    print("button was clicked")
    
def on_drag_data_received(widget, drag_context, x, y, data, info, time):

    text = "".join( chr(x) for x in bytearray(data.get_data()) )
    text = text.replace('file://','').replace('\r\n','')
    
    path = urllib.request.url2pathname(text)
    print("Received path: %s" % path)

    id = 123
    title = "nice title"
    year = 1234
    
    html = f"""
    <html>
    <head>
    <style>
    textarea {{
        width: 100%
    }}
    input {{
        width:80%;
    }}
    </style>
    
    </head>
    <body>
    
    <textarea>{path}</textarea><br>
    id:<input type="text" name="id" value="{id}"><br>
    title:<input type="text" name="title" value="{title}"><br>
    year:<input type="text" name="year" value="{year}"><br>

    """
    view.load_html_string(html, "file:///")
    
    
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

view = webkit.WebView()
view.set_size_request(200,130)
box.add(view)


button = gtk.Button.new_with_label("Click Me")
button.connect("clicked", on_clicked)
button.set_size_request(100,50)
box.add(button)


w.add(box)

w.show_all()
gtk.main()
