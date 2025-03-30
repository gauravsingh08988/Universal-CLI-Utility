import argparse

def main():
    parser = argparse.ArgumentParser(description="Universal CLI Utility")
    parser.add_argument("--ping", type=str, help="Ping a website")
    args = parser.parse_args()

    if args.ping:
        print(f"Pinging {args.ping}...")

if __name__ == "__main__":
    main()