s1,s2,s3,s4,s5 = map(int,input("Enter the marks of five subjects with spaces one after another : ").split(" "))
total = s1 + s2 + s3 + s4 + s5
aggregate = total / 5;
percentage = total / 500 * 100
print("Aggregate marks : {}".format(aggregate))
print("Percentage marks : {}".format(percentage))
