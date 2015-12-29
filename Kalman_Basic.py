from math import *
def f(mu,sigma2,x):
		return (1/sqrt(2*pi*sigma2))*exp(-0.5*(x-mu)**2/sigma2)
		
def update(mean1,var1,mean2,var2):
	new_mean=((mean1*var2)+(mean2*var1))/(var1+var2)
	new_var=1/((1/var1)+(1/var2))
	return [new_mean,new_var]

def predict(mean1,var1,mean2,var2):
	new_mean=mean1+mean2
	new_var=var1+var2
	return [new_mean,new_var]
	
measurements=[5.,6.,7.,9.,10.]
motion=[1.,1.,2.,1.,1.]
measurements_sig=4.0
motion_sig=2.0
mu=0.0
sig=1000.0

p=[mu,sig]

for i in range(len(motion)):
	p=update(p[0],p[1],measurements[i],measurements_sig)
	print p
	p=predict(p[0],p[1],motion[i],motion_sig)
	print p
