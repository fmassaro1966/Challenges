for i in range(1, 101):
    output = []

    if i % 11 == 0:
        output = ["Bong"]  # Overrides all others
    else:
        if i % 3 == 0:
            output.append("Fizz")
        if i % 5 == 0:
            output.append("Buzz")
        if i % 7 == 0:
            output.append("Bang")

    if i % 13 == 0:
        # Insert "Fezz" before first word starting with "B"
        inserted = False
        for j in range(len(output)):
            if output[j].startswith("B"):
                output.insert(j, "Fezz")
                inserted = True
                break
        if not inserted:
            output.append("Fezz")

    if i % 17 == 0:
        output.reverse()

    print(f"{i}: {''.join(output) if output else i}")
# Extended FizzBuzz implementation with additional rules