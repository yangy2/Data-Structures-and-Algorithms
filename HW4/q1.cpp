#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

using namespace std;

int main() {

	ifstream ifs("data1.txt", ifstream::in);
	string temp;
	double tmp;
	
	vector<double> v;
	
	while(getline(ifs, temp))
	{
		istringstream ss(temp);
		
		while(ss >> tmp)
		{
			v.push_back(tmp);
		}
	}
	for (int i = 2; i < 100; i++)
	{
		cout << v[i] << " ";
		if ((i-1) % 3 == 0 && i != 2) cout << endl;
	}
}

