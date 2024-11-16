## Python Interview Preparation

#### sort() v sorted()

* **sort()**  
Modifies the original list: It directly alters the original list in-place.  
Returns None: It doesn't return a new sorted list.  
Syntax: my_list.sort()
  
* **sorted()**  
Creates a new sorted list: It returns a new sorted list without modifying the original list.  
Returns a new list: It returns the newly created sorted list.  
Syntax: new_list = sorted(my_list)  

#### Lists v Tuples v Arrays
* Lists are sequence of SAME TYPES (meant for) & MUTABLE  
* Tuples are sequence of DIFFERENT TYPES & IMMUTABLE  
* Lists in Tuples are mutable
* Arrays are sequence of SAME TYPES & size id define at the time of variable declaration

#### PEP 8 (Python Enhancement Proposal)
* user PYCODESTYLE to check whether your code follows PEP 8

#### Local v Global
* Local: define & accessed inside functions
* Global: define outside the function n can not be accessed inside function unless specify with keyword **global <var>**

#### .py v .pyc
* if .py is present but no .pyc then python creates .pyc and loads .pyc
* if .pyc is present but no .py then python loads .pyc
* if .py & .pyc NEWER presents then python loads .pyc
* if .py & .pyc presents but .py is NEWER then python removes .pyc & re-compile module and creates NEW .pyc and loads .pyc



