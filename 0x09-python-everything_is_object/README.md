0x09. Python - Everything is object

Background Context
Now that we understand that everything is an object and have a little bit of knowledge, let’s pause and look a little bit closer at how Python works with different types of objects.

BTW, have you ever modified a variable without knowing it or wanting to? I mean:

>>> a = 1
>>> b = a
>>> a = 2
>>> b
1
>>> 
OK. But what about this?

>>> l = [1, 2, 3]
>>> m = l
>>> l[0] = 'x'
>>> m
['x', 2, 3]
>>> 

Tasks
0. Who am I?
What function would you use to get the type of an object?

Write the name of the function in the file, without ().

1. Where are you?
How do you get the variable identifier (which is the memory address in the CPython implementation)?

Write the name of the function in the file, without ().

2. Right count
In the following code, do a and b point to the same object? Answer with Yes or No.

3. Right count =
In the following code, do a and b point to the same object? Answer with Yes or No.

4. Right count =
In the following code, do a and b point to the same object? Answer with Yes or No.

5. Right count =+
In the following code, do a and b point to the same object? Answer with Yes or No.

6. Is equal
What do these 3 lines print?

7. Is the same
What do these 3 lines print?

8. Is really equal
What do these 3 lines print?

9. Is really the same
What do these 3 lines print?

10. And with a list, is it equal
What do these 3 lines print?

11. And with a list, is it the same
What do these 3 lines print?

12. And with a list, is it really equal
What do these 3 lines print?

13. And with a list, is it really the same
What do these 3 lines print?

14. List append
What does this script print?

15. List add
What does this script print?

16. Integer incrementation
What does this script print?

17. List incrementation
What does this script print?

18. List assignation
What does this script print?

19. Copy a list object
Write a function def copy_list(l): that returns a copy of a list.

The input list can contain any type of objects
Your file should be maximum 3-line long (no documentation needed)
You are not allowed to import any module

20. Tuple or not?
a = ()
Is a a tuple? Answer with Yes or No.

21. Tuple or not?
a = (1, 2)
Is a a tuple? Answer with Yes or No.

22. Tuple or not?
a = (1)
Is a a tuple? Answer with Yes or No.

23. Tuple or not?
a = (1, )
Is a a tuple? Answer with Yes or No.

24. Who I am?
What does this script print?

a = (1)
b = (1)
a is b

25. Tuple or not
What does this script print?

a = (1, 2)
b = (1, 2)
a is b

26. Empty is not empty
What does this script print?

a = ()
b = ()
a is b

27. Still the same?
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
Will the last line of this script print 139926795932424? Answer with Yes or No.

28. Same or not?
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
Will the last line of this script print 139926795932424? Answer with Yes or No.

Advanced Tasks.

