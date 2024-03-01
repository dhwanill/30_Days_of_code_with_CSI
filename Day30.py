# Day 30
# Farewell Message Generator

def generate_farewell_message(name, feedback):
    farewell_message = f"Dear {name},\nThank you for sharing your feedback. We're delighted to hear about your positive experience and the valuable lessons you've gained during the 30 Days of Code challenge. Your dedication and enthusiasm have been inspiring. Farewell and best wishes for your future coding endeavors!"
    return farewell_message

# Getting user input
name = input("Name: ")
feedback = input("Feedback: ")

# Generating and displaying farewell message
farewell_message = generate_farewell_message(name, feedback)
print("\nOutput:\n" + farewell_message)