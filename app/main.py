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
		ontology_combo.connect("changed", self.on_ontology_changed)
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
		ic_combo.connect("changed", self.on_ic_changed)
		hbox_ic_selector.pack_start(ic_combo, True, True, 0)

		# setup similarity selection UI
		hbox_sim_selector = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
		box_model_evaluator.pack_start(hbox_sim_selector, True, True, 0)

		label_select_sim = Gtk.Label()
		label_select_sim.set_text("Select Similarity model")
		label_select_sim.set_justify(Gtk.Justification.LEFT)
		hbox_sim_selector.pack_start(label_select_sim, True, True, 0)

		sim_store = Gtk.ListStore(str, str)
		sim_store.append([self.sim_models['resnik'], 'Resnik'])
		sim_store.append([self.sim_models['lin'], 'Lin'])
		sim_store.append([self.sim_models['jian'], 'Jian'])
		sim_store.append([self.sim_models['pirro'], 'Pirro'])
		sim_store.append([self.sim_models['batet'], 'Batet'])
		sim_store.append([self.sim_models['menggu'], 'Meng and Gu'])

		sim_combo = Gtk.ComboBox.new_with_model_and_entry(sim_store)
		sim_combo.set_entry_text_column(1)
		sim_combo.connect("changed", self.on_sim_changed)
		hbox_sim_selector.pack_start(sim_combo, True, True, 0)

		corr_cal_hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
		box_model_evaluator.pack_start(corr_cal_hbox, True, True, 0)

		calc_button = Gtk.Button.new_with_label('Generate correlation')
		calc_button.connect('clicked', self.on_calc_clicked)
		corr_cal_hbox.pack_start(calc_button, True, True, 0)

		results_vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
		box_model_evaluator.pack_start(results_vbox, True, True, 0)

		phy_hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
		results_vbox.pack_start(phy_hbox, True, True, 0)

		label_phy_result = Gtk.Label()
		label_phy_result.set_text('Correlation with Physical benchmark: ')
		label_phy_result.set_justify(Gtk.Justification.LEFT)
		phy_hbox.pack_start(label_phy_result, True, True, 0)

		self.label_phy_result_value = Gtk.Label()
		self.label_phy_result_value.set_text('0.0')
		self.label_phy_result_value.set_justify(Gtk.Justification.LEFT)
		phy_hbox.pack_start(self.label_phy_result_value, True, True, 0)

		med_hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
		results_vbox.pack_start(med_hbox, True, True, 0)

		label_med_result = Gtk.Label()
		label_med_result.set_text('Correlation with Medical benchmark: ')
		label_med_result.set_justify(Gtk.Justification.LEFT)
		med_hbox.pack_start(label_med_result, True, True, 0)

		self.label_med_result_value = Gtk.Label()
		self.label_med_result_value.set_text('0.0')
		self.label_med_result_value.set_justify(Gtk.Justification.LEFT)
		med_hbox.pack_start(self.label_med_result_value, True, True, 0)

		avg_hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
		results_vbox.pack_start(avg_hbox, True, True, 0)

		label_avg_result = Gtk.Label()
		label_avg_result.set_text('Correlation with Average benchmark: ')
		label_avg_result.set_justify(Gtk.Justification.LEFT)
		avg_hbox.pack_start(label_avg_result, True, True, 0)

		self.label_avg_result_value = Gtk.Label()
		self.label_avg_result_value.set_text('0.0')
		self.label_avg_result_value.set_justify(Gtk.Justification.LEFT)
		avg_hbox.pack_start(self.label_avg_result_value, True, True, 0)

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

	def on_ontology_changed(self, combo):
		tree_iter = combo.get_active_iter()
		if tree_iter is not None:
			model = combo.get_model()
			ontology_name = model[tree_iter][0]
			self.selected_ontology = ontology_name
			print self.selected_ontology

	def on_ic_changed(self, combo):
		tree_iter = combo.get_active_iter()
		if tree_iter is not None:
			model = combo.get_model()
			ic_name = model[tree_iter][0]
			self.selected_ic = ic_name
			print self.selected_ic

	def on_sim_changed(self, combo):
		tree_iter = combo.get_active_iter()
		if tree_iter is not None:
			model = combo.get_model()
			sim_name = model[tree_iter][0]
			self.selected_sim = sim_name
			print self.selected_sim

	def on_calc_clicked(self, button):
		print 'clicked'


app = AppWindow()
app.connect('destroy', Gtk.main_quit)
app.show_all()
Gtk.main()




