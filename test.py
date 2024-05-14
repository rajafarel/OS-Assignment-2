import random

# Generate 1000 random cylinder requests and write them to a text file
def generate_requests(filename):
    with open(filename, 'w') as file:
        for _ in range(1000):
            request = random.randint(0, 4999)
            file.write(str(request) + '\n')

generate_requests('request.txt')

