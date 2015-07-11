import random

n=open('animalOntoNodes.csv','r')
e=open('animalOntoEdges.csv','r')
n=n.read()
e=e.read()
n=n.split('\n')
e=e.split('\n')
allnodes=[]
nodes={}
edges={'source':[],'target':[],'label':[]}
two_op=['and','or','!=','<=','and not']
one_op=['not','']
op_map={'and':['','and',''],'or':['either','or','or both'],'not':'not','<=':['','implies',''],'!=':['either','or',''],'and not':['','but not',''],'':''}
two_tables={}
one_tables={}
truefalse={'t':True,'T':True,'f':False,'F':False}
allnodes.append([])

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
    if instances[1] in nodes.keys():
        nodes[instances[1]].append(instances[0])
    else:
        nodes[instances[1]]=[]
        nodes[instances[1]].append(instances[0])
    order=[]
    order.append(instances[1])
    order.append(instances[0])
    allnodes.append(order)


for i in range(1,len(e)-1):
    instances=e[i].split(',')
    edges['source'].append(instances[0])
    edges['target'].append(instances[1])
    edges['label'].append(instances[2])

while True:
    q1=random.randrange(1,1302)
    choice=random.randrange(6)
    ques=''
    option1=''
    option2=''
    if choice<5:
        op=two_op[random.randrange(len(two_tables))]
        record=random.randrange(4)
	row=two_tables[op][record]
        sourceortarget=random.randrange(2)
        source=edges['source'][q1]
        target=edges['target'][q1]
        label=edges['label'][q1]
	type1=''
	type2=''
	impliesflag=0
        if sourceortarget==0:   #same source
	    if op=='and not':
	    	continue
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
	    if row[1]==False:
	     	ctr=0
		for i in nodes.keys():
		    if allnodes[int(listoftargets[q2])][0]==i:
		    	type2=i
			option2=nodes[i][random.randrange(len(nodes[i]))]
		    	while option2==allnodes[int(listoftargets[q2])][1]:
			    option2=nodes[i][random.randrange(len(nodes[i]))]
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
		    	    flag=0
		    	    option1=nodes[i][random.randrange(len(nodes[i]))]
		    	    for e in range(len(edges)):
			        if edges['source'][e]==option1 and edges['target'][e]==allnodes[int(target)][1]:
				    flag=1
				    break
			    if flag==1:
				option1=allnodes[int(source)][1]
			    else:
				break
	    else:
	    	option1=allnodes[int(source)][1]
	    if row[1]==False:
	        for i in nodes.keys():
		    if allnodes[int(listofsources[q2])][0]==i:
		    	option2=nodes[i][random.randrange(len(nodes[i]))]
		    	while option2==allnodes[int(listofsources[q2])][1]:
		    	    flag=0
		    	    option2=nodes[i][random.randrange(len(nodes[i]))]
		    	    for e in range(len(edges)):
				if edges['source'][e]==option2 and edges['target'][e]==allnodes[int(target)][1]:
				    flag=1
				    break
			    if flag==1:
			 	option2=allnodes[int(listofsources[q2])][1]
			    else:
			 	break
	    else:
	    	option2=allnodes[int(listofsources[q2])][1]
	    ques=allnodes[int(target)][1]+' is the '+label+' of '+op_map[op][0]+' '+option1+' '+op_map[op][1]+' '+option2+' '+op_map[op][2]+'. (True/False Press t for true and f for false :  '
	ans=row[2]
    elif choice==5:
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
		    	    flag=0
		    	    option1=nodes[i][random.randrange(len(nodes[i]))]
		    	    for e in range(len(edges)):
			        if edges['source'][e]==option1 and edges['target'][e]==allnodes[int(target)][1]:
				    flag=1
				    break
			    if flag==1:
				option1=allnodes[int(source)][1]
			    else:
				break
	    else:
	    	option1=allnodes[int(source)][1]
	    ques=allnodes[int(target)][1]+' is '+op_map[op]+' the '+label+' of '+option1+'. (True/False) Press t for true and f for false : '
	ans=row[1]
    inp=raw_input(ques)
    while inp!='t' and inp!='T' and inp!='f' and inp!='F':
        inp=raw_input('Please enter t for true and f for false.  ')
    if truefalse[inp]==ans:
        print 'Correct!'
    else:
        print 'Incorrect!'
    print
