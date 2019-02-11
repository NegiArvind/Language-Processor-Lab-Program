from leading_operator_precedence import *
from trailing_operator_precedence import *

prcedence_table={}
def is_this_a_non_terminal(ch):
	if ord(ch)>=65 and ord(ch)<91:
		return True
	else:
		return False

def add_into_table(row_value,column_value,sign):
	if(prcedence_table.get(row_value)==None):
		prcedence_table[row_value]={}
	prcedence_table[row_value][column_value]=sign


def fill_the_table_on_trailing_or_leading(is_leading,templist,temp_terminal):
	for ch in templist:
		if(is_leading):
			# print("hello",ch,temp_terminal,templist)
			add_into_table(temp_terminal,ch,'<')
		else:
			# print("Hi",temp_terminal,ch,templist)
			add_into_table(ch,temp_terminal,'>')


def check_all_the_rules_and_then_apply(i,rhs_production):
	temp_terminal=rhs_production[i];
	if i>0 and is_this_a_non_terminal(rhs_production[i-1]):
		fill_the_table_on_trailing_or_leading(False,trailing[rhs_production[i-1]],temp_terminal)

	if i+1<len(rhs_production):
		if is_this_a_non_terminal(rhs_production[i+1]):
			fill_the_table_on_trailing_or_leading(True,leading[rhs_production[i+1]],temp_terminal)
			if i+2<len(rhs_production) and is_this_a_non_terminal(rhs_production[i+2])==False:
				# print("pagal")
				add_into_table(temp_terminal,rhs_production[i+2],'=')
		else:
			add_into_table(temp_terminal,rhs_production[i+1],'=')

def calculate_precedence_table():
	for non_terminal in order:
		for rhs_production in variable[non_terminal]:
			for i in range(0,len(rhs_production)):
				if not is_this_a_non_terminal(rhs_production[i]):
					# print("value",rhs_production[i])
					check_all_the_rules_and_then_apply(i,rhs_production)
					# print("Updated ",prcedence_table)


	prcedence_table['$']={}
	for non_terminal in leading[order[0]]:
		prcedence_table['$'][non_terminal]='<'
	for non_terminal in trailing[order[0]]:
		prcedence_table[non_terminal]['$']='>'

	prcedence_table['$']['$']='Accept'
	print("Precedence table ",prcedence_table)
	for row,value in prcedence_table.items():
		print(row,"-->",value)


def operator_parser(input_string):
	stack=[]
	input_string+='$'
	stack.append('$')
	i=0;
	while len(stack)!=0:
		stack_top=stack[-1]
		# print("stack_top outside",stack_top)
		if i<len(input_string) and stack_top==input_string[i]=='$':
			print("Given string is successfully parsed\n")
			break;

		elif i<len(input_string):
			try:
				if(prcedence_table[stack_top][input_string[i]]=='<' or prcedence_table[stack_top][input_string[i]]=='='):
					stack.append(input_string[i])
					# print("input_string value",input_string[i])
					i+=1
					# print("stack_top inside equal or less",stack[-1])
				elif prcedence_table[stack_top][input_string[i]]=='>':
					while prcedence_table[stack_top][input_string[i]]=='>':
						# print("stack_top",stack_top)
						stack.pop()
						stack_top=stack[-1]
				else:
					print("Given input string can't be parsed\n")
					break;
			except:
				# print("INNNNNNNNNNNNNNNn")
				print("Given input string can't be parsed\n")
				break;

calculate_precedence_table()
input_string=input("Enter the string which you want to parse\n")
operator_parser(input_string)


	