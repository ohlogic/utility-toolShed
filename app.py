#from Npp import *        #just comment this out, if you want to run a stand-alone app, and change console.write    statements to    print
import os
parent = os.path.dirname(__file__)
import pygtk
pygtk.require("2.0")
import gtk

class App(object):

	def init_hscale(self, name):                                                      # initialize object

		var = self.builder.get_object(name)
		var.set_range( 1, 100 )                                                       # this is funny, when it's (0, 100) it vanishes when it goes to 0 from being a window
		var.set_value( 100 )        
		
	def __init__(self):

		self.builder = gtk.Builder()
		#self.builder.add_from_file(parent + os.sep + "app.glade")
		self.builder.add_from_file("." + os.sep + "app.glade")

		self.window = self.builder.get_object("window1")
		self.window.set_title("Find - Replace - Find in Files - Mark")

		self.init_hscale("hscale1")

		if (self.window):
			self.window.connect("destroy", gtk.main_quit)                             # this is important, therefore set this directly!
		
# format is	# 'glade_signal_handler'   : method_name in app-class without parentheses # you can comma separate all your handlers here
		handlers = {
		"on_hscale1_value_changed"           : self.opacity_slider,
		"on_chkTransparency1_toggled"        : self.transparency_check_possible_set,
		"on_rdoOnLoseFocus1_toggled"         : self.transparency_group_value_changed, # note a minor workaround n items in an option group to a function
		"on_rdoAlways1_toggled"              : self.transparency_group_value_changed, # wanted ONE radio option value change event, i.e., did a value changed in a radio option group
		"on_window1_focus_in_event"          : self.got_focus,
		"on_window1_focus_out_event"         : self.lost_focus,
		"on_notebook1_switch_page"           : self.tab_changed,
		
		# tab 'Find'
		"on_btnFindNext_clicked"             : self.btnFindNext_clicked,
		"on_btnCount_clicked"                : self.btnCount_clicked,
		"on_btnFindAllOpened_clicked"        : self.btnFindAllOpened_clicked,
		"on_btnFindAllCurrent_clicked"       : self.btnFindAllCurrent_clicked,
		"on_btnClose1_clicked"               : self.close,
		
		# tab 'Replace'
		"on_btnFindNext_replace_tab_clicked" : self.btnFindNext_replace_tab_clicked,
		"on_btnReplace_clicked"              : self.btnReplace_clicked,
		"on_btnReplaceAll_clicked"           : self.btnReplaceAll_clicked,
		"on_btnReplaceAllOpened_clicked"     : self.btnReplaceAllOpened_clicked,
		"on_btnClose2_clicked"               : self.close,
		
		# tab 'Find in Files'
		"on_btnFindAll_clicked"              : self.btnFindAll_clicked,               
		"on_btnReplaceinFiles_clicked"       : self.btnReplaceinFiles_clicked,
		"on_btnClose3_clicked"               : self.close,
		"on_btnDirChooseDialog_clicked"      : self.btnDirChooseDialog_clicked,
		
		# tab 'Mark'
		"on_btnClose4_clicked"               : self.close,                            
		"on_btnMarkAll_clicked"              : self.btnMarkAll_clicked,
		"on_btnClearMarks_clicked"           : self.btnClearMarks_clicked
		}
		
		self.builder.connect_signals(handlers)

		
		self.boolean_group_value_change = False # work-around (to change two radio option toggle events to one group value changed event)
		self.boolean_window_has_focus   = False
		self.window.show_all()
		self.window.set_keep_above(True)        # good this works, but must be after show_all() or it silently doesn't work

	def close(self, w):
		var = self.builder.get_object("window1")
		if not var.emit("delete-event", gtk.gdk.Event(gtk.gdk.DELETE)):
			var.destroy()
		
	def hide_group(self, w):                    # list
	
		for item in w:
			var = self.builder.get_object(item)	# its  Name: '   '
			var.hide()
		
	def show_group(self, w):                    # list
	
		for item in w:
			var = self.builder.get_object(item)	# its  Name: '   '
			var.show()

	def show__from__tab_changed(self, label):	# for simplicity, i just list each label of the tab, can comment out or remove code
	
		if label == 'Find':
			self.show_group(['lblDirection', 'rdoUp', 'rdoDown','chkWrapAround'])
		if label == 'Replace':
			self.show_group(['lblDirection', 'rdoUp', 'rdoDown', 'chkWrapAround'])
		if label == 'Find in Files':
			pass
		if label == 'Mark':
			self.show_group(['chkWrapAround'])
			
	def hide__from__tab_changed(self, label):	# for simplicity, i just list each label of the tab, can comment out or remove code
	
		if label == 'Find':
			pass
		if label == 'Replace':
			pass
		if label == 'Find in Files':
			self.hide_group(['lblDirection', 'rdoUp', 'rdoDown', 'chkWrapAround'])
		if label == 'Mark':
			self.hide_group(['lblDirection', 'rdoUp', 'rdoDown'])
		
	def tab_changed(self, w, page, page_num):
		
		label = w.get_tab_label_text(   w.get_nth_page(page_num)   )
		
		self.hide__from__tab_changed(label)
		self.show__from__tab_changed(label)
                                                                           # console.write('tabs changed, Label:(' + label + ') \n')		
		
	def got_focus ( self , w , event ):
	
		self.boolean_window_has_focus = True                               # console.write('window got focus' + '\n')

		chkTransparency1 = self.builder.get_object("chkTransparency1")     # notify transparency
		self.transparency_check_possible_set(chkTransparency1)             # notify transparency #console.write('LABEL' + w.get_label() + '\n' )
			
	def lost_focus( self , w , event ):
	
		self.boolean_window_has_focus = False                              # console.write('window lost focus' + '\n')

		chkTransparency1 = self.builder.get_object("chkTransparency1")     # notify transparency
		self.transparency_check_possible_set(chkTransparency1)             # notify transparency #console.write('LABEL' + w.get_label() + '\n' )
			
			
	def transparency_group_value_changed(self, w):
	
		self.transparency_group_value_changed_event(w)

	def transparency_group_value_changed_event(self, w):
		
		if self.boolean_group_value_change == True:
		
			chkTransparency1 = self.builder.get_object("chkTransparency1") # notify transparency
			self.transparency_check_possible_set(chkTransparency1)         # notify transparency #console.write('LABEL' + w.get_label() + '\n' )
			
			self.boolean_group_value_change = False
		else:
			self.boolean_group_value_change = True


	def opacity_slider(self, w):
		
		rdoOnLoseFocus1 = self.builder.get_object("rdoOnLoseFocus1")
		active = [r for r in rdoOnLoseFocus1.get_group() if r.get_active()][0]
		label  = active.get_label()
		
		if label == 'Always':                                              # set transparency immediately
		
			self.window.set_opacity(w.get_value()/100.0)
			val = w.get_value()
			hscale1 = self.builder.get_object("hscale1")
			hscale1.set_value(val)
                                                                           # console.write('Setting transparency immediately' + '\n')
		else:
			console.write('Will set transparency on lose focus' + '\n')

			
	def set_grey_out(self, w, make_grey):                                  # just a wrapper that is logically opposite to .set_sensitive()

		for item in w:
			sensitive = False if make_grey == True else True               # this is what to do with confusing methods
			var = self.builder.get_object(item)
			var.set_sensitive(sensitive)

	def set_check(self, w, value):             # can delete or comment out, not used
	                                           # it wasl called with Name: '   ' e.g., #self.set_check("chkTransparency1", False)
		var = self.builder.get_object(w)
		var.set_active(value)

	def get_group_selected_label(self, w):
	
		var = self.builder.get_object(w)
		active = [r for r in var.get_group() if r.get_active()][0]
		label = active.get_label()
		return label

	def get_group_selected_name(self, w):
	
		var = self.builder.get_object(w)
		active = [r for r in var.get_group() if r.get_active()][0]
		name = gtk.Buildable.get_name(active)                              # note: its not active.get_name()   must use    gtk.Buildable.get_name()
		return name

	def transparency_check_possible_set(self, w):	
	                                                                       # console.write('ENTERING          : transparency_check_possible_set,  i am:' + gtk.Buildable.get_name(w) + '\n'); # console.write('   depends on Name: ' + self.get_group_selected_name("rdoOnLoseFocus1") + ' LABEL: ' + self.get_group_selected_label("rdoOnLoseFocus1") + '\n')
		if w.get_active() == True:
		
			self.set_grey_out(['hscale1', 'rdoAlways1', 'rdoOnLoseFocus1'], False)
			
			label = self.get_group_selected_label("rdoOnLoseFocus1")
			
			if label == 'Always':                                          # setting transparency immediately
				
				hscale1 = self.builder.get_object("hscale1")
				val = hscale1.get_value()
				self.window.set_opacity(val/100.0)
                                                                           # console.write('Setting transparency immediately' + '\n')
			else:
				self.window.set_opacity(100.0)                             # console.write('earlier in dev: Will somehow set transparency on lose focus' + '\n')
				
				if self.boolean_window_has_focus == False:
					hscale1 = self.builder.get_object("hscale1")
					val = hscale1.get_value()
					self.window.set_opacity(val/100.0)
                                                                           # console.write('later   in dev: NOW SETTING ON LOSE FOCUS TRANSPARENCY, it is NOW set to: (' + str(val) + ') \n')
		else:
			self.window.set_opacity(100.0)
			self.set_grey_out(['hscale1', 'rdoAlways1', 'rdoOnLoseFocus1'], True)
		
		
	# tab 'Find'
	def btnFindNext_clicked(self, w):
		console.write( "btnFindNext_clicked" + '\n')
		
	def btnCount_clicked(self, w):
		console.write( "btnCount_clicked" + '\n')
	def btnFindAllOpened_clicked(self, w):
		console.write( "btnFindAllOpened_clicked" + '\n')
	def btnFindAllCurrent_clicked(self, w):
		console.write( "btnFindAllCurrent_clicked" + '\n')
	
	# tab 'Replace'
	def btnFindNext_replace_tab_clicked(self, w):
		console.write( "btnFindNext_replace_tab_clicked" + '\n')
	def btnReplace_clicked(self, w):
		console.write( "btnReplace_clicked" + '\n')
	def btnReplaceAll_clicked(self, w):
		console.write( "btnReplaceAll_clicked" + '\n')
	def btnReplaceAllOpened_clicked(self, w):
		console.write( "btnReplaceAllOpened_clicked" + '\n')
	
	#tab 'Find in Files'
	def btnFindAll_clicked(self, w):
		console.write( "btnFindAll_clicked" + '\n')
	def btnReplaceinFiles_clicked(self, w):
		console.write( "btnReplaceinFiles_clicked" + '\n')
	
	def btnDirChooseDialog_clicked(self, w):
		folder_dialog    = gtk.FileChooserDialog(title="Browse for Folder",action=gtk.FILE_CHOOSER_ACTION_SELECT_FOLDER,
                                        buttons=(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL, gtk.STOCK_OPEN, gtk.RESPONSE_OK))
		#folder_dialog.set_default_response(gtk.RESPONSE_OK)
		filter = gtk.FileFilter()
		filter.set_name("Folder")
		filter.add_pattern("*")
		folder_dialog.add_filter(filter)
		#folder_dialog.set_action(gtk.FILE_CHOOSER_ACTION_SELECT_FOLDER)
		
		self.window.set_keep_above(False)
		response = folder_dialog.run()
		folder_dialog.set_keep_above(True)
		
		if response == gtk.RESPONSE_OK:
			console.write ( 'SELECTED:' + folder_dialog.get_filename() + '\n' )
		else:
			console.write ( 'Clicked cancel' + '\n')  # response == gtk.RESPONSE_CANCEL:
		
		self.window.set_keep_above(True)
		console.write( "btnDirChooseDialog_clicked" + '\n')
		folder_dialog.destroy()
		
	#tab 'Mark'
	def btnMarkAll_clicked(self, w):
		console.write( "btnMarkAll_clicked" + '\n')
	def btnClearMarks_clicked(self, w):
		console.write( "btnClearMarks_clicked" + '\n')		

		# how to write to status bar
		# push a new message to the statusbar, using context_id 0
		#var = self.builder.get_object("statusbar1")
		#var.push(0, "write successful to statusbar")		
		
if __name__ == "__main__":
	App()
	gtk.main()