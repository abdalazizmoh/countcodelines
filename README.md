# Count code lines C#
Implement a function that counts the Lines of Code (LOC) in a C# source text.

The source text is given as a string. The function returns the number of executable lines of code. Lines containing only comments or whitespace should be filtered **[1]**.

##### Please note:

- C# has no nested comments
- Comment characters –/*, */, //– don’t open/close comments inside of strings
- Strings inside comments are not recognized. That means, the comment /*a”*/”b… ends in front of “b.
- Executable code can be placed in the same line as a comment: in front of /* or // or after */.

##### Variation #1
Also return the number of lines that contain only comments or whitespace.

##### Endnotes
**[1]** Strings count as executable code. Even if they extend over multiple lines or contain whitespace lines.