import numpy as np
order=[]
variable={}
variableStack=[]
first={}
follow={}
with open("input_first_follow.txt") as inputFile:
	for production in inputFile:
		st=production[0]
		index=production.find('>')
		order.append(st)
		print(index)
		if production.endswith('\n'):
			rhsProduction=production[index+1:-1].split('|') #for removing '\n'
		else:
			rhsProduction=production[index+1:].split('|')
		print(rhsProduction)
		variable[st]=rhsProduction
print(variable)

def is_a_alpha_form(tempList,var,production):
	print("Production",production)
	if ord(production[0])>=65 and ord(production[0])<91 and production[0]!=var:
		variableStack.append(production[0])
	else:
		tempList.append(production[0])

def find_first():
	for ch in order:
		tempList=[]
		for i in range(len(variable[ch])):
			is_a_alpha_form(tempList,ch,variable[ch][i])
		while len(variableStack)!=0:
			value=variableStack.pop()
			print("value",value)
			for i in range(len(variable[value])):
				print("jjjj",i)
				print(variable[value][i],len(variable[value]),value)
				is_a_alpha_form(tempList,value,variable[value][i])
		first[ch]=tempList;
	print("first ",first)

def get_all_the_follow(value):
	print(value)
	tempList=[]
	for ch in order:
		for rhs in variable[ch]:
			print("rhs ",rhs)
			index=rhs.find(value)
			print("index ",index)
			if index>=0:
				# print("next",rhs[index+1])
				if index==len(rhs)-1:
					print("pagal")
					tempList=tempList+follow[ch]
					print("appended",tempList)
				elif 65<=ord(rhs[index+1])<=90:
					print("murk")
					for element in first[rhs[index+1]]:
						if element!='e':
							tempList.append(element)
					if 'e' in first[rhs[index+1]]:
						tempList=tempList+follow[ch]
					print("appended",tempList)
				elif ord(rhs[index+1])<65 or ord(rhs[index+1])>=91:
					tempList.append(rhs[index+1])
					print("Appended",rhs[index+1],tempList)
	print("tempList",tempList)
	return tempList;

def find_follow():
	for ch in order:
		follow[ch]=[]
	for pair in enumerate(order):
		value=pair[1]
		follow[value]=list(set(get_all_the_follow(value)))
		if pair[0]==0:
			follow[value].append('$')
	print("follow ",follow)

find_first()
find_follow()