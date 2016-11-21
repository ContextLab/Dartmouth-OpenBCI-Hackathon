import csv
import timeit
import datetime

import plugin_interface as plugintypes

class PluginCSVCollect(plugintypes.IPluginExtended):
	def __init__(self, file_name="collect.csv", delim = ", ", verbose=False):
		now = datetime.datetime.now()
		self.time_stamp = '%d-%d-%d_%d-%d-%d'%(now.year,now.month,now.day,now.hour,now.minute,now.second)
		self.file_name = self.time_stamp
		self.start_time = timeit.default_timer()
		self.delim = delim
		self.verbose = verbose

	def activate(self):
		if len(self.args) > 0:
			if 'no_time' in self.args:
				self.file_name = self.args[0]
			else:
				self.file_name = self.args[0] + '_' + self.file_name;
			if 'verbose' in self.args:
				self.verbose = True

		if not self.file_name.endswith('.csv'):
			self.file_name = self.file_name + '.csv'
		print "Will export CSV to:", self.file_name
		#Open in append mode
		with open(self.file_name, 'a') as f:
			# f.write('%'+self.time_stamp + '\n')
			f.write('%OpenBCI Raw EEG Data\n')
			f.write('%\n')
			f.write('%%Sample Rate = %.1f Hz\n' % self.sample_rate)
			f.write('%First Column = Time in sec\n')
			f.write('%Second Column = SampleIndex\n')
			f.write('%Other Columns = EEG data in microvolts followed by Accel Data (in G) interleaved with Aux Data\n')

	def deactivate(self):
		print "Closing, CSV saved to:", self.file_name
		return

	def show_help(self):
		print "Optional argument: [filename] (default: collect.csv)"

	def __call__(self, sample):
		t = timeit.default_timer() - self.start_time

		#print timeSinceStart|Sample Id
		if self.verbose:
			print("CSV: %f | %d" %(t,sample.id))

		row = ''
		row += str(t)
		row += self.delim
		row += str(sample.id)
		row += self.delim
		for i in sample.channel_data:
			row += str(i)
			row += self.delim
		for i in sample.aux_data:
			row += str(i)
			row += self.delim
		#remove last comma
		row += '\n'
		with open(self.file_name, 'a') as f:
			f.write(row)