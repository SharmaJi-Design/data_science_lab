import re
paragraph = """
London is a beautiful city. Python is a popular programming language.
Rocky and Razz went to the park. Kathmandu is capital city of Nepal.
"""
uppercase_words = re.findall(r'\b[A-Z][a-zA-Z]*\b', paragraph)

print("Words starting with an uppercase letter:", uppercase_words)