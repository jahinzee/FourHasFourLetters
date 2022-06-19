# FourHasFourLetters
A Python app that demonstrates the weird and wonderful world of worded-form-length functions.

## Table of Contents
- [FourHasFourLetters](#fourhasfourletters)
  - [Table of Contents](#table-of-contents)
  - [Dependencies](#dependencies)
    - [What each dependency is for](#what-each-dependency-is-for)
  - [Theory](#theory)
    - [Base](#base)
    - [Chain](#chain)
      - [`namedtuple`](#namedtuple)
    - [Reel<sup>1</sup>](#reelsup1sup)
      - [`namedtuple`](#namedtuple-1)
  - [Usage](#usage)
    - [Working with Chains](#working-with-chains)
      - [Parameters](#parameters)
      - [Example](#example)
    - [Working with Reels](#working-with-reels)
      - [Parameters](#parameters-1)
      - [Example](#example-1)
  - [Future Plans](#future-plans)

## Dependencies
Install the dependencies first before using the scripts:
```
pip install -r requirements.txt
```

### What each dependency is for

| Package | Purpose |
| ------- | ------- |
| `num2words` | *Converts numbers to words.*<br>This is, of course, the heart of the app. |
| `colorama` | *A library that provides ANSI color codes for terminal output.*<br>This serves to make the terminal outputs easier on the eyes. |
| `tabulate` | *A library that provides a simple way to format tabular data.*<br>This also serves to make outputs cleaner. |

## Theory
This project involves the simple theory of a recursive word-length function. In other words, extending the idea of "Four Has Four Letters" to a more general case.

The code here is based on a [video](https://www.youtube.com/watch?v=LYKn0yUTIU4) by Matt Parker of [StandUpMaths](https://www.youtube.com/channel/UCSju5G2aFaWMqn-_0YBtq5A).

### Base
A base function that is used to generate chains and reels. These take a `language` parameter, which is represented in ISO 639-1. (e.g. `"en"` is English, `"kz"` is Kazakh, etc.)

**Note:** Supported languages include all the languages supported by `num2words`. A full list of supported languages can be found [here](https://github.com/savoirfairelinux/num2words#usage).

### Chain
A series of integers, with each step defined recursively as: `f(n) = len(wordedForm(n))`

Every chain features a *loop*, a subset at the end of the chain that is repeated infinitely.

#### `namedtuple`
This represents the data structure that is output by the `Chain().gen()` function:

```yaml
- Chain:
    - array: [1, 3, 5, 4]    // the chain of integers, ended by the last item in the terminating loop.
    - loop_start_idx: 3      // the index of the first loop integer in the chain. 
```

### Reel<sup>1</sup>
A series of chains, ranging from a `min` to a `max` integer.

#### `namedtuple`
This represents the data structure that is output by the `Reel().gen()` function:

```yaml
- Reel:
    - (Chain):                      // a wrapper for the chain data structure.
        - starting_integer: 1       // the starting integer of the chain.
        - Chain: [1, 3, 5, 4], 3    // the chain itself (see above).
```

## Usage

This project, as of now, is not complete. The base functionality is implemented, but so far it's not the most user-friendly experience.

To begin, run the following command to load the modules into the Python interpreter:
```bash
python -i output.py
```

### Working with Chains

To generate a chain, create a Chain object and run the `gen(i)` method. The parameters should be structured like this:

```
chain = Chain(language).gen(start)
```
#### Parameters
- `language`: The language to use for the chain. This is an optional parameter; not specifying it will use the default language of `"en"`.
- `start`: The starting integer of the chain.

#### Example

If we want to generate a chain for words in Finnish starting from 15, we first create it with the `Chain` class:
```python
>>> chain = Chain("fi").gen(15)
```

You can then use `print(chain)` to see the chain in a `namedtuple` format, however you can also use the `ChainOutput` class to get the chain in a more human-readable format:
```python
>>> chain_output = ChainOutput(chain)
>>> print(chain_output)
15 ━ 11 ━ 10 ━ 8 ━ 9
               ^   ^
```
Note the carat (`^`) characters in the chain. In this example, it represents the loop. 

When printing to a console, these will be displayed as yellow text, instead of having carats below them<sup>2</sup>. Think of these as overbars in recurring decimal notation.

### Working with Reels

Generating reels works in the same way as generating chains, but the parameters are different:
```
reel = Reel(language).gen(min, max)
```
#### Parameters
- `language`: The language to use for the chain. This is an optional parameter; not specifying it will use the default language of `"en"`.
- `min`, `max`: The range of integers to generate chains from (inclusive).

#### Example

To generate a reel for words in Vietnamese from 10 to 15:
```python
>>> reel = Reel("vi").gen(10, 15)
>>> reel_output = ReelOutput(reel)
>>> print(reel_output)
  Index  ┆    Chain
     10  ┆    10 ━ 4 ━ 3 ━ 2
     11  ┆    11 ━ 8 ━ 3 ━ 2
     12  ┆    12 ━ 8 ━ 3 ━ 2
     13  ┆    13 ━ 7 ━ 3 ━ 2
     14  ┆    14 ━ 8 ━ 3 ━ 2
     15  ┆    15 ━ 8 ━ 3 ━ 2
```

Note that for all of these, 3 and 2 represent the loop<sup>3</sup>.

## Future Plans

- [ ] Config file support
- [ ] Implement command-line switches + a guided terminal interface for the user.
- [ ] Improve efficiency via look-up tables.
- [ ] Allow for custom languages, including ones with terminating cases ([Pokémon??](https://www.youtube.com/watch?v=LYKn0yUTIU4&lc=UgiTAl4G7qjJ_HgCoAEC))

---
<sup>1</sup>: Why reels? Because the [collective noun for chain](https://www.answers.com/english-language-arts/What_is_the_collective_noun_of_chain), and indeed collective nouns in general, are weird.

<sup>2</sup>: This is due to a limitation of GitHub's Markdown rendering engine. If you're as passionately disappointed at this as I am, [please let them know](https://github.com/github/markup/issues/1440).

<sup>3</sup>: See Footnote 2.
