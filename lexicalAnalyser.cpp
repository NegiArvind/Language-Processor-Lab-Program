#include<bits/stdc++.h>
using namespace std;
string removeBlankSpacesAndNewLines(string str)
{
	string newStr;
	int i=0,j=0,k;
	for(i=1;i<str.size();i++)
	{
		if((str[i]==' '&&str[i-1]==' ')||str[i]=='\n')
		{
			continue;
		}
		else
			newStr+=str[i];
	}
	return newStr;
}

bool isOperator(char ch) 
{ 
    if (ch == '+' || ch == '-' || ch == '*' ||  
        ch == '/' || ch == '>' || ch == '<' ||  
        ch == '=') 
        return (true); 
    return (false); 
} 

bool isDelimiter(char ch) 
{ 
    if (ch == ' ' || ch == '+' || ch == '-' || ch == '*' ||  
        ch == '/' || ch == ',' || ch == ';' || ch == '>' ||
        ch == '<' || ch == '=' || ch == '(' || ch == ')' ||
        ch == '[' || ch == ']' || ch == '{' || ch == '}' || ch==';') 
        return (true); 
    return (false); 
} 

bool isKeyword(string str) 
{ 
    if (str== "if" || str== "else" || str== "while" || str== "do"||  str== "break" ||  str== "continue" || str== "int"
        || str== "double" || str== "float" 
        || str== "return" || str== "char" 
        || str== "case" || str== "char"
        || str== "sizeof" || str== "long"
        || str== "short" || str== "typedef"
        || str== "switch" || str== "unsigned" 
        || str== "void" || str== "static" 
        || str== "struct" || str== "goto") 
        return (true); 
    return (false); 
} 

bool isValidIdentifier(string str) 
{ 
    if (str[0] == '0' || str[0] == '1' || str[0] == '2' || str[0] == '3' || str[0] == '4' || str[0] == '5' ||  
        str[0] == '6' || str[0] == '7' || str[0] == '8' ||  str[0] == '9' || isDelimiter(str[0]) == true) 
        return (false); 
    return (true); 
} 

int main()
{
	ifstream inputFile("floyd.cpp");
	char c;
	string symbTable[5000][2];
	string str,newStr;
	while(inputFile.get(c)){
		str+=c;
	}
	cout<<str;
	newStr=removeBlankSpacesAndNewLines(str);
	cout<<newStr;
	int k=0;
	string temp;
	for(int i=0;i<newStr.size();i++)
	{
		for(int j=0;j<newStr.size();j++)
		{
			if(isDelimiter(newStr[j]))
			{
				// cout<<"temp "<<temp<<"\n";
				cout<<"newSTr "<<newStr[j]<<"\n";
				if(isOperator(newStr[j])){
					symbTable[k++][0]=newStr[j];
					symbTable[k++][1]="Operator";
					cout<<"hello\n";
				}
				else if(newStr[j]!=' '){
					symbTable[k++][0]=newStr[j];
					symbTable[k++][1]="Delimeter";
				}
				if(temp.size()>0){
					cout<<"Pagal="<<temp;
					symbTable[k++][0]=temp;
					if(isKeyword(temp))
					{
						// symbTable[k++][0]=temp;
						symbTable[k++][1]="Keyword";
					}else if(isValidIdentifier(temp)){
						// symbTable[k++][0]=temp;
						symbTable[k++][1]="identifier";
					}else{
						symbTable[k++][1]="Wrong";
					}
					temp="";
				}
			}
			else{
				temp+=newStr[j];
				cout<<"temp====="<<temp<<"\n";
				i++;
			} 
		}
	}
	for(int i=0;i<k;i++)
	{
		cout<<symbTable[i][0]<<"  "<<symbTable[i][1]<<"\n";
	}
}