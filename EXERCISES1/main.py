# Bookstore Sales Summary
import array

# 1. Integers: Sales quantities for 7 days
sales_quantities = [120, 95, 110, 130, 105, 90, 115]
total_sales = sum(sales_quantities)
average_sales = total_sales / len(sales_quantities)
min_sales = min(sales_quantities)
max_sales = max(sales_quantities)

# 2. Strings: Formatted report
report = f"Total sales for the week: {total_sales}\n"
report += f"Average daily sales: {average_sales:.2f}\n"
report += f"Minimum sales in a day: {min_sales}\n"
report += f"Maximum sales in a day: {max_sales}\n"
print(report)

# 3. Booleans: Threshold check with compound condition
threshold = 100
above_standard = average_sales > threshold and max_sales > 120
if above_standard:
    print("Status: Above Standard")
else:
    print("Status: Below Standard")

# 4. Lists: Manage sales list
print(f"\nOriginal sales list: {sales_quantities}")
sales_quantities.append(125)  # Add new day's sales
sales_quantities = [qty for qty in sales_quantities if qty != min_sales]  # Remove day with min sales
sales_quantities.sort()
print(f"Modified and sorted sales list: {sales_quantities}")

# 5. Arrays: Fixed-size numeric subset
sales_array = array.array('i', sales_quantities[:5])  # First 5 days
array_sum = sum(sales_array)
print(f"\nSum of array (first 5 days): {array_sum}")
print(f"Sum of list (first 5 days): {sum(sales_quantities[:5])}")

# 6. List of dictionaries: Book records
books = [
    {'id': 1, 'name': 'Book A', 'value': 250},
    {'id': 2, 'name': 'Book B', 'value': 180},
    {'id': 3, 'name': 'Book C', 'value': 320},
    {'id': 4, 'name': 'Book D', 'value': 150},
]
# Update Book B's value
for book in books:
    if book['id'] == 2:
        book['value'] = 200
# Delete Book D
books = [book for book in books if book['id'] != 4]
# Compute total value
total_value = sum(book['value'] for book in books)
print(f"\nBook records: {books}")
print(f"Total value of all books: {total_value}")
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

# -------------------------------------------
# Strings: Formatted report using f-strings
# -------------------------------------------
print("\n---- Bookstore Sales Summary ----")
print(f"Total sales: {total_sales} books")
print(f"Average daily sales: {average_sales:.2f} books")
print(f"Minimum daily sales: {min_sales}, Maximum daily sales: {max_sales}")

# -------------------------------------------
# Booleans: Threshold check with compound condition
# -------------------------------------------
threshold = 30
if average_sales > threshold and len(daily_sales) > 3:
    print("Status: Above Standard")
else:
    print("Status: Below Standard")

# -------------------------------------------
# Lists: Modify and display step by step
# -------------------------------------------
print("\n--- Daily Sales List Changes ---")
print("Original list:", daily_sales)

# Add a new day’s sales
daily_sales.append(28)
print("After adding 28:", daily_sales)

# Remove the first value less than 25 (if any)
for x in daily_sales:
    if x < 25:
        daily_sales.remove(x)
        print(f"After removing {x} (first value < 25):", daily_sales)
        break

# Sort the list
daily_sales.sort()
print("After sorting:", daily_sales)

# -------------------------------------------
# Arrays: Using the array module
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
# List of Dictionaries: Records
# -------------------------------------------
records = [
    {"id": 1, "name": "Novel A", "value": 12},
    {"id": 2, "name": "Novel B", "value": 8},
    {"id": 3, "name": "Comics", "value": 5}
]
print("\nInitial records:", records)

# Update value of Novel B
for r in records:
    if r["id"] == 2:
        r["value"] = 10
        print("After updating Novel B:", records)
        break

# Delete Comics record
records = [r for r in records if r["id"] != 3]
print("After deleting Comics:", records)

# Compute total value across records
total_value = sum(r["value"] for r in records)
print("Total value across records:", total_value)
