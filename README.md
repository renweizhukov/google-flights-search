# google-flights-search

A simple script for searching for one-way flights at https://google.com/flights

## Dependencies

To use this script, you need to install [ChromeDriver](https://chromedriver.chromium.org/) and some Python
packages via `pip install -r requirements.txt`.

## Sample usage

* To search the earliest one-way non-stop flight from Seattle to Shanghai from 2020-07-22 to 2021-04-01
which satisfies the following conditions:
  + on either Wednesday or Saturday;
  + served by either United or Delta.

```bash
$ python main.py -c="/Users/wrn/Downloads/chromedriver" -u="https://www.google.com/flights?hl=en#flt=SEA./m/06wjf.{date};c:USD;e:1;s:0;sd:1;st:none;t:f;tt:o" -s=2020-07-22 -e=2021-04-01 -w=Wed,Sat -a=United,Delta
```

* To search the earliest one-way non-stop flight from San Francisco to Shanghai from 2020-07-22 to 2021-04-01
which satisfies the following conditions:
  + on Thursday;
  + served by either Delta or United.

```bash
$ python main.py -c="/Users/wrn/Downloads/chromedriver" -u="https://www.google.com/flights?hl=en#flt=SFO./m/06wjf.{date};c:USD;e:1;s:0;sd:1;st:none;t:f;tt:o" -s=2020-07-22 -e=2021-04-01 -w=Thu -a=Delta,United
```

* To search the earliest one-way non-stop flight from Seattle to Shanghai from 2020-07-22 to 2021-04-01
which satisfies the following conditions:
  + on either Wednesday or Saturday;
  + flight# = DL281.

```bash
$ python main.py -c="/Users/wrn/Downloads/chromedriver" -u="https://www.google.com/flights?hl=en#flt=SEA./m/06wjf.{date};c:USD;e:1;s:0;sd:1;st:none;t:f;tt:o" -s=2020-07-22 -e=2021-04-01 -w=Wed,Sat -f=DL281
```


* To search the earliest one-way non-stop flight from San Francisco to Shanghai from 2020-07-22 to 2021-04-01
which satisfies the following conditions:
  + on either Wednesday or Saturday;
  + flight# = UA857.

```bash
$ python main.py -c="/Users/wrn/Downloads/chromedriver" -u="https://www.google.com/flights?hl=en#flt=SFO./m/06wjf.{date};c:USD;e:1;s:0;sd:1;st:none;t:f;tt:o" -s=2020-07-22 -e=2021-04-01 -w=Thu -f=UA857
```

* To get help info,

```bash
$ python main.py -h
```