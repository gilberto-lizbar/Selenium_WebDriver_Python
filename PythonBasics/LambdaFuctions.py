def sum1(a, b):
    return a + b


print(sum1(12, 43))

# I dont want to use function multiple times, i just need to use once
# in that function there is a single line of code
# lambda function for this purpose: lambda keyword
# lambda a,b,c,d: a + b + c +d

# Lambda functions are small, anonymous (nameless),
# single-expression functions defined using the lambda keyword
sum2 = lambda a, b: a + b
print(sum2(14, 34))
