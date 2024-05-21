# rank-cli

This is essentially Beli but you can use it to rank anything.

Right now it is just a command-line interface, but maybe in the future I will turn it into a web app or make a GUI or something.

## Usage

```
usage: rank-cli.py [-h] [-n ENTRY_NAME | -r ENTRY_NAME | -d ENTRY_NAME] list_filepath

A command-line interface for generating and maintaining rankings of things.

positional arguments:
  list_filepath         Path to the list JSON

options:
  -h, --help            show this help message and exit
  -n ENTRY_NAME, --new-entry ENTRY_NAME
                        Add a new entry to the list
  -r ENTRY_NAME, --rerank ENTRY_NAME
                        Rerank an existing item on the list
  -d ENTRY_NAME, --delete ENTRY_NAME
                        Delete an entry from the list
```

## Examples

### Starting a new list

You can start a new list by simply specifying a filename which does not exist yet.

```
michael@michael-MS-7D43:~/projects/rank$ python3 rank-cli.py musicians
musicians does not already exist. Creating a new list...

michael@michael-MS-7D43:~/projects/rank$ 

```

### Adding to the list

You can add to the list by appending `-n "name of list entry"` or `--new-entry "name"`.

You will then be prompted with some questions to decide where in the list to put the new entry.

```
michael@michael-MS-7D43:~/projects/rank$ python3 rank-cli.py musicians --new-entry "Owl City"
musicians does not already exist. Creating a new list...
What did you think of Owl City?
(0: I liked it!), (1: It was fine), (2: I didn't like it): 0
1: Owl City (rating: 10.0)

michael@michael-MS-7D43:~/projects/rank$ python3 rank-cli.py musicians --new-entry "Porter Robinson"
What did you think of Porter Robinson?
(0: I liked it!), (1: It was fine), (2: I didn't like it): 0
Which do you prefer?
(0: Porter Robinson), (1: Owl City): 0
1: Porter Robinson (rating: 10.0)
2: Owl City (rating: 8.3)

michael@michael-MS-7D43:~/projects/rank$ python3 rank-cli.py musicians --new-entry "The 1975"
What did you think of The 1975?
(0: I liked it!), (1: It was fine), (2: I didn't like it): 0
Which do you prefer?
(0: The 1975), (1: Porter Robinson): 1
Which do you prefer?
(0: The 1975), (1: Owl City): 1
1: Porter Robinson (rating: 10.0)
2: Owl City (rating: 8.9)
3: The 1975 (rating: 7.8)

michael@michael-MS-7D43:~/projects/rank$ python3 rank-cli.py musicians --new-entry "Maroon 5"
What did you think of Maroon 5?
(0: I liked it!), (1: It was fine), (2: I didn't like it): 1
1: Porter Robinson (rating: 10.0)
2: Owl City (rating: 8.9)
3: The 1975 (rating: 7.8)
4: Maroon 5 (rating: 6.6)

michael@michael-MS-7D43:~/projects/rank$ python3 rank-cli.py musicians -n "Rebecca Black"
What did you think of Rebecca Black?
(0: I liked it!), (1: It was fine), (2: I didn't like it): 2
1: Porter Robinson (rating: 10.0)
2: Owl City (rating: 8.9)
3: The 1975 (rating: 7.8)
4: Maroon 5 (rating: 6.6)
5: Rebecca Black (rating: 3.3)

michael@michael-MS-7D43:~/projects/rank$ 
```

### Viewing an existing list

```
michael@michael-MS-7D43:~/projects/rank$ python3 rank-cli.py musicians
1: Porter Robinson (rating: 10.0)
2: Owl City (rating: 8.9)
3: The 1975 (rating: 7.8)
4: Maroon 5 (rating: 6.6)
5: Rebecca Black (rating: 3.3)

michael@michael-MS-7D43:~/projects/rank$ 
```

### Reranking an item

```
michael@michael-MS-7D43:~/projects/rank$ python3 rank-cli.py musicians --rerank "The 1975"
Reranking The 1975
What did you think of The 1975?
(0: I liked it!), (1: It was fine), (2: I didn't like it): 1
Which do you prefer?
(0: The 1975), (1: Maroon 5): 1
1: Porter Robinson (rating: 10.0)
2: Owl City (rating: 8.3)
3: Maroon 5 (rating: 6.6)
4: The 1975 (rating: 4.9)
5: Rebecca Black (rating: 3.3)

michael@michael-MS-7D43:~/projects/rank$ 

```

### Deleting items

```
michael@michael-MS-7D43:~/projects/rank$ michael@michael-MS-7D43:~/projects/rank$ python3 rank-cli.py musicians 
1: Porter Robinson (rating: 10.0)
2: Owl City (rating: 8.3)
3: Taylor Swift (rating: 6.6)
4: The 1975 (rating: 5.5)
5: Maroon 5 (rating: 4.4)
6: Rebecca Black (rating: 3.3)

michael@michael-MS-7D43:~/projects/rank$ python3 rank-cli.py musicians --delete "Maroon 5"
1: Porter Robinson (rating: 10.0)
2: Owl City (rating: 8.3)
3: Taylor Swift (rating: 6.6)
4: The 1975 (rating: 4.9)
5: Rebecca Black (rating: 3.3)

michael@michael-MS-7D43:~/projects/rank$ 
```
