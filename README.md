# Bare Except Block Masking Errors

This repository demonstrates a common yet subtle error in Python: using a bare `except` block without specifying the exception type. This can make debugging significantly harder as it masks the root cause of errors.

## The Problem

The `bug.py` file contains a function that uses a bare `except` block.  This catches *all* exceptions, making it difficult to identify and fix the specific issue.  This is a bad practice since it prevents specific error handling and makes debugging more difficult.

## The Solution

The `bugSolution.py` file shows the correct way to handle exceptions; by catching specific exception types or handling related exceptions with `except Exception as e:` but logging and re-raising the error.