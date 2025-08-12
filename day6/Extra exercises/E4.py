def exercise4_log_analyzer():
    try:
        with open("server.log", "r") as f:
            logs = f.readlines()

        status_counts = {"200": 0, "404": 0, "500": 0}

        for line in logs:
            parts = line.strip().split()
            if len(parts) >= 2:
                status = parts[1]
                if status in status_counts:
                    status_counts[status] += 1

        with open("report.txt", "w") as f:
            f.write(f"Successful (200): {status_counts['200']}\n")
            f.write(f"Not Found (404): {status_counts['404']}\n")
            f.write(f"Server Error (500): {status_counts['500']}\n")

        print("Report saved to report.txt")

    except FileNotFoundError:
        print("The server.log file was not found.")
    except Exception as e:
        print("An unexpected error occurred:", e)

if __name__ == "__main__":
    exercise4_log_analyzer()