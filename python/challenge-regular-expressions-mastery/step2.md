# Email Obfuscation

## Problem Statement

In this sub-challenge, you will create a Python function to obfuscate email addresses in a given text. The purpose of this function is to prevent email addresses from being easily harvested by spambots while still being readable by humans.

## Requirements

1. Complete the `obfuscate_emails` function in `email_obfuscation.py`, which takes a string as input and returns a new string with email addresses obfuscated.
2. Use `regex` to identify email addresses in the input string.
3. Replace the `@` symbol with `[at]` and the `.` symbol with `[dot]` in the email addresses.
4. Ensure that the function works with various email formats and edge cases.
5. Test the function with a sample text containing multiple email addresses.

## Example

If you complete the `obfuscate_emails` function, open the terminal and input:

```shell
python email_obfuscation.py
```

Output:

```python
"You can reach me at john [dot] doe [at] gmail [dot] com or johndoe [at] mycompany [dot] com."
```
