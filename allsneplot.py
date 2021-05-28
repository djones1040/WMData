#!/usr/bin/env python
from astropy.io import ascii
import numpy as np
import pylab as plt

def plotSNHist(allfile = 'sndateall.html'):

	start = False
	year = np.array([])
	for line in open(allfile,'r'):
		if not start and line.startswith('<tr><td></td><td></td><td></td><td>'):
			start = True
		elif start:
			if not line.startswith('<tr>'): continue
			snyr = line.split('<td>')[3].split('</td>')[0]
			if '/' in snyr: snyr = snyr.split('/')[0]
			year = np.append(year,int(snyr))
			

	yrbins = np.arange(1995,2019,1)
	plt.clf()
	plt.hist(year,bins=yrbins)
	plt.xlabel('Year',fontsize=15)
	plt.ylabel('# of Supernovae Discovered',fontsize=15)
	plt.xlim([min(yrbins),max(yrbins)])
	
	return
