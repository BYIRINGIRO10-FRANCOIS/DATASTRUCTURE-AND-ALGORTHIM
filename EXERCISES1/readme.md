"""
# Project 10: Bookstore Sales Summary

This project demonstrates the use of **integers, strings, booleans, lists, arrays, and dictionaries** in Python through a simple **Bookstore Sales Summary** program.

---

## Features

### 1. Integers
- Sales data (`daily_sales`) is represented as integers.
- The program calculates:
  - **Total sales**
  - **Average sales**
  - **Minimum and maximum sales**

### 2. Strings
- Uses **f-strings** to create a clear, formatted report.

### 3. Booleans
- A threshold condition checks if the **average sales** exceed a set value.
- Includes a **compound condition** (average > threshold **and** number of days > 3).

### 4. Lists
- Sales records are stored in a list.
- Demonstrates:
  - **Adding** an element
  - **Removing** an element based on a condition
  - **Sorting** the list
- The list is displayed **before and after** each change.

### 5. Arrays
- Uses the built-in **array** module for a fixed-size numeric subset.
- Computes the sum of the array and compares it with the list sum.

### 6. List of Dictionaries
- Each record contains: `id`, `name`, `value`
- Demonstrates:
  - **Updating** a record
  - **Deleting** a record
  - **Computing totals** across records

---

## Example Output

Initial daily sales: [25, 30, 40, 35, 20]

---- Bookstore Sales Summary ----
Total sales: 150 books
Average daily sales: 30.00 books
Minimum daily sales: 20, Maximum daily sales: 40
Status: Above Standard

--- Daily Sales List Changes ---
Original list: [25, 30, 40, 35, 20]
After adding 28: [25, 30, 40, 35, 20, 28]
After removing 20 (first value < 25): [25, 30, 40, 35, 28]
After sorting: [25, 28, 30, 35, 40]

--- Array Subset ---
Array contents: [25, 28, 30]
Array sum: 83
List sum: 158
Array subset sum is smaller than total list sum.

Initial records: [{'id': 1, 'name': 'Novel A', 'value': 12}, {'id': 2, 'name': 'Novel B', 'value': 8}, {'id': 3, 'name': 'Comics', 'value': 5}]
After updating Novel B: [{'id': 1, 'name': 'Novel A', 'value': 12}, {'id': 2, 'name': 'Novel B', 'value': 10}, {'id': 3, 'name': 'Comics', 'value': 5}]
After deleting Comics: [{'id': 1, 'name': 'Novel A', 'value': 12}, {'id': 2, 'name': 'Novel B', 'value': 10}]
Total value across records: 22

---

## How to Run

1. Save this file as `bookstore_summary.py`
2. Run with: `python bookstore_summary.py`
"""

from array import array

# -------------------------------------------
# Integers: Generate or input bookstore sales
# -------------------------------------------
daily_sales = [25, 30, 40, 35, 20]
print("Initial daily sales:", daily_sales)

# Compute total, average, min, max
total_sales = sum(daily_sales)
average_sales = total_sales / len(daily_sales)
min_sales = min(daily_sales)
max_sales = max(daily_sales)

print("\n---- Bookstore Sales Summary ----")
print(f"Total sales: {total_sales} books")
print(f"Average daily sales: {average_sales:.2f} books")
print(f"Minimum daily sales: {min_sales}, Maximum daily sales: {max_sales}")

# -------------------------------------------
# Booleans
# -------------------------------------------
threshold = 30
if average_sales > threshold and len(daily_sales) > 3:
    print("Status: Above Standard")
else:
    print("Status: Below Standard")

# -------------------------------------------
# Lists
# -------------------------------------------
print("\n--- Daily Sales List Changes ---")
print("Original list:", daily_sales)

daily_sales.append(28)
print("After adding 28:", daily_sales)

for x in daily_sales:
    if x < 25:
        daily_sales.remove(x)
        print(f"After removing {x} (first value < 25):", daily_sales)
        break

daily_sales.sort()
print("After sorting:", daily_sales)

# -------------------------------------------
# Arrays
# -------------------------------------------
sales_array = array('i', daily_sales[:3])
print("\n--- Array Subset ---")
print("Array contents:", sales_array.tolist())

array_sum = sum(sales_array)
print("Array sum:", array_sum)
print("List sum:", sum(daily_sales))

if array_sum < sum(daily_sales):
    print("Array subset sum is smaller than total list sum.")

# -------------------------------------------
# List of Dictionaries
# -------------------------------------------
records = [
    {"id": 1, "name": "Novel A", "value": 12},
    {"id": 2, "name": "Novel B", "value": 8},
    {"id": 3, "name": "Comics", "value": 5}
]
print("\nInitial records:", records)

for r in records:
    if r["id"] == 2:
        r["value"] = 10
        print("After updating Novel B:", records)
        break

records = [r for r in records if r["id"] != 3]
print("After deleting Comics:", records)

total_value = sum(r["value"] for r in records)
print("Total value across records:", total_value)
