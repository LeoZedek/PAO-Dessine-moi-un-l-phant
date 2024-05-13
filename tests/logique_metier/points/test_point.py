#!/usr/bin/env python

import numpy as np

from point import Point2D

def test_abscisse():
    assert Point2D(1,2).x == 1

def test_ordonnee():
    assert Point2D(1,2).y == 2

def test_module():
    assert Point2D(3,4).module == 5

def test_argument():
    assert Point2D(0,1).argument == np.pi/2

def test_complex():
    assert complex(Point2D(3,5)) == complex(3,5)
