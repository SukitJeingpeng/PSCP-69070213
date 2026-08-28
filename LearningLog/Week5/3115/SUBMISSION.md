# Problem Solving Submission

This file must be written by the student in their own words.

Use this template only for OJ problems that are marked as learning-log required.

Do not ask AI to write this file for you. AI may help check grammar, formatting, or clarity after you have written your own content.

If AI was used for this learning-log-required problem, also complete `ai_reflection.md`.

---

## 1. OJ Information

OJ problem number/title:

```text
3115 / Arcade of Time: Store Check
```

OJ submission ID, if submitted:

```text
632729
```

OJ status:

```text
Pass
```

Independent time spent on this problem:

```text
30-60 minutes
```

Choose one:

```text
0-15 minutes
15-30 minutes
30-60 minutes
1-3 hours
3-6 hours
6-24 hours
1-3 days
4-7 days
1-4 weeks
More than 4 weeks
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

```text
input : 
First input = Total Shop, Check time
second input to N-1 input = Start and Stop time for the each shop
the last input = Check time about how many shop is opened in that time
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
Step 1: get all the input (First input = Total Shop, Check time second input to N-1 input = Start and Stop time for the each shop the last input = Check time about how many shop is opened in that time)
Step 2: make a list to store start and stop value for each store (use loop to store each shop start and stop time)
Step 3: I didn't know how to do it after step 2 so I asked my friends how to check every start time and stop time for each shop with each of checktime and send back the result into list
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

```text
Step 1: get all the input (First input = Total Shop, Check time second input to N-1 input = Start and Stop time for the each shop the last input = Check time about how many shop is opened in that time)
Step 2: make a list to store start and stop value for each store (use loop to store each shop start and stop time)
Step 3: make a result list to store the check query time if Start <= Time < Stop then Count += 1 and then add all count in to result list
Step 4: print result list without [ ] and use space instead of ","

I didn't know how to do it after step 2 so I asked AI how to check every start time and stop time for each shop with each of checktime
```

---

## 5. My Tests

Write at least 3 test cases that you tried or designed by yourself.

Try to choose test cases that are different from each other.

For each test case, explain why you chose it.

If the input or output has many lines, write them inside the text blocks.

### Test Case 1

Why I chose this case:

```text
The normal one
```

Input:

```text
3 3
100 500
300 700
400 600
250 450 650
```

Expected output:

```text
1 3 1
```

Actual output:

```text
1 3 1
```

Result:

```text
Pass
```

### Test Case 2

Why I chose this case:

```text
2 4
0 100
1000 1200
50 500 900 1300
```

Input:

```text
if there is only first shop in time range
```

Expected output:

```text
1 0 0 0
```

Actual output:

```text
1 0 0 0
```

Result:

```text
Pass
```

### Test Case 3

Why I chose this case:

```text
if the check time is most of the time that all the shop opened
```

Input:

```text
4 2
100 800
200 900
300 1000
500 600
400 550
```

Expected output:

```text
3 4
```

Actual output:

```text
3 4
```

Result:

```text
Pass
```

---

## 6. AI Use

Did you use AI for this problem?

```text
No
```

If yes, also complete:

```text
ai_reflection.md
```

If you only asked a friend, TA, or instructor and did not use AI, you do not need to complete `ai_reflection.md`.

---

## 7. Human Help / Collaboration

Did you ask a friend, TA, instructor, or another person for help on this problem?

```text
Yes
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

```text
My friends
```

What did they help with?

```text
I didn't know how to do it after step 2 so I asked AI how to check every start time and stop time for each shop with each of checktime
```

What did you still do by yourself?

```text
I know how the code work but I just cant think about it at that moment and when they guide me I founded it that I can just use loop to get every index character in query list and check the start and stop time for each shop and then if it check and it go right then add count with 1 then append into result list
```

Did you copy any code from another person?

```text
No
```

---

## 8. Student Declaration

Write `Yes` for each statement.

| Statement | Yes/No |
|---|---|
| I wrote this submission in my own words. | Yes |
| I understand my final code. | Yes |
| I recorded the real OJ status. | Yes |
| I did not copy AI-generated text directly into this file. | Yes |
| I did not copy code from another person. | Yes |
| If I received human help, I disclosed it in this file. | Yes |
| I submitted the final code to the OJ by myself. | Yes |
