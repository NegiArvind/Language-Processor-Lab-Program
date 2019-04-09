#include<bits/stdc++.h>
using namespace std;
int main()
{
	string s;
	int i,acount,bcount,k=0;
	cout<<"Enter the string whose tokens you want to find\n";
	cin>>s;
	string lex[100];
	for(i=0;i<s.size();i++)
	{
		if(s[i]=='a')
		{
			if(bcount!=0)
			{
				if(bcount==2 && acount==1)
				{
					lex[k++]="abb";
					// bcount=0;
				}
				else if(bcount==1 && acount==0)
				{
					lex[k++]="b";
					bcount=0;
				}
				else    
				{
					// cout<<"Value of i a "<<i;
					lex[k++]="a*b+";
					// bcount=0;
				}
			}
			if(acount!=0 && bcount!=0)
			{
				acount=0;
				bcount=0;
			}
			if(i==s.size()-1)
			{
				lex[k++]="a";
			}
			acount++;
			// cout<<"acount=="<<acount<<"\n";
		}
		else if(s[i]=='b')
		{
			bcount++;
			// cout<<"bcount=="<<bcount<<"\n";
			// if(acount==0)
			// {
			// 	{
			// 		lex[k++]="a*b+";
			// 		bcount=0;
			// 	}
			// }
			if(i==s.size()-1)
			{
				if(bcount==2)
				{
					lex[k++]="abb";
				}
				else if(bcount==1)
				{
					lex[k++]="b";
				}
				else
				{
					// cout<<"Value of i b "<<i;
					lex[k++]="a*b+";
				}
			}
		}
	}
    cout<<"Tokens are\n";
	for(i=0;i<k;i++)
	{
		cout<<lex[i]<<"  ";
	}
	cout<<"\n";
}