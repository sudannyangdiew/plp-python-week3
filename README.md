# PLP Python Week 3: Conditions and Loops Assignment

## Overview of Files

* `grade\_reporter.py` - Processes a list of student test scores using a `for` loop, calculates letter grades using `if/elif/else`, and outputs total passes, fails, and the rounded average score.

* `bug\_hunt.py` - A debugged Python script that uses a `while` loop to sum numbers from 1 to 5, featuring explanations for syntax, logic, and type errors.

## Bug Hunt Reflection

The hardest bug to find was the off-by-one logic error in the condition `while count < 5`. Because Python executed the program without raising any error messages or warnings, everything appeared fine at first glance. However, I knew something was wrong because the printed total was `10` instead of the expected `15`, revealing that the loop stopped early and omitted `5` from the total sum.
