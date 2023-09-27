from teque import Teque


def main():
    with open("sample_input.txt", "r") as input_file:
        n = int(input_file.readline())

    teque = Teque()

    for _ in range(n):
        command, x = input().split()
        x = int(x)

        if command == "push_back":
            teque.push_back(x)
        elif command == "push_front":
            teque.push_front(x)
        elif command == "push_middle":
            teque.push_middle(x)
        elif command == "get":
            result = teque.get(x)
            print(f"Result: {result}")

    if __name__ == "__main__":
        main()
