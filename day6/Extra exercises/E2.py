def exercise2_temp_converter():
    try:
        with open("celsius.txt", "r") as f:
            lines = [line.strip() for line in f if line.strip()]

        results = []
        for temp in lines:
            try:
                c = float(temp)
                f_temp = (c * 9 / 5) + 32
                results.append(f"{c}C = {f_temp}F")
            except ValueError:
                print(f"Skipping invalid temperature: {temp}")

        with open("fahrenheit.txt", "w") as f:
            for line in results:
                f.write(line + "\n")

        print("Conversion results saved to fahrenheit.txt")

    except FileNotFoundError:
        print("The celsius.txt file was not found.")
    except Exception as e:
        print("An unexpected error occurred:", e)

if __name__ == "__main__":
    exercise2_temp_converter()
    