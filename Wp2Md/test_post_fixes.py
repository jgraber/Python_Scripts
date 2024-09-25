import pytest
from transform_posts import cleanup_post

def test_fix_date():
    input = """
---
date: "2023-12-31"
---

# Happy new years eve!
"""

    expected = """
---
date: 2023-12-31
---

# Happy new years eve!
"""

    output = cleanup_post(input)
    assert expected == output


def test_fix_code():
    input = """
---
date: 2023-12-31
---

# Happy new years eve!
```
a = 1
b = 2
```
"""

    expected = """
---
date: 2023-12-31
---

# Happy new years eve!
``` py3
a = 1
b = 2
```
"""

    output = cleanup_post(input)
    assert expected == output


def test_fix_images():
    input = """
![Image title](images/dummy.png)
"""

    expected = """
![Image title](dummy.png)
"""

    output = cleanup_post(input)
    assert expected == output


def test_add_more():
    input = """
abc

This post is part of my journey to learn Python. You find the code for this post in my PythonFriday repository on GitHub.

"""

    expected = """
abc

<!-- more -->

"""

    output = cleanup_post(input)
    assert expected == output


def test_fix_title():
    input = """
---
title: "Python Friday #1: Let’s Learn Python"
---
This post is part ...

"""

    expected = """
---
title: "#1: Let’s Learn Python"
---
This post is part ...

"""

    output = cleanup_post(input)
    assert expected == output