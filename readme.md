This project logs the bitcoin conversion rate (US dollars) 
as reported on coinbase.com

It is designed such that, if run on a consistent interval,
the output CSV could be used to produce a graph of the 
conversion rate over time and also to analyze the data.

Each time the script is run, it appends an entry into the CSV
of the form 'YYYYmmddHHMM,[price]\n'
For example:
201402122335,662.76
Represents the price of $662.76 on 12 February, 2014 at 23:35 UTC