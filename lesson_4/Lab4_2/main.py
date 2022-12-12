# COMP 1516 - Lab4 Part2
# Vilmor Somera
# 10/15/22

import data_format as x

def main():
    info = x.get_book_info()
    print("The CSV Format String:\n",x.csv_fomrat(info))
    print("The JSON Format String:\n",x.json_format(info))

if __name__ == "__main__":
    main()
    