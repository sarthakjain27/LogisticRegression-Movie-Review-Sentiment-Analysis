__author__ = 'user'
import numpy as np
import itertools
import sys
import math

def load_dictionary(path_of_dict):
    d = {}
    with open(path_of_dict) as f:
        for line in f:
           (key, val) = line.split()
           d[key] = val
    return d

def sparse_add(X,theta):
    for k,v in X.iteritems():
        theta[k+1]+=v
    return theta

def sparse_sub(X,theta):
    for k,v in X.iteritems():
        theta[k+1]-=v
    return theta

def sparse_dot(X,theta):
    product=0.0
    for k,v in X.iteritems():
        product+=(v*(theta[k+1]))
    return product

def exp_value(product):
    power=0.0
    power=math.exp(product)
    return (power/(1+power))

def update_theta(X,theta,y,exp_val,learn_rate):
    for k,v in X.iteritems():
        theta[k+1]=theta[k+1]+((v*(y-exp_val)*learn_rate))
    return theta

def create_X_matrix(train_file):
    X_matrix=[]
    Y=[]
    with open(train_file) as f:
        for line in f:
            d={}
            entire_row=line.split("\t")
            Y.append(int(entire_row[0]))
            entire_row.pop(0)
            d[-1]=1
            for each in entire_row:
                key_val=each.split(":")
                d[int(key_val[0])]=int(key_val[1])
            X_matrix.append(d)
    return X_matrix,Y



def train_parameters(X_matrix,labels,theta,num_epochs):
    for epoch in xrange(0,(int)(num_epochs)):
        for index,datarows in enumerate(X_matrix):
            dotp=sparse_dot(datarows,theta)
            expov=exp_value(dotp)
            theta=update_theta(datarows,theta,labels[index],expov,0.1)
    return theta

def test(theta,X_matrix,target_labels,target_file):
    fw=open(target_file,"w")
    error_count=0
    for index,datarows in enumerate(X_matrix):
            dotp=sparse_dot(datarows,theta)
            expov=exp_value(dotp)
            if(expov>=0.5):
                prediction=1
            else:
                prediction=0
            fw.write("{}\n".format(prediction))
            if(prediction!=target_labels[index]):
                error_count=error_count+1
    fw.close()
    error_value=(float)(error_count)/(len(target_labels))
    return error_value


if __name__== "__main__":
    loaded_dict=load_dictionary(sys.argv[4])
    theta=np.zeros(len(loaded_dict)+1)
    X_train,labels_train=create_X_matrix(sys.argv[1])
    updated_theta=train_parameters(X_train,labels_train,theta,sys.argv[8])
    print(updated_theta)


    X_valid,labels_valid=create_X_matrix(sys.argv[2])
    X_test,labels_test=create_X_matrix(sys.argv[3])

    train_error=test(updated_theta,X_train,labels_train,sys.argv[5])
    test_error=test(updated_theta,X_test,labels_test,sys.argv[6])
    fwm=open(sys.argv[7],"w")
    fwm.write("error(train): {}\n".format((train_error)))
    fwm.write("error(test): {}\n".format((test_error)))
    print("error(train): {}\n".format((train_error)))
    print("error(test): {}\n".format((test_error)))
    fwm.close()

