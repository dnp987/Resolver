def check_parameters(desc, expected, actual):
    expected = expected.strip() #remove all leading and trailing spaces
    actual = actual.strip()
    
    if (expected == actual):
        print ('Checking',desc,actual,'found as expected')
    else:
        print ('Checking',desc,expected,'expected',actual,'found')
  