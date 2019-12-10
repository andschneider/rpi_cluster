import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--hello", type=str)
    parser.add_argument("-w", type=str)
    parser.add_argument("-n", type=int, required=True)
    args = vars(parser.parse_args())

    if args.get("hello"):
        for i in range(args["n"]):
            print(f"{args['hello']} world")
    
    if args.get("w"):
        for i in range(args["n"]):
            print(f"hello {args['w']}")
