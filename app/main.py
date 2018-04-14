import sys
sys.path.append('./')
sys.path.append('../')
#from core import MedCore
import gi
from gi.repository import Gtk

class AppWindow(Gtk.Window):

	def __init__(self):
		Gtk.Window.__init__(self, title="MedSim")
		self.setup_vars()
		self.set_border_width(10)

		box_outer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
		self.add(box_outer)

		box_model_evaluator = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
		box_outer.pack_start(box_model_evaluator, True, True, 0)

		hbox_ontology_selector = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
		box_model_evaluator.pack_start(hbox_ontology_selector, True, True, 0)

		label_select_ontology = Gtk.Label()
		label_select_ontology.set_text("Select ontology")
		label_select_ontology.set_justify(Gtk.Justification.LEFT)
		hbox_ontology_selector.pack_start(label_select_ontology, True, True, 0)

		ontology_store = Gtk.ListStore(str, str)
		ontology_store.append([self.ontologies['SNOMEDCT'], 'SNOMEDCT'])
		ontology_store.append([self.ontologies['MESH'], 'MeSH'])

		ontology_combo = Gtk.ComboBox.new_with_model_and_entry(ontology_store)
		ontology_combo.set_entry_text_column(1)
		hbox_ontology_selector.pack_start(ontology_combo, True, True, 0)

		hbox_ic_selector = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
		box_model_evaluator.pack_start(hbox_ic_selector, True, True, 0)
		
		label_select_ic = Gtk.Label()
		label_select_ic.set_text("Select IC model")
		label_select_ic.set_justify(Gtk.Justification.LEFT)
		hbox_ic_selector.pack_start(label_select_ic, True, True, 0)
		


	def setup_vars(self):
		self.ontologies = {}
		self.ontologies['SNOMEDCT'] = 'SNOMEDCT'
		self.ontologies['MESH'] = 'MESH'
		self.selected_ontology = self.ontologies['SNOMEDCT']
		

app = AppWindow()
app.connect('destroy', Gtk.main_quit)
app.show_all()
Gtk.main()




