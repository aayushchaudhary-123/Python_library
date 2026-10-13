import pyjokes

print("Programming Joke Generator")

# Print three jokes
for i in range(3):
    joke = pyjokes.get_joke()
    print("Joke:", joke)

# Ask the user if they want more jokes
answer = input("Do you want another joke? (yes/no): ").strip().lower()
while answer == "yes":
    print(pyjokes.get_joke())
    answer = input("Do you want another joke? (yes/no): ").strip().lower()

print("Thank you! Goodbye.")
