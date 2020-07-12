# google-flights-search

A simple script for searching for one-way flights at https://google.com/flights

## Dependencies

To use this script, you need to install [ChromeDriver](https://chromedriver.chromium.org/) and some Python
packages via `pip install -r requirements.txt`.

## Sample usage

* To search the earliest one-way flight from Seattle to Shanghai from 2020-07-26 to 2020-11-01,

```bash
$ python main.py -c="/Users/wrn/Downloads/chromedriver" -u="https://www.google.com/flights?hl=en#flt=SEA./m/06wjf.{date};c:USD;e:1;s:1;sd:1;st:none;t:f;tt:o" -s=2020-07-26 -e=2020-11-01
```

* To get help info,

```bash
$ python main.py -h
```