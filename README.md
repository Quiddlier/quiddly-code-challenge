Invoice Payment Tracker
=======================

This is a small python dev test from the team at Quiddly!

## User Story

Jane Doe works at Company Alpha.
Company Alpha sends out paper-invoices by mail to their customers and Jane Dow gets post-it notes with a list of the 
payments the company has received from the accounting department.
On the post-it is the id of the invoice, and the amount of money transferred.
Jane prints two copies of every invoice and sticks post-it notes on the invoice they belong too - when an invoice is
paid in full it is filed away. Naturally, Jane loves this ingenious system!

But one day Jane got a new boss John Doe (no relation) who on his first day forbid her from printing two copies of
each invoice, complaining about the need to modernize operations. 
John requested that Jane have a digital record of invoices and payments and hires in a consultant to help get it done.

## Task

This is where you come in! You are the consultant.
In this project there is a small flask app with flask_restx. It is incomplete.
In the app one can create invoices but there is no functionality to register payments.
Assume that Jane will continue getting her post-it notes of payments and that she logs invoices with existing
functionality.

No need for a front end, Jane's never really made the move to GUIs, she is a flawless pro on the CLI
and her favorite tool is cURL.
Continue writing on this app to allow Jane to post in a payments and see which invoices are paid and not.

The purpose of this application is for Jane to be able to keep track of the invoices they have sent, and by matching
it to received payments see if they are paid in full or not.

## Time Investment

This is an open-ended task. You are free to add (or remove) as much as you want. 
We value your time, so it's totally fine if you just invest an hour.
But to set a max for any over-achievers out there, please spend **no more than 3 hours** on this task.
We are **not expecting a production ready app**, send up what you got.
Include a note on time invested in the `SOLUTION.md` file.

## Purpose: What we are looking for

First, obviously we want to check that you possess the necessary base prerequisite knowledge.
We expect this task to be easy to you unless explicitly joining as a junior developer.
We want to see that you solve the issue at hand in a clear and concise way.
If you want to throw in more - please feel free to show off your skills :)
In such cases, it is important you add notes about what you are doing and why.

## How to submit

Your solution should contain the relevant code changes for us to test your solution.
Please also add some notes about what you have done, time invested, and anything else you think may be relevant 
in `SOLUTION.md`.

When you are done add a new branch with your solution using your initials in the  branch name following the naming
convention: `<your initals>-test` e.g. `mo-test`. Compress the project folder and send it  to your contact 
at Quiddly.

## First steps

[Quick start](https://flask.palletsprojects.com/en/2.2.x/quickstart/) and
[installation](https://flask.palletsprojects.com/en/2.2.x/installation/)
are available as part of the flask documentation.
To save some time, assuming you are in a Linux or Mac environment and have a python version of at least 3.7,
run the following to run a development server on port 5000.

* `python3 -m venv venv`
* `. venv/bin/activate`
* `pip install -r requirements.txt`
* `flask run` || `python3 app.py`

Good luck and have fun!
