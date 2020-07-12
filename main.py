#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import date, datetime, timedelta
from selenium import webdriver
from time import sleep

import argparse
import beepy
import sys


def date_range(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


def print_flight_info(flight_list, curr_date):
    print("Found {} flights on {}".format(len(flight_list), curr_date.strftime("%Y-%m-%d")))
    print("==========================================================")
    for flight in flight_list:
        print(repr(flight))


def keep_playing_success_beep():
    while True:
        beepy.beep(sound="success")
        sleep(timedelta(minutes=1).total_seconds())


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="Search for the flights on the earliest date given a date range",
    )
    parser.add_argument(
        "-c",
        "--chromedriver-path",
        required=True,
        help="Full path to the ChromeDriver executable"
    )
    parser.add_argument(
        "-u",
        "--google-flights-url",
        required=True,
        help="""Google flights url where the exact date is replaced with a formatting
        placeholder, e.g., 
        https://www.google.com/flights?hl=en#flt=SEA./m/06wjf.{date};c:USD;e:1;s:1;sd:1;st:none;t:f;tt:o
        """
    )
    parser.add_argument(
        "-s",
        "--start-date",
        default=date.today().strftime("%Y-%m-%d"),  # If not specified, use today's date.
        help="Start date in the format of YYYY-MM-DD (included in search date range)"
    )
    parser.add_argument(
        "-e",
        "--end-date",
        required=True,
        help="End date in the format of YYYY-MM-DD (included in search date range)"
    )
    parser.add_argument(
        "-r",
        "--retry-interval",
        type=int,
        default=30,
        help="Retry interval in minutes"
    )
    args = parser.parse_args()

    # Open a Chrome window using ChromeDriver.
    driver = webdriver.Chrome(executable_path=args.chromedriver_path)
    sleep(timedelta(seconds=5).total_seconds())

    start_date = datetime.strptime(args.start_date, "%Y-%m-%d")
    end_date = datetime.strptime(args.end_date, "%Y-%m-%d")
    found_flights = False
    while True:
        try:
            for curr_date in date_range(start_date, end_date):
                google_flights_url = args.google_flights_url.format(date=curr_date.strftime("%Y-%m-%d"))
                print("Opening {}".format(google_flights_url))
                driver.get(google_flights_url)
                sleep(timedelta(seconds=3).total_seconds())
                xp_results_table = "//li[contains(@class, 'gws-flights-results__result-item')]"
                flight_containers = driver.find_elements_by_xpath(xp_results_table)
                flight_list = [flight.text for flight in flight_containers]
                if flight_list:
                    print_flight_info(flight_list, curr_date)
                    found_flights = True
                    break
            if found_flights:
                keep_playing_success_beep()
            else:
                print("No flights found. Sleeping {} minutes before retrying".format(args.retry_interval))
                sleep(timedelta(minutes=args.retry_interval).total_seconds())
        except KeyboardInterrupt:
            print("Program exiting...")
            sys.exit()


if __name__ == "__main__":
    main()
