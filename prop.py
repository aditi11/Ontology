import random
import sys
import collections

n=open('nodes1.csv','r')
e=open('edges1.csv','r')
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
reverse_map=collections.OrderedDict()
reverse_map['and']='and'
reverse_map['either']='!='
reverse_map['both']='or'
reverse_map['not']='not'
reverse_map['implies']='<='
reverse_map['but']='and not'
two_tables={}
one_tables={}
truefalse={'t':True,'T':True,'f':False,'F':False}
allnodes.append([])
implies={'jati':['aaroh','avroh'],'aaroh':['thaat','svar'],'avroh':['thaat','svar'],'thaat':['svar'],'vadi':['pakad'],'samvadi':['vadi']}
pakads=[]
listofsvars=['S','r','R','g','G','m','M','P','d','D','n','N']

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
        nodes[instances[1]].append(instances[2])
    else:
        nodes[instances[1]]=[]
        nodes[instances[1]].append(instances[2])
    allnodes.append(list(instances[1:3]))

for i in range(162):
    pakads.append('')

for i in range(1,979):
    instances=e[i].split(',')
    edges['source'].append(instances[0])
    edges['target'].append(instances[1])
    edges['label'].append(instances[2])
    if instances[2]=="'pakad'":
	if instances[1]=='[]':
	   continue
	pakads[int(instances[0])-1]=allnodes[int(instances[1])-1][1]

aaroh=[]
avroh=[]
svars=[]
four_grams=[]
five_grams=[]
six_grams=[]

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

for i in range(162):
    aa=nodes["'aaroh'"][i]
    av=nodes["'avroh'"][i]
    pa=pakads[i]
    temp=[]
    four_grams.append([])
    five_grams.append([])
    six_grams.append([])
    for j in range(len(aa)):
	if aa[j] in listofsvars:
	    temp.append(aa[j])
    for j in range(len(temp)-3):
	phrase=temp[j]+' '+temp[j+1]+' '+temp[j+2]+' '+temp[j+3]
	if phrase not in four_grams[i]:
	    four_grams[i].append(phrase)
    for j in range(len(temp)-4):
	phrase=temp[j]+' '+temp[j+1]+' '+temp[j+2]+' '+temp[j+3]+' '+temp[j+4]
	if phrase not in five_grams[i]:
	    five_grams[i].append(phrase)
    for j in range(len(temp)-5):
	phrase=temp[j]+' '+temp[j+1]+' '+temp[j+2]+' '+temp[j+3]+' '+temp[j+4]+' '+temp[j+5]
	if phrase not in six_grams[i]:
	    six_grams[i].append(phrase)
    temp=[]
    for j in range(len(av)):
	if av[j] in listofsvars:
	    temp.append(av[j])
    for j in range(len(temp)-3):
	phrase=temp[j]+' '+temp[j+1]+' '+temp[j+2]+' '+temp[j+3]
	if phrase not in four_grams[i]:
	    four_grams[i].append(phrase)
    for j in range(len(temp)-4):
	phrase=temp[j]+' '+temp[j+1]+' '+temp[j+2]+' '+temp[j+3]+' '+temp[j+4]
	if phrase not in five_grams[i]:
	    five_grams[i].append(phrase)
    for j in range(len(temp)-5):
	phrase=temp[j]+' '+temp[j+1]+' '+temp[j+2]+' '+temp[j+3]+' '+temp[j+4]+' '+temp[j+5]
	if phrase not in six_grams[i]:
	    six_grams[i].append(phrase)
    temp=[]
    for j in range(len(pa)):
	if pa[j] in listofsvars:
	    temp.append(pa[j])
    for j in range(len(temp)-3):
	phrase=temp[j]+' '+temp[j+1]+' '+temp[j+2]+' '+temp[j+3]
	if phrase not in four_grams[i]:
	    four_grams[i].append(phrase)
    for j in range(len(temp)-4):
	phrase=temp[j]+' '+temp[j+1]+' '+temp[j+2]+' '+temp[j+3]+' '+temp[j+4]
	if phrase not in five_grams[i]:
	    five_grams[i].append(phrase)
    for j in range(len(temp)-5):
	phrase=temp[j]+' '+temp[j+1]+' '+temp[j+2]+' '+temp[j+3]+' '+temp[j+4]+' '+temp[j+5]
	if phrase not in six_grams[i]:
	    six_grams[i].append(phrase)

n_grams_dict={}

for i in range(162):
    for j in range(len(four_grams[i])):
	if four_grams[i][j] in n_grams_dict.keys():
	    n_grams_dict[four_grams[i][j]].append(i)
	else:
	    n_grams_dict[four_grams[i][j]]=[]
	    n_grams_dict[four_grams[i][j]].append(i)
    for j in range(len(five_grams[i])):
	if five_grams[i][j] in n_grams_dict.keys():
	    n_grams_dict[five_grams[i][j]].append(i)
	else:
	    n_grams_dict[five_grams[i][j]]=[]
	    n_grams_dict[five_grams[i][j]].append(i)
    for j in range(len(six_grams[i])):
	if six_grams[i][j] in n_grams_dict.keys():
	    n_grams_dict[six_grams[i][j]].append(i)
	else:
	    n_grams_dict[six_grams[i][j]]=[]
	    n_grams_dict[six_grams[i][j]].append(i)


