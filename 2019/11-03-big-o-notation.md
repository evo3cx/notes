reading material
- https://www.reddit.com/r/programming/comments/1f2ml3/what_does_olog_n_mean_exactly/
- 

Takeaway keys:
imagine we at classroom and too stupid to remeber bring a pen to school, so i need to find the pen.
* n is it amount of students on the class

- O(n2): i quest a student and ask them, "does you have the pen? no? does bob have the pen?" and so on, naming each student. if i dont get the answer from the first student, i move on to the next one. in the worst case i need to ask n^2 questions - questioning each student about each other student.
- O(n): i ask each student if the have the pen. If not, i move on the next one. In the worst case i need to ask n question
- O(log n): i divide the class in two, then ask: "Is it on the left side, or the right side of the classroom?" the i take that group and divide it into two and ask again, and so on. in the worst case i need to ask log n question.
- O(n log(n)): I ask each student "do you know of any student whose name is <= Jeff who has the pen?" etc. This will zoom down on zero or one students in O(log n) steps. If you do not get the pen, you move on to the second student and do the same. 

i try to make it simplier:
- O(n2) will ask question to every students about every other student about the pen
- O(n) i only ask one person with one question if they doesnt know i move to next student
- O(log n) i dont look like some idiot asking every student, so i will divide them become half and repeat until only one person on this group
 
