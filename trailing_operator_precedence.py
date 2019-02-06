variable={}
order=[]
variableStack=[]
leading={}
with open("inputLeading.txt") as inputFile:
	for production in inputFile:
		st=production[0]
		index=production.find('>')
		order.append(st)
		print(index)
		if production.endswith('\n'):
			rhsProduction=production[index+1:-1].split('|') #for removing '\n'
		else:
			rhsProduction=production[index+1:].split('|') #for removing '\n'
		print(rhsProduction)
		variable[st]=rhsProduction

print(variable)
print(order)
def is_YaZ_form(tempList,var,production):
	print("var",var,"production",production)
	if ord(production[-1])>=65 and ord(production[-1])<91:
		if production[-1]!=var:
			if not production[-1] in variableStack:
				variableStack.append(production[-1])
		if len(production)>1: #condition is because a rightSentatial form can have only length 1
			tempList.append(production[-2])
	else:
		tempList.append(production[-1])

print("Variable",variable)
for i in range(len(order)):
	print("order",order[i])
	print("order var",	variable[order[i]])
	tempList=[]
	for j in range(len(variable[order[i]])):
		print("jjjj",j)
		is_YaZ_form(tempList,order[i],variable[order[i]][j])
		print("tempList",order[i],tempList)
	print("length",len(variableStack))
	while len(variableStack)!=0:
		ch=variableStack.pop()
		for j in range(len(variable[ch])):
			is_YaZ_form(tempList,ch,variable[ch][j])
		print("inside while",order[i],tempList)
	print(order[i],tempList)
	leading[order[i]]=tempList;
print(leading)