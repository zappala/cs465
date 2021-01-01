# CS 465 Website

This system is built on Python using Flask for static web pages. It
has a variety of quirks but it works well.

## Setting up your environment

These instructions assume you are running MacOS.

First, install pipenv:

```
brew install pipenv
```

Next, install the dependencies for this project:

```
pipenv install --three
```

## Running a development environment

Run a development web server:

```
pipenv run python app.py
```

This will start a server at `localhost:8080`, which you can visit in
your browser.

## Adding a new semester

1. Create a new schedule in `views/fallXXXX.py` or `views/winterXXXX.py`.

   The easiest way to do this is by copying a schedule from a previous
   semester. Be sure to replace any instances of, e.g., `fall-2019`,
   with the new semester name.

2. Import the new schedule into `app.py`.

3. Create a new directory in `templates` for the new semester, named
`templates/fall-XXXX.py` or `templates/winter-XXXX.py`.

4. Link to the new semester in `templates/index.html`

## Editing the Schedule

The schedule uses the following commands:

```
s = Schedule()
```

Creates an instance of a new schedule for the semester

```
s.week()
```

Creates a new week.

```
d = s.day("January 8")
```

Creates a new day, with the given date.

```
d.lecture("Name of lecture")
```

Indicates the topic for the day.

```
d.slide("Name",link)
```

Links to slides that will be presented that day. The slides should be stored in `static/lectures`. The link is optional.

```
d.reading("Name",link)
```

Links to readings for that day. Typically these are links to external
resources, but some may be stored in `static/pubs`. The link is optional.

```
d.assignment("Name",link)
```

Links to an assignment. Assignments should be in `template/semester-XXXX`.
The link is optional.

## Editing other pages

All other pages are static HTML or Markdown, written in the `template`
directory. Inside of `template/semester-XXXX`, you should have:

### menu.html

This defines the menu for your semester. It should have a statement
at the top:

```
{% extends "base.html" %}
```

that indicates it extends the base HTML template. Then there are sections for several blocks:

```
{% block term %}
Winter 2019
{% endblock %}
```

Define your term here.

```
{% block section %}
Section 1: TTh 3:00pm - 4:15pm 2113 JKB
{% endblock %}
```

Define the sections here.

```
{% block menu %}
{% endblock %}
```

Define your menu here. See an example from a previous semester for
details.  The easiest thing to do is to copy it from a previous
semester and then modify for your needs.

### index.html

This is the home page for your semester. You should have:

```
{% block page %}
{% endblock %}
```

for the main content of the page.

Inside of this block, you can use HTML, or you can use:

```
{% filter markdown %}
{% endfilter %}
```

to use Markdown syntax.

### schedule.html

This renders the schedule from the `view` you defined. Copy one from a
previous semester and change the top line indicating the menu it
extends.

### help

This directory contains files such as contact info for the instructor
and office hours.

### homework

This directory contains homework assignments.

### projects

This directory contains project assignments.

## Deploying

When you want to deploy the site, edit `dodo.py` and change the login
information to use your username. You may be able to do this by
uncommenting the right line. Then run:

```
pipenv run doit
```
