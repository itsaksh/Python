def process_marks(marks):
    
    passed = [mark for mark in marks if mark >= 40]
   
    processed = sorted(set(passed))
    
    qualified = [mark for mark in processed if mark >= 60]
    top_three = sorted(qualified, reverse=True)[:3]
    return processed, qualified, top_three
 
 
marks = [35, 60, 45, 80, 35, 55, 60, 95, 40, 80]
processed, qualified, top_three = process_marks(marks)
print("Original marks :", marks)          
print("Processed marks:", processed)
print("Qualified marks:", qualified)
print("Top three      :", top_three)
 
print("\n--- Edge cases ---")
for test in ([35, 30, 60, 20, 10, 45], [39, 40, 59, 60, 60], [10, 20, 30]):
    print(test, "->", process_marks(test))

