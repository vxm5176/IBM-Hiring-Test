#We don't know how deeply nested any given
#unflattened JSON will be, so we must use recursion
def flatten_json(obj):
    ret = {} #Object with a single key
    #For each key we want to recurse its children, so we must introduce a nested function
    def flatten(x,flattened_key = ''): #x is an arbitrary object; key is initialzied in case we don't have one yet
        """Base Case: We are not at a list or an object
        so we will the current item to the return object"""
        if isinstance(x,dict):
            for current_key in x:
                flatten(x[current_key], flattened_key + current_key + '_') #Pass the nested JSON; with each call, append nested keys to original

        elif isinstance(x,list):#Append index of where we are in the list to the key
            i = 0
            for elem in x:
                flatten(elem, flattened_key + str(i) + '_') #End up back in our base case, where key has appended index
                i +=1

        #x == string, int, etc
        else:
            ret[flattened_key[:-1]] = x


    flatten(obj)
    return ret

if __name__ == "__main__":
    obj = unflat_json = {'user':
                   {'Rachel':
                        {'UserID': 1717171717,
                         'Email': 'rachel1999@gmail.com',
                         'friends': ['John', 'Jeremy', 'Emily']
                         }
                    }
               }
    print(flatten_json(obj))