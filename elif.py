#test grading program



test_score = int(input("Please enter your test score: "))
if test_score >= 80:
    print("A grade")
elif test_score >= 70:
    print("B grade")
elif test_score >= 60:
    print("C grade")
elif test_score >= 50:
    print("D grade")
elif test_score >= 40:
    print("E grade")
else:
    print("Fail")
