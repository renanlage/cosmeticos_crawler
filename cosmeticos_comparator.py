import csv

from collections import Counter


class CosmeticosSpiderComparator:
    def __init__(self, filename1, filename2):
        self.filename1 = filename1
        self.filename2 = filename2
        self.products_counter = Counter()

    def same_n_lines(self):
        # Count number of lines from first file
        n_lines1 = 0
        with open(self.filename1, 'rt') as f1:
            for line in f1:
                n_lines1 += 1

        print "Number of lines in file " + self.filename1 + ": " + str(n_lines1)

        # Decrement number of lines in second file from counter
        n_lines2 = 0
        with open(self.filename2, 'rt') as f2:
            for line in f2:
                n_lines2 += 1

        print "Number of lines in file " + self.filename2 + ": " + str(n_lines2)

        # If number of lines decremented is different than incremented return false
        return n_lines1 == n_lines2

    def same_products(self):
        # Count the number of times a url appear in file 1 and 2
        with open(self.filename1, 'rt') as f1:
            reader = csv.reader(f1)
            for line in reader:
                url = line[0]
                self.products_counter[url] += 1

        with open(self.filename2, 'rt') as f2:
            reader = csv.reader(f2)
            for line in reader:
                url = line[0]
                self.products_counter[url] += 1

        # Check number of urls is always equal to 2
        # every url appears just once in each file
        for n_url in self.products_counter.values():
            if n_url != 2:
                return False
        return True

    def get_different_products(self):
        products1 = []
        with open(self.filename1, 'rt') as f1:
            reader = csv.reader(f1)
            for line in reader:
                url = line[0]
                products1.append(url)

        products2 = []
        with open(self.filename2, 'rt') as f2:
            reader = csv.reader(f2)
            for line in reader:
                url = line[0]
                products2.append(url)

        for url in set(products1).symmetric_difference(set(products2)):
            print url


def main():
    comparator = CosmeticosSpiderComparator('cosmeticos_sitemap.csv', 'cosmeticos_deu_errado.csv')
    print comparator.same_n_lines()
    print comparator.same_products()
    comparator.get_different_products()

if __name__ == "__main__":
    main()