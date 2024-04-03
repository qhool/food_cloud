# Food Truck Word Cloud

This project generates a word cloud of food truck menu items from truck permitting data in San Francisco, filtered to trucks open on this day of the week. There are a lot of un-interesting.

You need a fairly modern python 3.8+; I used 3.11.

    mkdir venv
    python -m venv venv
    . ./venv/bin/activate
    ./setup.py install
    ./food_words
    deactivate

for now the number of most-frequent words is changed by editing the `ELIMINATE_MOST_COMMON` constant at the top of food_words.

Possible enhancements/fixes.

* Filter to trucks within a radius of a given address.
* Filter by time of day.
* Retain historical data, so newly open trucks can be shown.
* Web interface

The first two filtration steps are simple to implement.
