CHECK = "\u2713"   # ✓
CROSS = "\u274c"   # ✗


def analyze_password(password):
    has_upper = False
    has_lower = False
    has_number = False
    special_count = 0

    for character in password:
        if character.islower():
            has_lower = True
        elif character.isupper():
            has_upper = True
        elif character.isdigit():
            has_number = True
        elif not character.isalnum():
            special_count += 1

    results = {
        "at least 8 characters": len(password) >= 8,
        "at least 1 uppercase letter": has_upper,
        "at least 1 lowercase letter": has_lower,
        "at least 1 number": has_number,
        "at least 2 special characters": special_count >= 2,
    }
    return results


def show_results(results):
    print("\nPassword Requirements")
    for requirement, passed in results.items():
        mark = CHECK if passed else CROSS
        print(f"{mark} {requirement}")


def main():
    print("\n" + "=" * 50)
    print("           PASSWORD STRENGTH TESTER")
    print("=" * 50)
    print("\nYour password must have:")
    print("  - at least 8 characters")
    print("  - at least 1 uppercase letter")
    print("  - at least 1 lowercase letter")
    print("  - at least 1 number")
    print("  - at least 2 special characters")

    while True:
        password = input("\nPlease enter your new password: ")
        results = analyze_password(password)
        show_results(results)

        if all(results.values()):
            print("\nPassword is strong! Password created successfully!")
            break
        else:
            print("\nPassword unacceptable. Please try again.")


if __name__ == "__main__":
    main()
