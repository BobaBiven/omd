# Test instruction.

## issue 1
A test of morse code encoding.
doctest is used.

To run issue_1.py do:

```
python3 -m doctest -v issue_1.py
```

## issue 2
A test of morse code decoding.
pytest.parametrize is used.

To run issue_2.py you need to have pytest installed.
To install pytest do:
```
pip install -U pytest
```
in your virtual enviroment.



Then to run test:

```
python3 -m pytest -v issue_2.py
```

## issue 3
For the following 2 tests you will also need file one_hot_encoder.py, as it's code is being tested.
Here is a test using unittest.
To run issue_3 test do:

```
python3 -m unittest -v issue_3.py
```

## issue 4
This is a test of one_hot_encoder with pytest.
Assuming you already have pytest install after clause 2. If not, check how to in stall in clause 2. 
To run:

```
python3 -m pytest -v issue_4.py
```

## issue 5
In this test you will also need file called "what_year_is_now.py", as it's code is being tested.
To run test:
```
python3 -m pytest -v -s issue_5.py
```

To check what percetage of code is covered by tests you firstly need to install pytest-cov:
```
pip install -U pytest-cov
```
Then run:
```
python3 -m pytest -q issue_5.py --cov=what_is_year_now
```
