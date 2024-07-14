#prodigy task-3
#password complexity checker

import re
def check_password_strength(password):
    score = 0
    feedback = []

    #Criteria check
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'[0-9]', password))
    specialchar_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    #update score
    if length_criteria:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters")
    
    if uppercase_criteria:
        score += 1
    else:
        feedback.append("Password should include at least one capital letter")

    if lowercase_criteria:
        score += 1
    else:
        feedback.append("Password should include at least one small letter")

    if number_criteria:
        score += 1
    else:
        feedback.append("Password should include at least one number")

    if specialchar_criteria:
        score += 1
    else:
        feedback.append("Password should include at least one special character")

    
    #Access overall strength score
    if score == 5:
        password_strength = "Very strong"
    elif score == 4:
        password_strength = "Strong"
    elif score == 3:
        password_strength = "Medium"
    elif score == 2:
        password_strength = "Weak"
    else:
        password_strength = "Very weak"

    #Provide feedback
    if not feedback:
        feedback.append("Your password is Strong")

    return password_strength, feedback

#User input
password = input("Enter your password to check its strength: ")
password_strength, feedback  = check_password_strength(password)

print(f"Password Strength: {password_strength}")
print("feedback")
for comment in feedback:
    print(f" - {comment}")
