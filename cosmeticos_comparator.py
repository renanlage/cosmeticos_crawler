import csv

from collections import Counter


class CosmeticosSpiderComparator:
    def __init__(self, filename1, filename2):
        self.filename1 = filename1
        self.filename2 = filename2
        self.products_counter = Counter()

    def same_n_lines(self):
        # Count number of lines from first file
        count = 0
        with open(self.filename1, 'rt') as f1:
            for line in f1:
                count += 1

        # Decrement number of lines in second file from counter
        with open(self.filename2, 'rt') as f2:
            for line in f2:
                count -= 1

        # If number of lines decremented is different than incremented return false
        return count == 0

    def same_products(self):
        # Count the number of times a url appear in file 1 and 2
        with open(self.filename1, 'rt') as f1:
            reader = csv.reader(f1)
            for line in reader:
                url = line[1]
                self.products_counter[url] += 1

        with open(self.filename2, 'rt') as f2:
            reader = csv.reader(f2)
            for line in reader:
                url = line[1]
                self.products_counter[url] += 1

        # Check number of urls is always equal to 2
        # every url appears just once in each file
        for n_url in self.products_counter.values():
            if n_url != 2:
                return False
        return True


def main():
    comparator = CosmeticosSpiderComparator('cosmeticos_sitemap.csv', 'cosmeticos_only_products.csv')
    print comparator.same_n_lines() == True
    print comparator.same_products() == True

if __name__ == "__main__":
    main()
