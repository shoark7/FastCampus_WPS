"""
This is code for household ledger.
I'm in a kakao talk open chatting room for python.
And someone uploaded his household ledger program code.
I guess it's worth reviewing.

And I put some notes for better code and good code.
"""

from itertools import product as cartesian_product
from operator import itemgetter
from os.path import exists


class HouseholdLedger(object):

  def __init__(self):
    self.options = {
      self.insert_entry: "Input entry",
      self.view_entry: "View entry",
      self.select_by_date: "Search results by date",
      self.select_by_item: "Search results by item",
      self.get_top: "Show top 10 most expensive products",
    }
    self.count = len(self.options.keys())
    #! len method for dict also operates on pure dict, not only on keys.
    #! it would be better --> len(self.options)

    self.filename = None
    self.content = None
    self.flatcache = []
    self.cache = {}
    # ! What is this caches for? I'm curious :)

  def load_file(self, file, permission='r'):
    """ Read a file and return content.
    :param filename: file name.
    :param permission: (optional) permission.
    """
    try: assert exists(str(file))
    except: raise AssertionError
    # ! 1. I think indenting would be much better, for readability and style guide for python
    # ! 2. I don't know what is str func for in here
    # ! 3. Also AssertionError is not that good, I guess.
    # ! FileNotFoundError would be much better.


    self.filename = file

    # read
    with open(file, permission) as f:
      self.content = filter(len, f.read().split('\n'))
      """
      This code is good. He's intention is to filter out the blank line('') with len method.
      Good! I learn something.
      """
      f.close()
    # ! close method is not needed here, because file is automatically closed
    # ! when 'with' statement is finished.
    # ! And I don't like 'f'. 'fp' would be better for other developers to understand.
    return self.content or []

  def build_cache(self):
    """ Cache objects from file content.
    """
    try: assert self.content
    except: raise ValueError

    for entry in self.content:
      date, *item, price = entry.split()
      """
      This code is also good.
      """

      # join item into single string
      item = ' '.join(item).lower()

      # cache
      if date in self.cache:
        self.cache[date].append((item, price))
      else:
        self.cache[date] = [(item, price)]

    # flatten cache
    for pairs in self.cache.items():
      for pair in pairs[1]:
        self.flatcache.append([pairs[0],pair[0],pair[1]])

    return self.cache or {}

  def select_by_date(self):
    """ Search rows by date.
    :param datetime: date (format: YYYY-MM-DD).
    """
    date = input("Date (YYYY-MM-DD): ")
    if 3 != len(date.split('-')):
      return False

    return tuple(self.cache[date])

  if __name__ == '__main__':
      if __name__ == '__main__':
          def select_by_item(self):
            """ Search rows by item.
            :param item: item.
            """
            item = input("Product: ").lower()
            return [ x for x in filter(lambda x:item in x, self.flatcache) ]
            # !We usualy make filter objects into list by list function
            # !But he used list comprehension. It's another good way maybe
            # !But style guide is somewhat ignored here, at the beginning and ending of statement

  def get_top(self, count=10):
    """ Get top 10 most expensive products.
    """
    return sorted(self.flatcache, key=lambda x:int(x[-1]), reverse=True)

  def view_entry(self):
    """ View current cache stack.
    """
    print(self.cache)

  def insert_entry(self):
    """ Insert a new row to cache.
    """
    date = input("Date (YYYY-MM-DD): ")
    if 3 != len(date.split('-')):
      return False

    item = input("Product: ")
    price = input("Price: ")

    if date in self.cache: self.cache[date].append((item, price))
    else: self.cache[date] = [(item, price)]
    return True

  def load(self):
    """ Provide interface.
    """
    try:
      # compile options into string-format
      menu = '\n'.join([ "[%s] %s." %(i, list(self.options.values())[i]) for i in range(self.count) ])
      """
      Great! Mr. Ahn's style, the most adorable part to me, is same here!!
      It's really good.
      """

      # rotate options until exit
      while 1:
      # !old style. I think 'True' would be better
        print(menu)
        choice = input(">> ")

        # error checking
        if not choice.strip() or not 0x30 <= ord(choice[0]) < (0x30 + self.count):
        """
        This code is very very interesting.
        He used 'ord' built-in function to check the choice letter.
        He didn't use any kind of 'str' or 'int' functions that I used to use.
        It has an interesting advantage,
            "Every character that the user inputs can be executed without no error"
        It doesn't matter if the choice is '*', '#', '?'. No errors.
        But 0x30 is not good to understnad. It would be much better if he used
        ord('0'), no 0x30. Who know that 0x30 is '0' actually.
        It's really impressive :)
        """
          print("[!] Not valid input. Exiting..")
          break

        # convert choice value to interpretable format
        choice = ord(choice) - 0x30

        # back result
        print(list(self.options.keys())[choice]())
        # !This code is not good. It's too, too difficult.
      except KeyboardInterrupt: print("\n[*] Exiting..")


if __name__ == '__main__':

  ledger = HouseholdLedger()
  ledger.load_file('../data/money.txt')
  ledger.build_cache()
  """
  No. not good. Cache is temporary, not driven from such as databases..
  """
  ledger.load()

