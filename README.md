# Password Strength Tester
![Tests](https://github.com/MichaelTM0/password-strength-tester/actions/workflows/test.yml/badge.svg)


A command-line Python tool that checks a password against a set of strength requirements, the same kind of check you see when creating an account on a website. It shows a pass/fail checklist for each rule and keeps prompting until the password meets all of them.

## ⚠️ Disclaimer — Educational Use Only

This project was built for **learning purposes** as part of my journey studying
Python and cybersecurity fundamentals. It runs entirely **locally** on a password
the user enters themselves, and it does **not** target, access, or attempt to
compromise any real account, system, or network.

It is intended to demonstrate core programming concepts (loops, `itertools`,
input validation, efficiency) and to illustrate *why* password length and
complexity matter. Please do not use it for anything other than education on
systems you own.

## Features

- Checks a password against five requirements:
  - At least 8 characters
  - At least 1 uppercase letter
  - At least 1 lowercase letter
  - At least 1 number
  - At least 2 special characters
- Displays a ✓ / ✗ checklist so you can see exactly which rules passed
- Keeps asking until the password is strong, then confirms it was accepted

## Requirements

- Python 3.6 or newer
- No external packages; it uses only the standard library
  ## Run with Docker

```bash
docker build -t password-tester .
docker run -it password-tester
```

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/MichaelTM0/password-strength-tester.git
   cd password-strength-tester
   ```

2. Run the program:

   ```bash
   python pwordstrengthtester.py
   ```

3. Enter a password when prompted. The checklist shows what passed and what didn't.

## Example

```
Your password must have:
  - at least 8 characters
  - at least 1 uppercase letter
  - at least 1 lowercase letter
  - at least 1 number
  - at least 2 special characters

Please enter your new password: Abcdef1!

Password Requirements
✓ at least 8 characters
✓ at least 1 uppercase letter
✓ at least 1 lowercase letter
✓ at least 1 number
✗ at least 2 special characters

Password unacceptable. Please try again.

Please enter your new password: Str0ng!!

Password Requirements
✓ at least 8 characters
✓ at least 1 uppercase letter
✓ at least 1 lowercase letter
✓ at least 1 number
✓ at least 2 special characters

Password is strong! Password created successfully!
```

## How It Works

- `analyze_password()` walks through the password once, works out which rules pass, and returns the results as a dictionary: each requirement is a key, and its pass/fail (True/False) is the value.
- `show_results()` loops over that dictionary and prints each requirement with a ✓ or ✗.
- `main()` uses `all(results.values())` to decide whether every rule passed, and loops until one does.

Returning a single dictionary (instead of several separate values) keeps the data easy to pass between functions, and adding a new requirement only means adding one line to the dictionary.

## Notes

- Spaces currently count as special characters, since any non-letter, non-digit character qualifies. A future version could define an explicit set of allowed symbols.
- This is a demonstration tool. Don't enter a real password you use anywhere.

## Future Improvements

- Define an explicit set of allowed special characters (and decide whether spaces count)
- Give a strength score or rating instead of just pass/fail
- Check against a list of common passwords
- Mask the password as it's typed

## What I Learned

- Returning a dictionary from a function instead of several loose values
- Looping a dictionary with `.items()` to get keys and values together
- Using `all()` to check that every condition passed
- That comparisons like `len(password) >= 8` are already True/False on their own
- Why defining a function isn't the same as calling it (`main()` has to be called)

## Author

**Michael Murchie**

- GitHub: [@MichaelTM0](https://github.com/MichaelTM0)
- LinkedIn: [michael-murchie](https://www.linkedin.com/in/michael-murchie/)
