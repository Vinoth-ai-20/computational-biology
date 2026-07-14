"""Tests for compbio_utils — Wilson et al. (2017) standard."""

import pytest

from compbio_utils import gc_content


class TestGCContent:
    def test_balanced(self):
        assert gc_content("ATGC") == 0.5

    def test_all_at(self):
        assert gc_content("AAAA") == 0.0

    def test_all_gc(self):
        assert gc_content("GGCC") == 1.0

    def test_case_insensitive(self):
        assert gc_content("atgc") == gc_content("ATGC")

    def test_empty_raises(self):
        with pytest.raises(ValueError):
            gc_content("")
