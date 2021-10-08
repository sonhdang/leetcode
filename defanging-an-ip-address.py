# https://leetcode.com/problems/defanging-an-ip-address/

def defangIPaddr(address):
    result = ''
    for i in range(len(address)):
        if address[i] == '.':
            result += '[.]'
        else:
            result += address[i]
    return result