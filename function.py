#functions taken from scipy.stats and changed according to the use
#from __future__ import division
import numpy as np
import scipy.special as special

def _betai(a, b, x):
    x = np.asarray(x)
    x = np.where(x < 1.0, x, 1.0)  # if x > 1 then return 1.0
    return special.betainc(a, b, x)

def _sum_of_squares(a, axis = 0):
	a, axis = _chk_asarray(a, axis)
    	return np.sum(a*a, axis)

def _chk_asarray(a, axis):
    if axis is None:
        a = np.ravel(a)
        outaxis = 0
    else:
        a = np.asarray(a)
        outaxis = axis

    if a.ndim == 0:
        a = np.atleast_1d(a)

    return a, outaxis

def pearsonr1(x, y):
    	# x and y should have same length.
    	x = np.asarray(x)
    	y = np.asarray(y)
    	n = len(x)
    	mx = x.mean()
    	my = y.mean()
    	xm, ym = x - mx, y - my
    	r_num = np.add.reduce(xm * ym)
    	r_den = np.sqrt(_sum_of_squares(xm) * _sum_of_squares(ym))
	if r_den != 0:
		r = r_num / r_den
	else:
		r = -1
	r = max(min(r, 1.0), -1.0)
    	return r