qora=input('Enter 1 to answer questions, 2 to enter questions and 3 to exit: ')

while qora==1:
    q1=random.randrange(1,1302)
    choice=random.randrange(8)
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
	    if op=='<=' and (type1.replace("'",'')) not in implies and label.replace("'",'') not in implies:
	     	continue
	    if row[1]==False:
	     	ctr=0
	        if op=='<=':
		    if type1=="'svar'":
		    	type2=implies[label.replace("'",'')][random.randrange(len(implies[label.replace("'",'')]))]
		    else:
	     	    	type2=implies[type1.replace("'",'')][random.randrange(len(implies[type1.replace("'",'')]))]
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
    else:
	op=two_op[random.randrange(len(two_tables))]
	record=random.randrange(4)
	row=two_tables[op][record]
	if op=='<=':
	    continue
	phrases=n_grams_dict.keys()
	phrase=phrases[random.randrange(len(phrases))]
	if len(phrase)==1:
	    continue
	if row[0]==False:
	    option1=random.randrange(162)
	    while option1 in n_grams_dict[phrase]:
		option1=random.randrange(162)
	else:
	    option1=n_grams_dict[phrase][random.randrange(len(n_grams_dict[phrase]))]
	if row[1]==False:
	    option2=random.randrange(162)
	    while option2 in n_grams_dict[phrase] or option2==option1:
	    	option2=random.randrange(162)
	else:
	    option2=n_grams_dict[phrase][random.randrange(len(n_grams_dict[phrase]))]
	    while option1==option2:
	        option2=n_grams_dict[phrase][random.randrange(len(n_grams_dict[phrase]))]
	ques='The phrase '+phrase+' is present in '+op_map[op][0]+' '+nodes["'raga'"][option1]+' '+op_map[op][1]+' '+nodes["'raga'"][option2]+' '+op_map[op][2]+'. (True/False) Press t for true and f for false: '
	ans=row[2]
    inp=raw_input(ques)
    while inp!='t' and inp!='T' and inp!='f' and inp!='F':
        inp=raw_input('Please enter t for true and f for false.  ')
    if truefalse[inp]==ans:
        print 'Correct!'
    else:
        print 'Incorrect!'
    print
    qora=input('Enter 1 to answer questions, 2 to enter questions and 3 to exit: ')

if qora==3:
    sys.exit()


while qora==2:
    question=raw_input('Enter question: ')
    tokens={'source':[],'label':[],'target':[],'operator':''}
    split1=question.split("'")
    split2=[]
    mod=0
    for i in split1:
    	if mod==0:
		temp=i.split(' ')
		for j in temp:
			if j not in ['the','that','present'] and len(j.strip()) is not 0:
				split2.append(j)
		mod=1
	else:
		split2.append("'"+i+"'")
		mod=0
    '''string=''
    for i in split1:
    	if len(i)==1:
		string=string+' '+i
	else:
		if len(string) is not 0:
			split2.append(string)
			string=''
    		if i not in ['the','that','present'] and i is not '':
			split2.append(i)'''
    print split2
    for i in reverse_map:
    	if i in split2:
		tokens['operator']=reverse_map[i]
    if tokens['operator']=='' or tokens['operator']=='not':
    	ind=split2.index('of')
	tokens['label'].append(split2[ind-1])
	tokens['source'].append(split2[ind+1])
	ind=split2.index('is')
	tokens['target'].append(split2[ind-1])
    elif 'its' in split2:
    	#2 labels
    	ind=split2.index('of')
	tokens['source'].append(split2[ind+1])
	tokens['label'].append(split2[ind-1])
	ind=split2.index('its')
	tokens['label'].append(split2[ind+1])
	count=1
	for i in range(len(split2)):
		if split2[i]=='is':
			tokens['target'].append(split2[i+1])
    else:
  	#2 sources
	ind=split2.index('is')
	tokens['target'].append(split2[ind-1])
	ind=split2.index('of')
	tokens['label'].append(split2[ind-1])
	keywords=op_map[tokens['operator']]
	if isinstance(keywords,list):
		ind=split2.index(keywords[1].split(' ')[0])
		tokens['source'].append(split2[ind-1])
		tokens['source'].append(split2[ind+len(keywords[1].split(' '))])
    outputs=[]
    print tokens
    for i in tokens['source']:
	for j in range(len(tokens['target'])):
		flag=0
		for k in range(len(edges['source'])):
			if allnodes[int(edges['source'][k])][1]==i and allnodes[int(edges['target'][k])][1]==tokens['target'][j] and edges['label'][k]==tokens['label'][j]:
				print k
				outputs.append('True')
				flag=1
				break
		if flag==0:
		 	outputs.append('False')
    print outputs
    if len(outputs)==1:
	print eval(tokens['operator']+' '+outputs[0])
    else:
	print eval(outputs[0]+' '+tokens['operator']+' '+outputs[1])
