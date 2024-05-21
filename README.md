# rank-cli

This is essentially Beli but you can use it to rank anything.

Right now it is just a command-line interface, but maybe in the future I will turn it into a web app or make a GUI or something.

## Usage

```
usage: rank-cli.py [-h] [-n NEW_ENTRY] list_filepath

A command-line interface for generating and maintaining rankings of things.

positional arguments:
  list_filepath         Path to the list JSON

options:
  -h, --help            show this help message and exit
  -n NEW_ENTRY, --new-entry NEW_ENTRY
                        Add a new entry to the list
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
Adding Owl City to list.
What did you think of Owl City?
(0: I liked it!), (1: It was fine), (2: I didn't like it): 0
1: Owl City (rating: 10.0)

michael@michael-MS-7D43:~/projects/rank$ python3 rank-cli.py musicians --new-entry "Porter Robinson"
Adding Porter Robinson to list.
What did you think of Porter Robinson?
(0: I liked it!), (1: It was fine), (2: I didn't like it): 0
Which do you prefer?
(0: Porter Robinson), (1: Owl City): 0
1: Porter Robinson (rating: 10.0)
2: Owl City (rating: 8.3)

michael@michael-MS-7D43:~/projects/rank$ python3 rank-cli.py musicians --new-entry "The 1975"
Adding The 1975 to list.
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
Adding Maroon 5 to list.
What did you think of Maroon 5?
(0: I liked it!), (1: It was fine), (2: I didn't like it): 1
1: Porter Robinson (rating: 10.0)
2: Owl City (rating: 8.9)
3: The 1975 (rating: 7.8)
4: Maroon 5 (rating: 6.6)

michael@michael-MS-7D43:~/projects/rank$ python3 rank-cli.py musicians -n "Jake Paul"
Adding Jake Paul to list.
What did you think of Jake Paul?
(0: I liked it!), (1: It was fine), (2: I didn't like it): 2
1: Porter Robinson (rating: 10.0)
2: Owl City (rating: 8.9)
3: The 1975 (rating: 7.8)
4: Maroon 5 (rating: 6.6)
5: Jake Paul (rating: 3.3)

michael@michael-MS-7D43:~/projects/rank$ 
```

### Viewing an existing list

```
michael@michael-MS-7D43:~/projects/rank$ python3 rank-cli.py musicians
1: Porter Robinson (rating: 10.0)
2: Owl City (rating: 8.9)
3: The 1975 (rating: 7.8)
4: Maroon 5 (rating: 6.6)
5: Jake Paul (rating: 3.3)

michael@michael-MS-7D43:~/projects/rank$ 
```
