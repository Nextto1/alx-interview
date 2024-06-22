import sys
import signal

def print_statistics(total_size, status_counts):
    print(f"File size: {total_size}")
    for status_code in sorted(status_counts.keys()):
        print(f"{status_code}: {status_counts[status_code]}")

def parse_line(line):
    try:
        parts = line.split()
        ip = parts[0]
        date = parts[3] + " " + parts[4]
        request = " ".join(parts[5:8])
        status_code = parts[8]
        file_size = parts[9]

        if not request.startswith('"GET /projects/260 HTTP/1.1"'):
            return None, None
        
        status_code = int(status_code)
        file_size = int(file_size)
        
        return status_code, file_size
    except (IndexError, ValueError):
        return None, None

def main():
    total_size = 0
    status_counts = {}
    line_count = 0

    def signal_handler(sig, frame):
        print_statistics(total_size, status_counts)
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    try:
        for line in sys.stdin:
            line_count += 1
            status_code, file_size = parse_line(line)

            if status_code is not None and file_size is not None:
                total_size += file_size
                if status_code in status_counts:
                    status_counts[status_code] += 1
                else:
                    status_counts[status_code] = 1

            if line_count % 10 == 0:
                print_statistics(total_size, status_counts)

    except KeyboardInterrupt:
        print_statistics(total_size, status_counts)
        sys.exit(0)

    print_statistics(total_size, status_counts)

if __name__ == "__main__":
    main()
