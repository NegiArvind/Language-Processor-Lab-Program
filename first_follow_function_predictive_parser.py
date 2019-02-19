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
		# print(index)
		if production.endswith('\n'):
			rhsProduction=production[index+1:-1].split('|') #for removing '\n'
		else:
			rhsProduction=production[index+1:].split('|')
		# print(rhsProduction)
		variable[st]=rhsProduction
print("All Production",variable,"\n")
def is_this_a_non_terminal(ch):

	if ord(ch)>=65 and ord(ch)<91:
		return True
	else:
		return False

def is_a_alpha_form(tempList,var,production):
	# print("Production",production)
	if is_this_a_non_terminal(production[0]) and production[0]!=var:
		variableStack.append(production[0])
	else:
		tempList.append(production[0])

def add_first_val_into_first_ch(first_ch,first_val):
	for item in first_val:
		if item != 'e':
			first_ch.append(item)

	return first_ch;

def find_first():
	for ch in order:
		tempList=[]
		for i in range(len(variable[ch])):
			is_a_alpha_form(tempList,ch,variable[ch][i])
		while len(variableStack)!=0:
			value=variableStack.pop()
			# print("value",value)
			for i in range(len(variable[value])):
				# print("jjjj",i)
				# print(variable[value][i],len(variable[value]),value)
				is_a_alpha_form(tempList,value,variable[value][i])
		first[ch]=list(set(tempList));

	# print("first before",first)

	# Epsilong checking in each and every production
	for ch in order:
		for i in range(len(variable[ch])):
			for val_pair in enumerate(variable[ch][i]):
				val=val_pair[1]
				if is_this_a_non_terminal(val):
					# first[ch]=list(set(first[ch]+first[val]))
					first[ch]=list(set(add_first_val_into_first_ch(first[ch],first[val]))) # All the first[val] will be firs[ch]
					# except 'e'. We will check if first[val] contains e(epsilon) then i will move ahead in rhs production.
					# if e is in first[val] and also it is the last element of particular production(like A->BaCD here it is D)
					# then i will also insert e into first[ch]
					if 'e' in first[val]:
						if val_pair[0]==(len(variable[ch][i])-1):
							first[ch].append('e')
							break
						else:
							# print("inside big bgi",val)
							continue
					else:
						break
				else:
					break

	print("first ",first,"\n")

def add_follow_or_first_or_handle_epsilon(lhs_varible,rhs_production,tempList,index):
	if(index<len(rhs_production)):
		# print("lhs_varible",rhs_production[index])
		for element in first[rhs_production[index]]:
			if element!='e':
				# print("values",element)
				tempList.append(element)
			elif index==len(rhs_production)-1:
				# print("index",index,follow[lhs_varible])
				tempList=tempList+follow[lhs_varible]
				# print("tempList",tempList)
			else:
				tempList=add_follow_or_first_or_handle_epsilon(lhs_varible,rhs_production,tempList,index+1)
	return tempList

def get_all_the_follow(value):
	# print(value)
	tempList=[]
	for ch in order:
		for rhs in variable[ch]:
			# print("rhs ",rhs)
			index=rhs.find(value)
			# print("index ",index)
			if index>=0:
				# print("next",rhs[index+1])
				if index==len(rhs)-1:
					# print("pagal")
					tempList=tempList+follow[ch]
					# print("appended",tempList)
				elif 65<=ord(rhs[index+1])<=90:
					# print("murk")
					# print("value lhs",value)
					tempList=add_follow_or_first_or_handle_epsilon(ch,rhs,tempList,index+1)
					# print("\nfinal tempList\n",tempList)
					# for element in first[rhs[index+1]]:
						# if element!='e':
						# 	tempList.append(element)
						# else:
						# 	handle_epsilon(rhs,tempList,index+1)
					# if 'e' in first[rhs[index+1]]:
					# 	tempList=tempList+follow[ch]
					# print("appended",tempList)
				elif ord(rhs[index+1])<65 or ord(rhs[index+1])>=91:
					tempList.append(rhs[index+1])
					# print("Appended",rhs[index+1],tempList)
	# print("tempList",tempList)
	return tempList;

def find_follow():
	for ch in order:
		follow[ch]=[]
	for pair in enumerate(order):
		value=pair[1]
		# print("VAluesghvsuhg",value)
		follow[value]=list(set(get_all_the_follow(value)))
		if pair[0]==0:
			follow[value].append('$')
	print("follow ",follow,"\n")

find_first()
find_follow()