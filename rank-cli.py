#!/usr/bin/python3

import argparse
import json
import os


LIKES_KEYWORD = 'likes'
MID_KEYWORD = 'mid'
DISLIKES_KEYWORD = 'dislikes'


class RankedList:
	def __init__(self, list_filepath):
		self.list_filepath = list_filepath

		if not os.path.isfile(self.list_filepath):
			print(f"{self.list_filepath} does not already exist. Creating a new list...")
			self.likes = []
			self.mid = []
			self.dislikes = []
			self._write_out()
		else:
			self._parse_in()


	def _parse_in(self):
		with open(self.list_filepath, 'r') as list_file:
			list_data = json.load(list_file)
			# TODO: validate list_data in proper format

		self.likes = list_data[LIKES_KEYWORD]
		self.mid = list_data[MID_KEYWORD]
		self.dislikes = list_data[DISLIKES_KEYWORD]


	def _write_out(self):
		list_data = {
			LIKES_KEYWORD: self.likes,
			MID_KEYWORD: self.mid,
			DISLIKES_KEYWORD: self.dislikes
		}

		with open(self.list_filepath, 'w') as list_file:
			json.dump(list_data, list_file)


	def add_new_entry(self, name, skip_duplicate_check=False):
		if not skip_duplicate_check and (name in self.likes or name in self.mid or name in self.dislikes):
			print(f"{name} is already in your list! Use `--rerank` to change the rank.")
			return

		while True:
			print(f"What did you think of {name}?")
			rating = input("(0: I liked it!), (1: It was fine), (2: I didn't like it): ")

			if rating == '0':
				choice_list = self.likes
			elif rating == '1':
				choice_list = self.mid
			elif rating == '2':
				choice_list = self.dislikes
			else:
				print(f"Unrecognized option: '{rating}'. Must be '0', '1', or '2'.")
				continue

			break

		# Binary search
		n, left, right = 0, 0, len(choice_list) - 1
		choice = '0'
		while left <= right and len(choice_list) > 0:
			n = (left + right) // 2
			other_option = choice_list[n]

			print("Which do you prefer?")
			choice = input(f"(0: {name}), (1: {other_option}): ")

			if choice == '0':
				right = n - 1
			elif choice == '1':
				left = n + 1
			else:
				print(f"Unrecognized option: '{choice}'. Must be '0' or '1'.")

		if choice == '0':
			choice_list.insert(n, name)
		else:
			choice_list.insert(n + 1, name)
		self._write_out()


	def list_all_entries(self):
		ranking = []

		choice_lists = {LIKES_KEYWORD: self.likes, MID_KEYWORD: self.mid, DISLIKES_KEYWORD: self.dislikes}
		choice_rating_maxes = {LIKES_KEYWORD: 10.0, MID_KEYWORD: 6.6, DISLIKES_KEYWORD: 3.3}
		starting_rank = 1
		for choice_list_keyword, choice_list in choice_lists.items():
			for idx, name in enumerate(choice_list):
				rating = choice_rating_maxes[choice_list_keyword] - ((idx / len(choice_list)) * 3.3)
				ranking.append((starting_rank + idx, name, round(rating, 1)))
			starting_rank += len(choice_list)

		return ranking


	def delete(self,name):
		removed = False
		for choice_list in [self.likes, self.mid, self.dislikes]:
			if name in choice_list:
				choice_list.remove(name)
				removed = True
				break
		if not removed:
			raise ValueError(f"{name} does not exist in this list")
		self._write_out()


	def rerank(self, name):
		self.delete(name)
		print(f"Reranking {name}")
		self.add_new_entry(name, skip_duplicate_check=True)


	def __str__(self):
		result = ""
		for rank, name, rating in self.list_all_entries():
			result += f"{rank}: {name} (rating: {rating})\n"
		return result

def main():
	parser = argparse.ArgumentParser(description="A command-line interface for generating and maintaining rankings of things.")
	parser.add_argument('list_filepath', help="Path to the list JSON")
	# TODO: add nargs='*' to handle multiple new entries at at time
	group = parser.add_mutually_exclusive_group()
	group.add_argument('-n', '--new-entry', metavar="ENTRY_NAME", help="Add a new entry to the list")
	group.add_argument('-r', '--rerank', metavar="ENTRY_NAME", help="Rerank an existing item on the list")
	group.add_argument('-d', '--delete', metavar="ENTRY_NAME", help="Delete an entry from the list")
	args = parser.parse_args()

	rl = RankedList(args.list_filepath)

	if args.new_entry:
		rl.add_new_entry(args.new_entry)

	if args.rerank:
		rl.rerank(args.rerank)

	if args.delete:
		rl.delete(args.delete)

	print(rl)


if __name__ == '__main__':
	main()
