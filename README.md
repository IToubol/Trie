# Trie Data Structure

A Python implementation of a Trie (prefix tree) from scratch.

## What is a Trie?

A Trie is a tree data structure where each node represents a character.
Words sharing a common prefix share the same path from the root.
It allows fast prefix-based search and insertion.

## Features

- Insert words (`add`)
- Check if a word exists (`contains`)
- Handles Unicode characters (accents, ligatures: `à`, `œuf`...)
- No external dependencies

## Usage

```python
from trie import Trie

trie = Trie()
trie.add("arbre")
trie.add("art")
trie.add("artiste")

trie.contains("art")     # True
trie.contains("artis")   # False
trie.contains("Bonjour") # False
```

## Run tests

```bash
python trie.py
```

## Stack

- Python 3.12+
- Standard library only (`typing`)

## Example
```
|
|__à *[à]
|
|__a
|  |__r
|     |__b
|     |  |__r
|     |     |__e *[arbre]
|     |
|     |__t *[art]
|        |__i
|           |__s
|              |__t
|                 |__e *[artiste]
|
|__c
|  |__h
|  |  |__a
|  |     |__p
|  |        |__e *[chape]
|  |           |__a
|  |              |__u *[chapeau]
|  |
|  |__r
|     |__é
|        |__a
|           |__t
|              |__i
|                 |__f *[créatif]
|                 |
|                 |__o
|                    |__n *[création]
|
|__œ
|  |__u
|     |__f *[œuf]
|
|__z
   |__è
      |__b
         |__r
            |__e *[zèbre]
```
