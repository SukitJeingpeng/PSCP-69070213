# Problem Solving Submission

This file must be written by the student in their own words.

Use this template only for OJ problems that are marked as learning-log required.

Do not ask AI to write this file for you. AI may help check grammar, formatting, or clarity after you have written your own content.

If AI was used for this learning-log-required problem, also complete `ai_reflection.md`.

---

## 1. OJ Information

OJ problem number/title:

```
2996สลับตัวอักษร
```

OJ submission ID, if submitted:

```
541380
```

OJ status:

```
Pass
```

Independent time spent on this problem:

```
01-15 minutes
```

How to count this time:

- Count only the time you actively worked on this problem independently.
- Start counting from when you first read the problem.
- Do not include breaks, meals, classes, sleep, time spent on other problems, or time when you were not working on this problem.
- If you used AI, count only the independent time before your first AI prompt.
- If you asked a friend, TA, or instructor for help, count only the independent time before your first help request.
- If you used both AI and human help, count only the independent time before the first outside help of any kind.
- If you did not use AI or human help, count the time before writing this `submission.md`.
- An estimate is acceptable, but it must be honest.

---

## 2. My Understanding

Write the problem in your own words.

Also explain the input, output, and important constraints.

If you do not fully understand the problem yet, write what you currently understand. Your understanding may be incomplete or incorrect, but you must make a genuine attempt.

```
This Question is asked to solve an inverse letter in words so my input have WORD and my output is printing WORD backward
```

---

## 3. My First Plan

Write your first plan before getting help from AI, a friend, a TA, an instructor, or before finalizing your code.

If you used AI, write the plan you had before your first AI prompt.

If you asked a friend, TA, or instructor for help, write the plan you had before asking for help.

If you did not use AI or human help, write the plan you had before or while you started coding.

This can be rough. It may be incomplete or different from your final solution.

You may write pseudocode, a flowchart idea, or step-by-step thinking.

```text
Step 1: My first step is to make my input become lower case so i use input().lower()
Step 2: My second step is make "WORD" print backward so i do print(f"{WORD[4]}{WORD[3]}{WORD[2]}{WORD[1]}{WORD[0]}") there is other way to do it but I like it this way.
Step 3: Check if the result is correct or not.
```

---

## 4. My Final Approach

Briefly explain the final algorithm or method you actually used in your submitted code.

This section is different from Section 3:

- Section 3 is your first plan before AI, human help, or before the final code.
- Section 4 is the final method used in your actual solution.
- If your final approach is the same as your first plan, write that it is the same and briefly explain why.

Do not copy AI's explanation.

Do not copy another person's explanation.

```
It came out as I expected. It should be correct because the input is always 5Letters and My code is can only use with 5letters in word or else it will make index out of range or make the word not fully backward.
```

---

## 5. My Tests

Write at least 3 test cases that you tried or designed by yourself.

Try to choose test cases that are different from each other.

For each test case, explain why you chose it.

If the input or output has many lines, write them inside the text blocks.

### Test Case 1

Why I chose this case:

```
I used this one as my test case because it show every upper case is made lower. and it really write it

```

Input:

```
TESTT
```

Expected output:

```
ttest
```

Actual output:

```
ttest
```

Result:

```
Pass
```

### Test Case 2

Why I chose this case:

```I chose this test case because the letters in this word is more than 5 and I think it musk broke my code

```

Input:

```
HEllOWoRLd
```

Expected output:

```
It must be broke
```

Actual output:

```
olleh
```

Result:

```
Not Pass
```

### Test Case 3

Why I chose this case:

```
I choose this case to check if the letter in word is lesser than 5 will it break my code.
```

Input:

```
Lets
```

Expected output:

```
The code must be broke.
```

Actual output:

```
Error index out of range
```

Result:

```
Not Pass
```

---

## 6. AI Use

Did you use AI for this problem?

```
No
```

If yes, also complete:

If you only asked a friend, TA, or instructor and did not use AI, you do not need to complete `ai_reflection.md`.

---

## 7. Human Help / Collaboration

Did you ask a friend, TA, instructor, or another person for help on this problem?

```
No
```

If yes, briefly explain what kind of help you received.

Allowed examples:

- explanation of the problem statement
- explanation of a programming concept
- hint about the approach
- debugging discussion
- test-case discussion
- help understanding an error message

Not allowed:

- copying another person's code
- submitting another person's solution
- asking another person to write the solution for you
- using another person's OJ submission
- asking another person to submit to the OJ for you

Who helped you?

```
-

```

What did they help with?

```
-
```

What did you still do by yourself?

```
-
```

Did you copy any code from another person?

```
-
```

---

## 8. Student Declaration

Write `Yes` for each statement.

| Statement | Yes/No |
|---|---|
| I wrote this submission in my own words. |YES|
| I understand my final code. |YES|
| I recorded the real OJ status. |YES|
| I did not copy AI-generated text directly into this file. |YES|
| I did not copy code from another person. |YES|
| If I received human help, I disclosed it in this file. |YES|
| I submitted the final code to the OJ by myself. |YES|
