# [leetcode](https://leetcode.com/problemset/all/)

Repository containing Python solutions to LeetCode problems. The focal point of this project is to try to provide solutions as minimalist and as clean as possible. 

| # | Title | Solution | Difficulty |
|---| ----- | -------- | ---------- |
|1|[Two Sum](https://leetcode.com/problems/two-sum/)|[Python](solutions/1-two-sum.py)|Easy|
|2|[Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)|[Python](solutions/2-add-two-numbers.py)|Medium|
|7|[Reverse Integer](https://leetcode.com/problems/reverse-integer/)|[Python](solutions/7-reverse-integer.py)|Easy|
|8|[String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/)|[Python](solutions/8-string-to-integer-atoi.py)|Medium|
|9|[Palindrome Number](https://leetcode.com/problems/palindrome-number/)|[Python](solutions/9-palindrome-number.py)|Easy|
|13|[Roman to Integer](https://leetcode.com/problems/roman-to-integer/)|[Python](solutions/13-roman-to-integer.py)|Easy|
|14|[Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)|[Python](solutions/14-longest-common-prefix.py)|Easy|
|36|[Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)|[Python](solutions/36-valid-sudoku.py)|Medium|
|179|[Largest Number](https://leetcode.com/problems/largest-number/)|[Python](solutions/179-largest-number.py)|Medium|
|189|[Rotate Array](https://leetcode.com/problems/rotate-array/)|[Python](solutions/189-rotate-array.py)|Medium|
|279|[Perfect Squares](https://leetcode.com/problems/perfect-squares/)|[Python](solutions/279-perfect-squares.py)|Medium|
|347|[Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)|[Python](solutions/347-top-k-frequent-elements.py)|Medium|
|478|[Generate Random Point in a Circle](https://leetcode.com/problems/generate-random-point-in-a-circle/)|[Python](solutions/478-generate-random-point-in-a-circle.py)|Medium|
|509|[Fibonacci Number](https://leetcode.com/problems/fibonacci-number/)|[Python](solutions/509-fibonacci-number.py)|Easy|
|628|[Maximum Product of Three Numbers](https://leetcode.com/problems/maximum-product-of-three-numbers/)|[Python](solutions/628-maximum-product-of-three-numbers.py)|Easy|
|709|[To Lower Case](https://leetcode.com/problems/to-lower-case/)|[Python](solutions/709-to-lower-case.py)|Easy|
|872|[Leaf-Similar Trees](https://leetcode.com/problems/leaf-similar-trees/)|[Python](solutions/872-leaf-similar-trees.py)|Easy|
|875|[Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/)|[Python](solutions/875-koko-eating-bananas.py)|Medium|
|941|[Valid Mountain Array](https://leetcode.com/problems/valid-mountain-array/)|[Python](solutions/941-valid-mountain-array.py)|Easy|
|944|[Delete Columns to Make Sorted](https://leetcode.com/problems/delete-columns-to-make-sorted/)|[Python](solutions/944-delete-columns-to-make-sorted.py)|Easy|
|957|[Prison Cells After N Days](https://leetcode.com/problems/prison-cells-after-n-days/)|[Python](solutions/957-prison-cells-after-n-days.py)|Medium|
|1115|[Print FooBar Alternately](https://leetcode.com/problems/print-foobar-alternately/)|[Python](solutions/1115-print-foobar-alternately.py)|Medium|
|1116|[Print Zero Even Odd](https://leetcode.com/problems/print-zero-even-odd/)|[Python](solutions/1116-print-zero-even-odd.py)|Medium|
|1195|[Fizz Buzz Multithreaded](https://leetcode.com/problems/fizz-buzz-multithreaded/)|[Python](solutions/1195-fizz-buzz-multithreaded.py)|Medium|
|1304|[Find N Unique Integers Sum up to Zero](https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/)|[Python](solutions/1304-find-n-unique-integers-sum-up-to-zero.py)|Easy|
|1309|[Decrypt String from Alphabet to Integer Mapping](https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/)|[Python](solutions/1309-decrypt-string-from-alphabet-to-integer-mapping.py)|Easy|
|1342|[Number of Steps to Reduce a Number to Zero](https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/)|[Python](solutions/1342-number-of-steps-to-reduce-a-number-to-zero.py)|Easy|
|1366|[Rank Teams by Votes](https://leetcode.com/problems/rank-teams-by-votes/)|[Python](solutions/1366-rank-teams-by-votes.py)|Medium|
|1394|[Find Lucky Integer in an Array](https://leetcode.com/problems/find-lucky-integer-in-an-array/)|[Python](solutions/1394-find-lucky-integer-in-an-array.py)|Easy|
|1447|[Simplified Fractions](https://leetcode.com/problems/simplified-fractions/)|[Python](solutions/1447-simplified-fractions.py)|Medium|
|1448|[Count Good Nodes in Binary Tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/)|[Python](solutions/1448-count-good-nodes-in-binary-tree.py)|Medium|
|1449|[Form Largest Integer With Digits That Add up to Target](https://leetcode.com/problems/form-largest-integer-with-digits-that-add-up-to-target/)|[Python](solutions/1449-form-largest-integer-with-digits-that-add-up-to-target.py)|Hard|
|1456|[Maximum Number of Vowels in a Substring of Given Length](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/)|[Python](solutions/1456-maximum-number-of-vowels-in-a-substring-of-given-length.py)|Medium|
|1528|[Shuffle String](https://leetcode.com/problems/shuffle-string/)|[Python](solutions/1528-shuffle-string.py)|Easy|

## Dataframe & Git Automation

The python file [[automation.py]](automation.py) provides a simple way to automatise the generation of 'row' and folder/files to update the repository. For example, if the ids is set to [2, 13], the script will generate the files, the missing folders and output:

```
|2|[Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)|[Python](./0000-0100/2-add-two-numbers.py)|Medium|
|13|[Roman to Integer](https://leetcode.com/problems/roman-to-integer/)|[Python](./0000-0100/13-roman-to-integer.py)|Easy|
```

The automation file also generate a dataframe that summarize all the existing Leetcode questions:

![leetcode-dataframe](pictures/dataframe.png)
