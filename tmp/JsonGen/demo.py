import random
import string
import re
from typing import Union, List, Any
from faker import Faker
import exrex

fake = Faker()

def gen_data(nameItem: str, type: str, pattern: Union[str, int] = None, max_val: int = None, min_val: int = None, default: Any = None, listValue: List[Any] = None):
    if listValue:
        return listValue
    
    skipLimit = False;
    limitLength = 0
    skipMin = False;
    skipMax = False;
    results = []
    mpRst = {}

    if type == 'string':
        if min_val is not None:
            if max_val is None:
                limitLength = min_val + 1
        if max_val is not None:
            if min_val is None:
                limitLength = max_val - 1
        if max_val is not None and min_val is not None:
                limitLength = random.randint(min_val, max_val)
        if default is not None:
            if min_val is not None and len(default) == min_val:
                print("First condition met")
                results.append(default)
                skipMin = True
            elif max_val is not None and len(default) == max_val:
                print("Second condition met")
                results.append(default)
                skipMax = True
            elif max_val is not None and len(default) < max_val:
                if min_val is None:
                    print("Third condition met")
                    results.append(default)
                    skipLimit = True
                elif min_val is not None and len(default) > min_val:
                    results.append(default)
                    skipLimit = True
            elif min_val is not None and len(default) > min_val:
                if max_val is None:
                    results.append(default)
                    skipLimit = True
                elif max_val is not None and len(default) < max_val:
                    results.append(default)
                    skipLimit = True    
        
        if pattern == 'int':
            if min_val is not None and not skipMin:
                results.append(''.join(random.choices(string.digits, k=min_val)))
            if max_val is not None and not skipMax:
                results.append(''.join(random.choices(string.digits, k=max_val)))
            if not skipLimit and limitLength > 0:
                results.append(''.join(random.choices(string.digits, k=limitLength)))
        elif pattern == '':
            if min_val is not None and not skipMin:
                results.append(''.join(random.choices(string.ascii_letters, k=min_val)))
            if max_val is not None and not skipMax:
                results.append(''.join(random.choices(string.ascii_letters, k=max_val)))
            if not skipLimit and limitLength > 0:
                results.append(''.join(random.choices(string.ascii_letters, k=limitLength)))
        else:
            if min_val is not None and not skipMin:
                while True:
                    gen_str =  exrex.getone(pattern, limit=min_val)
                    if len(gen_str) >= min_val:
                        results.append(gen_str[0:min_val]);
                        break;
            if max_val is not None and not skipMax:
                while True:
                    gen_str =  exrex.getone(pattern, limit=max_val) 
                    if len(gen_str) >= max_val:
                        results.append(gen_str[0:max_val]); 
                        break;
            if not skipLimit and limitLength > 0:
                while True:
                    gen_str =  exrex.getone(pattern)
                    if len(gen_str) >= limitLength:
                        results.append(gen_str[0:limitLength]); 
                        break;
    
    elif type == 'int':
        if min_val is not None:
                results.append(min_val)
        if max_val is not None:
            results.append(max_val)
        if default is not None:
            if min_val is not None:
                if max_val is None and default > min_val:
                    results.append(default)
                elif max_val is not None and default > min_val and default < max_val:
                    results.append(default)
            else:
                if max_val is None:
                    results.append(default)
                elif max_val is not None and default < max_val:
                    results.append(default)
        else:
            if min_val is not None and max_val is not None:
                results.append(random.randint(min_val + 1, max_val -1))
            elif min_val is  None and max_val is not None:
                results.append(random.randint(0, max_val -1))
            elif min_val is not None and max_val is None:
                results.append(random.randint(min_val, min_val + 1000))
            elif min_val is None and max_val is None:
                results.append("123456")
    
    elif type == 'boolean':
        results.append(True)
        results.append(False)
    
    elif type == 'array':
        # Assuming array elements are of type int for simplicity
        if min_val is not None:
            results.append([gen_data(nameItem, 'int', None, max_val, min_val)[0] for _ in range(min_val)])
        if max_val is not None:
            results.append([gen_data(nameItem, 'int', None, max_val, min_val)[0] for _ in range(max_val)])
        if min_val is not None and max_val is not None:
            results.append([gen_data(nameItem, 'int', None, max_val, min_val)[0] for _ in range(random.randint(min_val, max_val))])
    
    elif type == 'object':
        # Assuming a simple object with random key-value pairs for simplicity
        results.append({fake.word(): gen_data(nameItem, 'string')[0] for _ in range(random.randint(1, 5))})
    mpRst[nameItem] = results
    return mpRst

# Example usage:
print(gen_data("usernam", "string", pattern="^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-]+)(\-[a-zA-Z]{2,5}){1,2}$", max_val=50, default="abc@gmail.com"))
print(gen_data("age", "int", max_val=50, min_val=10, default=12))
print(gen_data("sex", "boolean"))
