import merge
import read_input


def write_output(filename, data):
    with open(filename, 'w') as file:
        for num in data:
            file.write(str(num) + '\n')


if __name__ == "__main__":
    sorted_data = merge(input_data)
    output_filename = "output.txt"  # Angi ønsket filnavn for resultatet
    write_output(output_filename, sorted_data)
