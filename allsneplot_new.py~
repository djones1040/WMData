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

def plotSNHist_NRAO(allfile = 'osc_all.json',panfitres='SALT2mu_fpan.fitres'):
	plt.rcParams['font.size'] = 15
	plt.rcParams['figure.figsize'] = (10,5)
	import astropy.table as at
	import json
	from txtobj import txtobj
	plt.ion()
	with open(allfile,'r') as fin:
		data = json.load(fin)
	ysedata = at.Table.read('genericsummary.csv',format='ascii.csv',delimiter='|')
	#import pdb; pdb.set_trace()
	
	mdsyear,year,ps1year,yseyear = [],[],[],[]
	snids = []
	for k in data.keys():
		#if len(data[k]['claimedtype']):
		#	#print(data[k]['claimedtype'][0]['value'])
		#	if data[k]['claimedtype'][0]['value'] != 'Ia': continue
		#else: continue
		
		if len(data[k]['discoverdate']):
			year += [int(data[k]['discoverdate'][0]['value'].split('/')[0])]
			snids += [k]
		if len(data[k]['discoverer']):
			if data[k]['discoverer'][0]['value'] == 'PS1' or data[k]['discoverer'][0]['value'] == 'YSE':
				ps1year += [int(data[k]['discoverdate'][0]['value'].split('/')[0])]
				if k[2:] in ysedata['tns_name'] or k in ysedata['tns_name']:
					yseyear += [int(data[k]['discoverdate'][0]['value'].split('/')[0])]
					#import pdb; pdb.set_trace()
					
		if 'PSc' in k:
			mdsyear += [int(data[k]['discoverdate'][0]['value'].split('/')[0])]
			ps1year += [int(data[k]['discoverdate'][0]['value'].split('/')[0])]

			
	lowzyear = []
	fr = txtobj(panfitres,fitresheader=True)
	for i in fr.CID:
		if i.startswith('199') or i.startswith('200'): # or i.startswith('201'):
			lowzyear += [int(i[0:4])]
	
	yrbins = np.arange(1995,2022,1)
	plt.clf()
	plt.hist(year,bins=yrbins,label='all SN discoveries',ec='k')
	plt.hist(lowzyear,bins=yrbins,label='low-$z$ cosmology sample',ec='k')
	#plt.hist(ps1year,bins=yrbins,label='PS1 discoveries',ec='k')
	#plt.hist(mdsyear,bins=yrbins,label='PS1-MDS discoveries',ec='k')
	#plt.hist(yseyear,bins=yrbins,label='YSE discoveries')

	
	plt.xlabel('Year',fontsize=15)
	plt.ylabel('# of Supernovae Discovered',fontsize=15)
	plt.yscale('log')
	plt.ylim(bottom=0.5)
	plt.xlim([min(yrbins),max(yrbins)])
	plt.legend()


	import pdb; pdb.set_trace()
	return

def plotSNHist_NRAO_Movie(allfile = 'osc_all.json',panfitres='SALT2mu_fpan.fitres'):
	plt.rcParams['font.size'] = 15
	plt.rcParams['figure.figsize'] = (10,5)
	import astropy.table as at
	import json
	from txtobj import txtobj
	#plt.ion()
	with open(allfile,'r') as fin:
		data = json.load(fin)
	ysedata = at.Table.read('genericsummary.csv',format='ascii.csv',delimiter='|')
	#import pdb; pdb.set_trace()
	
	mdsyear,year,ps1year,yseyear = [],[],[],[]
	snids = []
	for k in data.keys():
		#if len(data[k]['claimedtype']):
		#	#print(data[k]['claimedtype'][0]['value'])
		#	if data[k]['claimedtype'][0]['value'] != 'Ia': continue
		#else: continue
		
		if len(data[k]['discoverdate']):
			year += [int(data[k]['discoverdate'][0]['value'].split('/')[0])]
			snids += [k]
		if len(data[k]['discoverer']):
			if data[k]['discoverer'][0]['value'] == 'PS1' or data[k]['discoverer'][0]['value'] == 'YSE':
				ps1year += [int(data[k]['discoverdate'][0]['value'].split('/')[0])]
				if k[2:] in ysedata['tns_name'] or k in ysedata['tns_name']:
					yseyear += [int(data[k]['discoverdate'][0]['value'].split('/')[0])]
					#import pdb; pdb.set_trace()
					
		if 'PSc' in k:
			mdsyear += [int(data[k]['discoverdate'][0]['value'].split('/')[0])]
			ps1year += [int(data[k]['discoverdate'][0]['value'].split('/')[0])]

			
	lowzyear = []
	fr = txtobj(panfitres,fitresheader=True)
	for i in fr.CID:
		if i.startswith('199') or i.startswith('200'): # or i.startswith('201'):
			lowzyear += [int(i[0:4])]

	for i,y in enumerate(np.arange(1922,2023,1)):
		yrbins = np.arange(1920,y,1)+0.5
		plt.clf()
		plt.hist(year,bins=yrbins,label='all SN discoveries',ec='k')
		if len(np.where(np.array(lowzyear) < y)[0]):
			plt.hist(lowzyear,bins=yrbins,label='low-$z$ cosmology sample',ec='k')
		if len(np.where(np.array(ps1year) < y)[0]):
			plt.hist(ps1year,bins=yrbins,label='PS1 discoveries',ec='k')
		if len(np.where(np.array(mdsyear) < y)[0]):
			plt.hist(mdsyear,bins=yrbins,label='PS1-MDS discoveries',ec='k')
		#plt.hist(yseyear,bins=yrbins,label='YSE discoveries')

	
		plt.xlabel('Year',fontsize=15)
		plt.ylabel('# of Supernovae Discovered',fontsize=15)
		plt.yscale('log')
		plt.ylim(bottom=0.5)
		plt.xlim([min(yrbins),max(yrbins)])
		plt.legend(loc='upper left')
		plt.ylim([0.5,2e4])
		plt.xlim([1920,2021])
		plt.savefig('snmovie/hist%03i.png'%i,dpi=300)


	return

def mkvideo():

	import cv2
	import os

	image_folder = 'snmovie'
	video_name = 'all_sne.avi'

	#images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
	images = ['snmovie/hist%i.png'%i for i in range(101)]

	frame = cv2.imread(images[0]) #os.path.join(image_folder, images[0]))
	height, width, layers = frame.shape

	video = cv2.VideoWriter(video_name, 0, 1, frameSize=(width,height), fps=15)

	for image in images:
		video.write(cv2.imread(image))

	cv2.destroyAllWindows()
	video.release()
	
if __name__ == "__main__":
	#plotSNHist_NRAO()
	plotSNHist_NRAO_Movie()
	#mkvideo()
