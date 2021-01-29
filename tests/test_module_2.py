"""Tests for module 2"""

import datetime

from scientific_python.modules.module_2 import draw_sinus
from scientific_python.modules.module_2 import tracer_températures


def test_temperatures():
    """Test temperatures drawing"""

    start = datetime.date(2015, 12, 1)
    end = datetime.date(2015, 12, 31)

    tracer_températures(start, end)


def test_sinus():
    """Test sinus drawing"""

    draw_sinus()
