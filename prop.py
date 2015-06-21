import random

n=open('nodes1.csv','r')
e=open('edges1.csv','r')
n=n.read()
e=e.read()
n=n.split('\n')
e=e.split('\n')
allnodes=[]
nodes={}
edges={'source':[],'target':[],'label':[]}
two_op=['and','or','!=','<=']
one_op=['not']
op_map={'and':['','and',''],'or':['either','or','or both'],'not':'not','<=':['','implies',''],'!=':['either','or','']}
two_tables={}
one_tables={}
truefalse={'t':True,'T':True,'f':False,'F':False}
allnodes.append([])
implies={'jati':['aaroh','avroh'],'aaroh':['thaat','svar'],'avroh':['thaat','svar'],'thaat':['svar'],'vadi':['pakad'],'samvadi':['vadi']}

for i in range(len(two_op)):
    two_tables[two_op[i]]=[]
    two_tables[two_op[i]].append([True,True,eval("True "+two_op[i]+" True")])
    two_tables[two_op[i]].append([True,False,eval("True "+two_op[i]+" False")])
    two_tables[two_op[i]].append([False,True,eval("False "+two_op[i]+" True")])
    two_tables[two_op[i]].append([False,False,eval("False "+two_op[i]+" False")])

for i in range(len(one_op)):
    one_tables[one_op[i]]=[]
    one_tables[one_op[i]].append([True,eval(one_op[i]+" True")])
    one_tables[one_op[i]].append([False,eval(one_op[i]+" False")])

for i in range(1,len(n)-1):
    instances=n[i].split(',')
    if(instances[1] in nodes.keys()):
        nodes[instances[1]].append(instances[2])
    else:
        nodes[instances[1]]=[]
        nodes[instances[1]].append(instances[2])
    allnodes.append(list(instances[1:3]))

for i in range(1,979):
    instances=e[i].split(',')
    edges['source'].append(instances[0])
    edges['target'].append(instances[1])
    edges['label'].append(instances[2])

aaroh=[]
avroh=[]
svars=[]
for i in range(162):
    aaroh.append('')
    avroh.append('')
    svars.append([])

for i in range(979,3750):
    instances=e[i].split(',')
    if allnodes[int(instances[1])][1].replace("'",'')=='':
	continue
    aaroh[int(instances[0])-1]=aaroh[int(instances[0])-1]+' '+allnodes[int(instances[1])][1].replace("'",'')
    if allnodes[int(instances[1])][1] not in svars[int(instances[0])-1]:
	svars[int(instances[0])-1].append(allnodes[int(instances[1])][1])

for i in range(3750,7004):
    instances=e[i].split(',')
    if allnodes[int(instances[1])][1].replace("'",'')=='':
	continue
    avroh[int(instances[0])-1]=avroh[int(instances[0])-1]+' '+allnodes[int(instances[1])][1].replace("'",'')
    if allnodes[int(instances[1])][1] not in svars[int(instances[0])-1]:
	svars[int(instances[0])-1].append(allnodes[int(instances[1])][1])


#print aaroh
#print avroh
nodes["'aaroh'"]=[]
nodes["'avroh'"]=[]

for i in range(162):
    nodes["'aaroh'"].append(aaroh[i])
    nodes["'avroh'"].append(avroh[i])
    allnodes.append(["'aaroh'",aaroh[i]])
    allnodes.append(["'avroh'",avroh[i]])
    edges['source'].append(str(i+1))
    edges['source'].append(str(i+1))
    edges['target'].append(str(len(allnodes)-2))
    edges['target'].append(str(len(allnodes)-1))
    edges['label'].append("'aaroh'")
    edges['label'].append("'avroh'")

#print one_tables 
#print two_tables 
   
#print nodes.keys()


