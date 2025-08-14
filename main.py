import sys

from classes.activity_fetcher import ActivityFetcher
from classes.summarizer import Summarizer


def main():

    if len(sys.argv) < 2:
        sys.exit("Please provide a GitHub username")

    username = sys.argv[1]

    data = ActivityFetcher.fetch_activities(username)

    if len(data) == 0:
        sys.exit("No events found")

    Summarizer.summarize(data)


if __name__ == "__main__":
    main()
