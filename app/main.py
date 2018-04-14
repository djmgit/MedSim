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

		box_model_evaluator = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=25)
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

		ic_store = Gtk.ListStore(str, str)
		ic_store.append([self.ic_models['seco'], 'Seco'])
		ic_store.append([self.ic_models['zhou'], 'Zhou'])
		ic_store.append([self.ic_models['sanchez2011'], 'Sanchez 2011'])
		ic_store.append([self.ic_models['sanchez2012'], 'Sanchez 2012'])
		ic_store.append([self.ic_models['our'], 'Adhikari'])
		ic_store.append([self.ic_models['meng'], 'Meng'])
		ic_store.append([self.ic_models['harispe'], 'Harispe'])
		ic_store.append([self.ic_models['hadj'], 'Hadj'])

		ic_combo = Gtk.ComboBox.new_with_model_and_entry(ic_store)
		ic_combo.set_entry_text_column(1)
		hbox_ic_selector.pack_start(ic_combo, True, True, 0)

	def setup_vars(self):

		# setup all the required constants
		self.ontologies = {}
		self.ontologies['SNOMEDCT'] = 'SNOMEDCT'
		self.ontologies['MESH'] = 'MESH'
		self.selected_ontology = self.ontologies['SNOMEDCT']

		# setting up ic models
		self.ic_models = {}
		self.ic_models['seco'] = 'seco'
		self.ic_models['zhou'] = 'zhou'
		self.ic_models['our'] = 'our'
		self.ic_models['sanchez2011'] = 'sanchez2011'
		self.ic_models['sanchez2012'] = 'sanchez2012'
		self.ic_models['meng'] = 'meng'
		self.ic_models['our'] = 'our'
		self.ic_models['harispe'] = 'harispe'
		self.ic_models['hadj'] = 'hadj'
		self.selected_ic = self.ic_models['seco']

		# setting up similarity models
		self.sim_models = {}
		self.sim_models['resnik'] = 'resnik'
		self.sim_models['lin'] = 'lin'
		self.sim_models['jian'] = 'jian'
		self.sim_models['pirro'] = 'pirro'
		self.sim_models['batet'] = 'batet'
		self.sim_models['menggu'] = 'menggu'
		self.selected_similarity = self.sim_models['resnik']


app = AppWindow()
app.connect('destroy', Gtk.main_quit)
app.show_all()
Gtk.main()




