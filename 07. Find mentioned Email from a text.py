def email_func(str):
    if('@' in str):
        position = str.find('@')
        position2 = str.find(' ',position)
        position3 = str.rfind(' ',-len(str), (position-len(str)))
        return str[position3+1:position2]
    else:
        return False
        

email_func("Crazy Frog")
email_func("this is first akash@cloudxlab.com and this is second sandeep@cloudxlab.com")
