__author__ = 'user'
import csv
import sys

def load_dictionary(path_of_dict):
    d = {}
    with open(path_of_dict) as f:
        for line in f:
           (key, val) = line.split()
           d[key] = val
    return d

def format_data_model1(path_of_file,loaded_dict,output_file_path):

    fwm=open(output_file_path,"w")
    with open(path_of_file) as tsvfile:
        reader = csv.reader(tsvfile, dialect='excel-tab')
        for row in reader:
            fwm.write("{}".format(row[0]))
            d={}
            for word in row[1].split():
                index=loaded_dict.get(word,-1)
                if(index!=-1):
                    already_present=d.get(index,-1)
                    if(already_present==-1):
                        fwm.write("\t")
                        fwm.write("{}:1".format(index))
                        d[index]=1
            fwm.write('\n')
    fwm.close()
    return

def format_data_model2(path_of_file,loaded_dict,output_file_path):
    fwm=open(output_file_path,"w")
    with open(path_of_file) as tsvfile:
        reader = csv.reader(tsvfile, dialect='excel-tab')
        for row in reader:
            fwm.write("{}".format(row[0]))
            d={}

            #Create index:frequency for each word in the row and store in dict d
            for word in row[1].split():
                index=loaded_dict.get(word,-1)
                if(index!=-1):
                    d[index]=d.get(index,0)+1

            #Write only those indexes in o/p file where frequency<4
            for word in row[1].split():
                index=loaded_dict.get(word,-1)
                if(index!=-1):
                    numb_count=d.get(index,5)
                    if(numb_count<4):
                        fwm.write("\t")
                        fwm.write("{}:1".format(index))
                        d.pop(index)
            fwm.write('\n')
    fwm.close()
    return

if __name__== "__main__":

    loaded_dict=load_dictionary(sys.argv[4])
    if(int(sys.argv[8])==1):
        format_data_model1(sys.argv[1],loaded_dict,sys.argv[5])
        format_data_model1(sys.argv[2],loaded_dict,sys.argv[6])
        format_data_model1(sys.argv[3],loaded_dict,sys.argv[7])
    else:
        format_data_model2(sys.argv[1],loaded_dict,sys.argv[5])
        format_data_model2(sys.argv[2],loaded_dict,sys.argv[6])
        format_data_model2(sys.argv[3],loaded_dict,sys.argv[7])


