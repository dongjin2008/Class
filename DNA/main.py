def complement(UI):
    complement = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join([complement[base] for base in UI])

def reverse(UI):
    return UI[::-1]

def reverse_complement(UI):
    return reverse(complement(UI))

print(
"""
1. Complement
2. Reverse
3. Reverse Complement
"""
)

choice = int(input("Enter your choice: "))
UI = input("Enter the DNA sequence: ").upper()

if choice == 1:
  print(complement(UI))
elif choice == 2:
  print(reverse(UI))
elif choice == 3:
  print(reverse_complement(UI))