import re
import yaml
mydict={}
with open ('stackrc', 'r') as f:
	prevline=None
	for line in f:
		if prevline is not None:
			prevline=prevline.strip()
			word=re.split(' |=',prevline)
			if word[1] in ('OS_AUTH_URL', 'OS_PASSWORD', 'OS_USERNAME'):
				mydict[word[1]]=word[2]
		prevline=line

print mydict
with open('data1.yml', 'w') as outfile:
    outfile.write( yaml.dump(mydict,default_flow_style=False) )
		
