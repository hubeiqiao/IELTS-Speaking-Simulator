
import random
import datetime

def get_random_seed():
    # Generate a random seed based on the current time
    return int(datetime.datetime.now().timestamp())

def load_topics_from_file(file_path):
    # Load topics from the provided file
    with open(file_path, 'r') as file:
        topics = file.readlines()
    return [topic.strip() for topic in topics if topic.strip()]

def select_random_topics(topics, part, num_topics):
    # Select random topics based on the part of the IELTS test
    random.seed(get_random_seed())
    if part == 1:
        return random.sample(topics[:34], num_topics)  # For Part 1
    elif part in [2, 3]:
        return random.choice(topics[34:85])  # For Parts 2 and 3

def main():
    file_path = 'The Latest IELTS Topic Pool.txt'  # Path to the topic pool file
    topics = load_topics_from_file(file_path)

    # Example usage
    print("Part 1 Topics:", select_random_topics(topics, 1, 3))  # Select 3 topics for Part 1
    print("Part 2 Topic:", select_random_topics(topics, 2, 1))   # Select 1 topic for Part 2

if __name__ == "__main__":
    main()
