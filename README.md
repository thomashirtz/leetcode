# [leetcode](https://leetcode.com/problemset/all/)


| # | Title | Solution | Difficulty |
|---| ----- | -------- | ---------- |
|7|[Reverse Integer](https://leetcode.com/problems/reverse-integer/)|[Python](0000-0100/7-reverse-integer.py)|Easy|
|13|[Roman to Integer](https://leetcode.com/problems/roman-to-integer/)| [Python](0000-0100/13-roman-to-integer.py)|Easy|
|279|[Perfect Squares](https://leetcode.com/problems/perfect-squares/)| [Python](0200-0300/279-perfect-squares.py)|Medium|
|347|[Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)| [Python](0300-0400/347-top-k-frequent-elements.py)|Medium|
|628|[Maximum Product of Three Numbers](https://leetcode.com/problems/maximum-product-of-three-numbers/)|[Python](0600-0700/628-maximum-product-of-three-numbers.py)|Easy|
|872|[Leaf-Similar Trees](https://leetcode.com/problems/leaf-similar-trees/)|[Python](0800-0900/872-leaf-similar-trees.py)|Easy|
|957|[Prison Cells After N Days](https://leetcode.com/problems/prison-cells-after-n-days/)|[Python](0900-1000/957-prison-cells-after-n-days.py)|Medium|
|1304|[Find N Unique Integers Sum up to Zero](https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/)| [Python](1300-1400/1304-find-n-unique-integers-sum-up-to-zero.py)|Easy|


## Dataframe & Git Automation

The python file [[automation.py]](automation.py) provides a simple way to automatise the generation of 'row' and folder/files to update the repository. For example, if the ids is set to [2, 13], the script will generate the files, the missing folders and output:

```
|2|[Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)|[Python](./0000-0100/2-add-two-numbers.py)|Medium|
|13|[Roman to Integer](https://leetcode.com/problems/roman-to-integer/)|[Python](./0000-0100/13-roman-to-integer.py)|Easy|
```

The automation file also generate a dataframe that summarize all the existing Leetcode questions:

![leetcode-dataframe](pictures/dataframe.png)
