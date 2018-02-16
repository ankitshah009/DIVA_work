import os
import sys
import yaml
#from ruamel.yaml import YAML

def convert_yml(input_file,output_dir):
	f = open(input_file,'r') 
	lines=f.readlines()
	f.close()
	output_file_string=input_file.split('_',1)[1].rsplit('.',3)[0]
	#### skip first line
	#del lines[0]
	#for line in lines:
	#	line = line.strip()
					
	
	with open(input_file,'r') as  stream:
		try:
			data= (yaml.load(stream))
			print "Data loaded"
		except yaml.YAMLError as exc:
			print (exc)
	for data_number,data_instance in enumerate(data):
		if data_number == 0:
			continue
		else:
			
			#print data_instance['geom']
			data_geom = data_instance['geom']
			file_name = int(data_instance['geom']['ts0'])
			#print file_name
			final_file_name = output_dir + '/' + output_file_string + '_F_' + str(file_name).zfill(8) + '.json'
			print final_file_name 
			bounding_box = []
			data_temp = data_geom['g0'].split(' ')
			for data1 in data_temp:
				bounding_box.append(int(data1))
			#print bounding_box
			data_temp = data_geom['cset3']
			for key,value in data_temp.iteritems():
				#print key
				#print value
				string = "{\"score\":"  + str(value) + ",\"cat_name\":" + key.lower() + ",\"bbox\":"+str(bounding_box) + "}"
				#print string 
				with open(final_file_name,'a') as f:
					string_new = string + '\n'
					f.write(string_new)
	#input_file = open(input_file).read()
	#print "Read"
	#yaml = YAML()
	#data = yaml.load(input_file)
	#print "data loaded"
	#print data



	
if __name__=="__main__":
	input_file = sys.argv[1]
	output_path = sys.argv[2]
	if not os.path.exists(output_path):
		os.mkdir(output_path)
	convert_yml(input_file,output_path)	 


