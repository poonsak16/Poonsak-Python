"""
Personal Finance Calculator
Student: [Poonsak Rojanapong]
Date: [26/07/2025]
Purpose: Calculate monthly budget and savings
"""

#ขอข้อมูลจากผู้ใช้ในประเด็นรายได้ (income) และค่าใช้จ่าย (expense) ดังนี้
#รายได้ต่อเดือน
monthly_income = float(input("Enter your monthly income (THB) "))
#ค่าเช่า
rent_cost = float(input("Enter your Monthly rent / housing cost (THB) "))
#ค่ากิน
food_budget = float(input("Enter your food budget (THB) "))
#ค่าเดินทาง
transportation_cost = float(input("Enter your Monthly transportation expenses (THB) "))
#ค่าผักผ่อน
entertainment_budget = int(input("Enter your monthly entertainment budget (THB): "))
#เผื่อสำหรับฉุกเฉิน
emergency_fund_percent = int(input("Enter percentage to save for emergency (0 - 100): "))
#เงินลงทุน
investment_percent = int(input("Enter percentage to invest (0 - 100): "))

#คำนวณข้อมูลดังนี้
#ค่าใช้จ่ายคงที่
total_fixed_expenses = rent_cost + transportation_cost
#ค่าใช้จ่ายไม่คงที่
total_variable_expenses = food_budget + entertainment_budget
#ค่าใช้จ่ายทั้งหมด
total_expenses = total_fixed_expenses + total_variable_expenses
#รายได้คงเหลือ
remaining_income = monthly_income - total_expenses
#เงินฉุกเฉิน
emergency_fund_amount = monthly_income * (emergency_fund_percent / 100)
#เงินลงทุน
investment_amount = monthly_income * (investment_percent / 100)
#เงินเหลือสำหรับออม
available_for_savings = remaining_income - emergency_fund_amount - investment_amount
#สัดส่วนค่าใช้จ่ายต่อรายได้
expense_ratio = (total_expenses / monthly_income) * 100

#แสดงผลลัพธ์
print("\n=== MONTHLY BUDGET REPORT ===")
print(f"Income: {monthly_income:.2f} THB")
print(f"Fixed Expenses: {total_fixed_expenses:.2f} THB")
print(f"Variable Expenses: {total_variable_expenses:.2f} THB")
print(f"Total Expenses: {total_expenses:.2f} THB")
print(f"Remaining: {remaining_income:.2f} THB")
print("\n=== SAVINGS BREAKDOWN ===")
print(f"Emergency Fund ({emergency_fund_percent}%): {emergency_fund_amount:.2f} THB")
print(f"Investment ({investment_percent}%): {investment_amount:.2f} THB")
print(f"Available for Savings: {available_for_savings:.2f} THB")
print("\n=== ANALYSIS ===")
print(f"Expense Ratio: {expense_ratio:.2f}%")