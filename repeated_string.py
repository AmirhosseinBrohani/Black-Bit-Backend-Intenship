def repeatedString(s, n):
    # Write your code here
    
    a_count = s.count('a')
    final_itter = int(n / len(s)) * a_count
    x = n % len(s)
    a = s.count('a',0 ,x)
    final_itter += a
    return final_itter 