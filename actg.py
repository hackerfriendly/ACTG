'''
	actg.py

	Reverse complement plugin for Sublime Text 2
'''
import sublime, sublime_plugin

class ReverseComplementCommand(sublime_plugin.TextCommand):
	def complement(self, sequence, reverse=False):
		"""
			Compute the complement of a DNA sequence.

			If reverse is True, reverse it too.
		"""
		flip = {
			'A': 'T',
			'C': 'G',
			'G': 'C',
			'T': 'A',
			'N': 'N',
			'a': 't',
			'c': 'g',
			'g': 'c',
			't': 'a',
			'n': 'n'
		}

		complines = []

		# Gracefully handle line endings
		if '\n' in sequence:
			postfix = '\n'
		else:
			postfix = ''

		for line in sequence.split('\n'):
			line_complement = []
			for i in list(line):
				if not i in flip:
					sublime.error_message('Selection contains non-nucleotides.')
					return False
				line_complement.append(flip[i])

			if reverse:
				complines.append(''.join(line_complement[::-1]))
			else:
				complines.append(''.join(line_complement))

		return postfix.join(complines)

	def run(self, edit):
		sels = self.view.sel()
		for sel in sels:
			if not sel.empty():
				ret = self.complement(self.view.substr(sel), reverse=True)
				if(ret):
					self.view.replace(edit, sel, ret)
