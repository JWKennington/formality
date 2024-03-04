"""Tests for the mathexp.groups.young module."""
from mathtools.comb.young import YoungTableau
from mathtools.groups import young


class TestYoungGroups:
	"""Test group"""

	def test_fused_row_generators(self):
		"""Test fused_row_generators method"""
		yt = YoungTableau("2 + 2")
		gens = young.fused_row_generators(yt)
		assert gens == [young.Permutation(1, 3)(2, 4)]
