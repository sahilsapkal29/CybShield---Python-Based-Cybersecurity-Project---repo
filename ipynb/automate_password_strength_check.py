import re
import os

# ---------------- PASSWORD CHECK ----------------

def password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Min 8 chars")

    if re.search("[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase")

    if re.search("[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase")

    if re.search("[0-9]", password):
        score += 1
    else:
        feedback.append("Add number")

    if re.search("[@#$%^&+=]", password):
        score += 1
    else:
        feedback.append("Add special char")

    if score == 5:
        return "Very Strong", feedback
    elif score >= 3:
        return "Moderate", feedback
    else:
        return "Weak", feedback


# ---------------- AUTOMATION ----------------
def automated_check(input_file, output_file):
    
    if not os.path.exists(input_file):
        print("Input file not found!")
        return

    with open(input_file, "r") as f:
        passwords = f.readlines()

    with open(output_file, "w") as report:
        report.write("PASSWORD SECURITY REPORT\n")
        report.write("="*40 + "\n")

        for pwd in passwords:
            pwd = pwd.strip()
            status, feedback = password_strength(pwd)

            report.write(f"\nPassword: {pwd}\n")
            report.write(f"Strength: {status}\n")

            if feedback:
                report.write("Suggestions: " + ", ".join(feedback) + "\n")

    print("Automation Complete! Report saved in", output_file)


# ---------------- MAIN ----------------
if __name__ == "__main__":
    automated_check("passwords.txt", "report.txt")
