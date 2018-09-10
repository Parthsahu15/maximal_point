from array import *
import math

def main():
	n = int(input("Enter the number of points"))

	arr =[]

	for i in range (0,n):
		arr.append([])
		for j in range (0,2):
			arr[i].append(int(input("Enter the point")))


	array = sorted(arr,key=lambda l: l[0])
	res1 = maximal(array)

	return

def split_list(a_list):
    l = len(a_list)/2
    half = math.ceil(l);
    return a_list[:half], a_list[half:]



def maximal(array):
	if (len(array)<=1):
		return array

	#ar = array
	m1, m2 = split_list(array);
	
	max1 = maximal(m1)
	max2 = maximal(m2)


	l=len(max1)
	
	count1=0
	count2=0
	i=0
	
	for j in range(0,l):
		
		if((int(max1[i][0])<=int(max2[0][0])) and (int(max1[i][1])<=int(max2[0][1]))):
			max1.pop(i)
			count1+=1

		if(count2==count1):
			i+=1
		else:
			count2=count1;
	
	ll=len(max1)		
	
	if (ll==0):
		return max2
	else:
		return max1+max2


main()