while True:
    q1=random.randrange(1,1302)
    #print q1
    choice=random.randrange(6)
    ques=''
    option1=''
    option2=''
    if choice<5:
        op=two_op[random.randrange(len(two_tables))]
	if not op=='<=':
	    continue
        record=random.randrange(4)
	row=two_tables[op][record]
        sourceortarget=random.randrange(2)
        source=edges['source'][q1]
        target=edges['target'][q1]
        label=edges['label'][q1]
	#print source+':'+target+':'+label
	type1=''
	type2=''
	impliesflag=0
	print target
        if sourceortarget==0:   #same source
	    #print row
	    listoftargets=[]
            listoflabels=[]
            for i in range(len(edges['source'])):
                if edges['source'][i]==source and edges['label'][i]!=label:
                    listoftargets.append(edges['target'][i])
                    listoflabels.append(edges['label'][i])
            q2=random.randrange(len(listoftargets))
	    if row[0]==False:
		for i in nodes.keys():
		    if allnodes[int(target)][0]==i:
		    	type1=i
		        option1=nodes[i][random.randrange(len(nodes[i]))]
		    	while option1==allnodes[int(target)][1]:
		    	    option1=nodes[i][random.randrange(len(nodes[i]))]
	    else:
	     	type1=allnodes[int(target)][0]
	     	option1=allnodes[int(target)][1]
	    if op=='<=' and (type1.replace("'",'')) not in implies and label.replace("'",'') not in implies:
		#print type1+' or '+label+' not in implies'
	     	continue
	    if row[1]==False:
	     	ctr=0
	        if op=='<=':
		    #print 'label:'+label
		    #print 'Type1: '+type1
		    if type1=="'svar'":
		    	type2=implies[label.replace("'",'')][random.randrange(len(implies[label.replace("'",'')]))]
		    else:
	     	    	type2=implies[type1.replace("'",'')][random.randrange(len(implies[type1.replace("'",'')]))]
		    #print type2
		    if type2=='svar':
		    	option2=nodes["'svar'"][random.randrange(len(nodes["'svar'"]))]
			while option2 in svars[int(source)-1]:
			    option2=nodes["'svar'"][random.randrange(len(nodes["'svar'"]))]
		    elif type2=='vadi':
			option2=nodes["'svar'"][random.randrange(len(nodes["'svar'"]))]
			for k in range(len(listoflabels)):
			    if listoflabels[k]=="'vadi'":
				ans=allnodes[int(listoftargets[k])][1]
				break
			print 'ans:'+ans
			while option2==ans:
			    option2=nodes["'svar'"][random.randrange(len(nodes["'svar'"]))]
			    print 'option2:'+option2
		    else:
	     	    	option2=nodes["'"+type2+"'"][random.randrange(len(nodes["'"+type2+"'"]))]
	     	    	for j in range(len(listoflabels)):
	     		    if listoflabels[j].replace("'",'')==type2:
	     		    	while option2==allnodes[int(listoftargets[j])][1]:
			       	    option2=nodes[type2][random.randrange(len(nodes[type2]))]
			    	break
		    listoflabels[q2]=type2
	        else:
	     	    for i in nodes.keys():
		    	if allnodes[int(listoftargets[q2])][0]==i:
		    	    type2=i
			    option2=nodes[i][random.randrange(len(nodes[i]))]
		    	    while option2==allnodes[int(listoftargets[q2])][1]:
			        option2=nodes[i][random.randrange(len(nodes[i]))]
	    else:
	        if op=='<=':
		    #print 'label:'+label
		    #print 'Type1: '+type1
		    if type1=="'svar'":
		    	type2=implies[label.replace("'",'')][random.randrange(len(implies[label.replace("'",'')]))]
		    else:
	            	type2=implies[type1.replace("'",'')][random.randrange(len(implies[type1.replace("'",'')]))]
		    if type2=='svar':
		        option2=svars[int(source)-1][random.randrange(len(svars[int(source)-1]))]
		     	while option2=="'P'" or option2=="'S'":	
		            option2=svars[int(source)-1][random.randrange(len(svars[int(source)-1]))]
		    elif type2=='vadi':
		     	for k in range(len(listoflabels)):
			    if listoflabels[k]=="'vadi'":
			    	option2=allnodes[int(listoftargets[k])][1]
			    	break
		    else:
	      	    	for j in range(len(listoflabels)):
			    if listoflabels[j].replace("'",'')==type2:
			    	option2=allnodes[int(listoftargets[j])][1]
			    	break
		    listoflabels[q2]=type2
		else:
	    	    type2=allnodes[int(listoftargets[q2])][0]
	     	    option2=allnodes[int(listoftargets[q2])][1]
	    ques=op_map[op][0]+' the '+label+' of '+allnodes[int(source)][1]+' is '+option1+' '+op_map[op][1]+' its '+listoflabels[q2]+' is '+option2+'. (True/False) Press t for true and f for false :  '
	else:       #same target
	    if op=='<=':
	       continue
	    listofsources=[]
	    for i in range(len(edges['target'])):
		if edges['target'][i]==target and edges['label'][i]==label and edges['source'][i]!=source:
		    listofsources.append(edges['source'][i])
	    if len(listofsources)==0:
	 	continue
	    q2=random.randrange(len(listofsources))
	    if row[0]==False:
	        for i in nodes.keys():
		    if allnodes[int(source)][0]==i:
		    	option1=nodes[i][random.randrange(len(nodes[i]))]
		    	while option1==allnodes[int(source)][1]:
		    	    option1=nodes[i][random.randrange(len(nodes[i]))]
	    else:
	    	option1=allnodes[int(source)][1]
	    if row[1]==False:
	        for i in nodes.keys():
		    if allnodes[int(listofsources[q2])][0]==i:
		    	option2=nodes[i][random.randrange(len(nodes[i]))]
		    	while option2==allnodes[int(listofsources[q2])][1]:
		    	    option2=nodes[i][random.randrange(len(nodes[i]))]
	    else:
	    	option2=allnodes[int(listofsources[q2])][1]
	    ques=allnodes[int(target)][1]+' is the '+label+' of '+op_map[op][0]+' '+option1+' '+op_map[op][1]+' '+option2+' '+op_map[op][2]+'. (True/False Press t for true and f for false :  '
	inp=raw_input(ques)
	ans=row[2]
    else:
    	op=one_op[random.randrange(len(one_tables))]
	record=random.randrange(2)
	row=one_tables[op][record]
	sourceortarget=random.randrange(2)
        source=edges['source'][q1]
        target=edges['target'][q1]
        label=edges['label'][q1]
	if sourceortarget==0:
	    if row[0]==False:
		for i in nodes.keys():
		    if allnodes[int(target)][0]==i:
		        option1=nodes[i][random.randrange(len(nodes[i]))]
		    	while option1==allnodes[int(target)][1]:
		    	    option1=nodes[i][random.randrange(len(nodes[i]))]
	    else:
	    	option1=allnodes[int(target)][1]
	    ques=option1+' is '+op+' the '+label+' of '+allnodes[int(source)][1]+'. (True/False) Press t for true and f for false : '
	else:
	    if row[0]==False:
	        for i in nodes.keys():
		    if allnodes[int(source)][0]==i:
		    	option1=nodes[i][random.randrange(len(nodes[i]))]
		    	while option1==allnodes[int(source)][1]:
		    	    option1=nodes[i][random.randrange(len(nodes[i]))]
	    else:
	    	option1=allnodes[int(source)][1]
	    ques=allnodes[int(target)][1]+' is '+op_map[op]+' the '+label+' of '+option1+'. (True/False) Press t for true and f for false : '
	inp=raw_input(ques)
	ans=row[1]
    while inp!='t' and inp!='T' and inp!='f' and inp!='F':
        inp=raw_input('Please enter t for true and f for false.  ')
    if truefalse[inp]==ans:
        print 'Correct!'
    else:
        print 'Incorrect!'
    print
