"""Tests for the mathexp.comb.partition module."""

from sympy.combinatorics import IntegerPartition

from maths.comb import partition


class TestPartition:
    """Test group"""

    def test_is_valid_partition(self):
        """Test partition.is_valid_partition method"""

        # Proper case
        assert partition.is_valid_partition("5 + 4 + 3 + 2 + 1")

        # Wrong, not descending
        assert not partition.is_valid_partition("5 + 4 + 3 + 2 + 3")

        # Wrong, not all integers
        assert not partition.is_valid_partition("5 + 4 + 3 + 2 + 1 + a")

        # Wrong symbols used
        assert not partition.is_valid_partition("5 + 4 * 3 + 2 - 1")

        # Wrong, not ending with an integer
        assert not partition.is_valid_partition("5 + 4 + 3 + 2 +")

    def test_from_str(self):
        """Test partition.from_str method"""

        # Proper case
        p = partition.from_str("5 + 4 + 3 + 2 + 1")
        assert p == IntegerPartition([5, 4, 3, 2, 1])

    def test_to_str(self):
        """Test partition.to_str method"""

        # Proper case
        p = IntegerPartition([5, 4, 3, 2, 1])
        assert partition.to_str(p) == "5 + 4 + 3 + 2 + 1"

    def test_values(self):
        """Test partition values"""

        # Proper case
        p = partition.from_str("5 + 3 + 1")
        values = partition.values(p)
        assert values == [
            [1, 2, 3, 4, 5],
            [6, 7, 8],
            [9],
        ]

    def test_values_zero_indexed(self):
        """Test partition values"""

        # Proper case
        p = partition.from_str("5 + 3 + 1")
        values = partition.values(p, zero_indexed=True)
        assert values == [
            [0, 1, 2, 3, 4],
            [5, 6, 7],
            [8],
        ]

    def test_generate_partitions(self):
        """Test partition.generate_partitions method"""

        # Proper case
        parts = list(partition.generate_partitions(5))
        assert parts == [
            [1, 1, 1, 1, 1],
            [2, 1, 1, 1],
            [2, 2, 1],
            [3, 1, 1],
            [3, 2],
            [4, 1],
            [5],
        ]
