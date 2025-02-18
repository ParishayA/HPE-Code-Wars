import re

def clean_data(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        
        data_line = lines[0].strip()
        checksum_line = lines[1].strip()

        expected_sum = float(checksum_line.split("=")[-1].strip())
        
        valid_numbers = re.findall(r'\d+\.\d+|\d+', data_line)
        
        calculated_sum = sum(float(num) for num in valid_numbers)
        
        print(" ".join(valid_numbers))

        if abs(calculated_sum - expected_sum) < 1e-9:
            print("CHECKED")
        else:
            print(f"BADCHECK:{calculated_sum}")

clean_data('input14.txt')