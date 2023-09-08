---
layout: default
title: Asynchronous programming
permalink: /asyncio
---

## Asynchronous programming

Asynchronous programming is becoming more and more popular in Python since the introduction in Python 3.5 (with [PEP 492](https://www.python.org/dev/peps/pep-0492)) of two keywords: `await` and `async`.

It is important to be aware of few facts about Python performance:

- the _GIL_ (Global Interpreter Lock) from the C Python implementation puts a strong limitation in Python performance: programs with strong computing requirements **cannot** be accelerated with multithreading. Multiprocessing is an option, but it comes with its set of limitations;

- Multithreading remains however relevant when a program uses a lot of blocking calls. These includes I/O calls (writing a file, sending a request on the web, accessing USB devices): multithreading releases the _GIL_ during these blocking calls, and allows the program to perform other tasks while the first task is waiting for a blocking call to complete.

Asynchronous programming, also known under the name of a Python module `asyncio`, provides a **single threaded** efficient implementation of programs made of blocking calls.

If the following Spongebob is rather multiprocessing:

<img class="giphy" src="https://media.giphy.com/media/3DnDRfZe2ubQc/giphy.webp"/>

<div class="alert alert-info">
asynchronous programming is more about vacuuming while the dishwasher cleans instead of waiting for it to finish before doing your next chores.
</div>

The **tl;dr version of `asyncio`** goes as follows:

- blocking calls are annotated with the `await` keyword. The Python interpreter (and its main _loop_) will put this function on hold until the reply comes, and proceed with different asynchronous calls;

- functions with an `await` keyword in their implementation must be prefixed with the `async` keyword; an `async` function must be `await`ed. This may sound like egg or chicken, and that actually may make it all confusing before you get used to it.

So let's start with a function which does nothing more than sleeping:

```python
async def count():
    print("one")
    await asyncio.sleep(1)
    print("two")
```

If you run it once, it will take... one second:

```python
>>> import asyncio
>>>
>>> loop = asyncio.get_event_loop()  # the loop in charge of sequencing async calls
>>> loop.run_until_complete(count())
one
two
```

But if you run several calls together, it will also take one second. Check the printing order: the loop schedules the next call of `count()` when it hits on an `await` instruction:

```python
>>> loop.run_until_complete(asyncio.gather(count(), count(), count()))
one
one
one
two
two
two
```

<div class="alert alert-danger">
<b>Warning</b> &nbsp;&nbsp; Jupyter notebooks run in an asynchronous environment where an event loop already runs in background. It is therefore not possible to run the code above as is.
<br/>
You would get the following exception:<br/>
<pre><code>RuntimeError: This event loop is already running.</code></pre>
It is however possible to run a cell with an `await` keyword. The following code is valid in Jupyter but not in Python:<br/>
<pre><code>await asyncio.gather(count(), count(), count())</code></pre>
</div>

In practice, many libraries made of blocking calls provide an asynchronous version of their code, which becomes relevant if you need to make many small blocking calls, e.g. many small downloads, or many calls to a database.

### Comparison between blocking and non-blocking downloads

`requests` is the most common library for synchronous http requests. For this example, let's download all flags of the world from [https://flagcdn.com/](https://flagcdn.com/).

The full list of flags is available at the following link:

```python
import requests

c = requests.get("https://flagcdn.com/fr/codes.json")
c.raise_for_status()
codes = c.json()
# >>> codes {'ad': 'Andorre', 'ae': 'Émirats arabes unis', 'af': 'Afghanistan',
# 'ag': 'Antigua-et-Barbuda', 'ai': 'Anguilla', 'al': 'Albanie', 'am':
# 'Arménie', 'ao': 'Angola', 'aq': 'Antarctique', 'ar': 'Argentine', ...
```

Now we can time the synchronous download of all flags:

```python
from tqdm import tqdm

for c in tqdm(codes.keys()):
    r = requests.get(f'https://flagcdn.com/256x192/{c}.png')
    r.raise_for_status()
    # ignoring content for this example
```

```text
100%|█████████████████████████████████████████████████████████████| 306/306 [01:15<00:00,  3.77it/s]
```

One of the most widespread libraries for asynchronous web requests in `aiohttp` which syntax is somehow similar. The proper code would be here:

```python
import aiohttp
import time

async def fetch(code, session):
    async with session.get(f"https://flagcdn.com/256x192/{code}.png") as resp:
        return await resp.read()


async def main():
    t0 = time.time()
    async with aiohttp.ClientSession() as session:
        futures = [fetch(code, session) for code in codes]
        for response in await asyncio.gather(*futures):
            data = response
    print(f"done in {time.time() - t0:.5f}s")


asyncio.run(main())
```

```text
done in 0.52194s
```

<div class="alert alert-success">
<b>Note</b> &nbsp;&nbsp; This approach leads to a speedup of nearly 150. This significant speedup makes a particular sense here, with a lot of small blocking requests.
</div>

<div class="alert alert-warning">
<b>Warning</b> &nbsp;&nbsp; If you run this code behind a proxy, you may need to adjust the code.
<pre><code># with requests
requests.get(url, proxies={"http"=proxy, "https"=proxy})
# with aiohttp
async with session.get(url, proxy=proxy)
</code></pre>
</div>

### Exercice

We will implement a particular case of webcrawling in this example, with a breadth first exploration in a graph.

- Background: Queen Victoria is considered as the grandmother of Europe. She is the ancestor of many famous reigning people today. We will write a program to ask to find the relationship between cousins in this extended family. A first example could be to explore the genealogy of Queen Elizabeth II and the Duke of Edinburgh. Yes, they are extended cousins.

<img class="giphy" src="https://media.giphy.com/media/l0MYMoUUuLpsL9JTi/giphy.webp"/>

- We will use the Wikidata API to explore the structure of the relationship between pages. Based on the Wikipedia entry, you will find in the left panel a [Wikidata item](https://www.wikidata.org/wiki/Special:EntityPage/Q9439)

![wikidata](../assets/images/wikidata.png)

- Pick the final identifier in the URL (here `Q9439`) and replace it in the JSON URL

  |               | URL                                                                                                                        |
  | ------------- | -------------------------------------------------------------------------------------------------------------------------- |
  | Wikidata item | [https://www.wikidata.org/wiki/Special:EntityPage/Q9439](https://www.wikidata.org/wiki/Special:EntityPage/Q9439)           |
  | JSON file     | [https://www.wikidata.org/wiki/Special:EntityData/Q9439.json](https://www.wikidata.org/wiki/Special:EntityData/Q9439.json) |

  Explore the JSON and find specific relationships in the `claims` dictionary: `P22` for the "father" relationship, `P25` for the "mother" relationship and `P40` for the "children" relationship. Find new identifiers for members of extended family in those dictionaries.

- Explore the entries for all neighbours of the current entry. Pay attention to stick to _breadth-first_ exploration: explore all kins directly related to Queen Victoria, then all kins with two degrees of relationship, etc.

- Draw the genealogic subtree (consider the `networkx` package) with Queen Victoria, Queen Elizabeth II and the Duke of Edinburgh.

- Extend the graph with another grandfather of Europe, Christian IX of Denmark. The late British royal couple was also cousin through this branch. Look at their relationships with other cousins, like Nicholas II of Russia (the last tsar of Russia), or Felipe VI of Spain, current King of Spain.

You will find a suggestion of solution in the `asyncio.ipynb` notebook.

[↑ Home](.)
