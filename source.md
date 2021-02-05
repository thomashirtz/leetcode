# [leetcode](https://leetcode.com/problemset/all/)

Repository containing Python solutions to LeetCode problems. The focal point of this project is to try to provide solutions as minimalist and as clean as possible.

| # | Title | Solution | Difficulty |
|---| ----- | -------- | ---------- |
$PLACEHOLDER$

## Dataframe & Git Automation

The python file [[automation.py]](automation.py) provides a simple way to automatise the generation of 'row' and folder/files to update the repository. For example, if the ids is set to [2, 13], the script will generate the files if they do not exist yet, change the README.md using the source.md, and copy the commit message to the pastebin as follows:

Rows created in the README.md:
```
|2|[Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)|[Python](./solutions/2-add-two-numbers.py)|Medium|
|13|[Roman to Integer](https://leetcode.com/problems/roman-to-integer/)|[Python](./solutions/13-roman-to-integer.py)|Easy|
```

Commit information printed and copied into the clipboard (only the last item of the list):
```
Add 13-roman-to-integer
```

The automation file also generate a dataframe that summarize all the existing Leetcode questions:

![leetcode-dataframe](dataframe.png)
