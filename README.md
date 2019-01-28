# Data Mailing

## Inspiration
With 74 trillion messages sent each year, it hard to think of a means of communication more widely used that emails. Yet, most of those are spammy and the email client haven't evolved as much as the rest of the tech industry over the years. As a result, everyone has grown to hate their mailbox, being overwhelmed by useless emails and not finding relevant information quickly when needed.

## What it does
In an attempt to challenge this status quo, we developed data mailing, a webapp mining your GMail data to deliver you a clean, categorised and well organised subset of relevant information standing out from the many gigabytes of your mailbox. Our product applies two filters on the user's emails, one to select only emails of interest (events, plane, train and coach tickets, receipts, vouchers and promocodes, confirmation links and job applications follow-ups) and the other one to extract only relevant information from the selected emails. This relevant information and this information only is then stored in a database. This data can then be accessed in via a user-friendly webapp in which it is listed in the different categories our proprietary algorithms identified.

## How we built it
Our backend interface with GMail and filtering infrastructure are built in Python, which several processes running in parallel to mine the email data in an efficient manner and the resulting data is stored in an sqlite database. Finally, our backend relies on Python with Django and our front-end on the fast, modern and scalable Vue.js.

## Challenges we ran into
We encountered several challenges throughout the hackathon, the most important ones being:
- Learning new languages on the fly by going through tens of pages of documentation at 5am
- Efficiently identifying relevant emails and relevant information within emails.
- Connecting to the extremely poorly documented GMail API.
- Debugging an issue due to some processes failing silently.
- Handling large attachments such as plane tickets.

## Accomplishments that we're proud of
- Developing a new modern webapp in an environment as old as emails.
- Designing data efficient algorithms to filter relevant data from emails and filter out spams.

## What we learned
- Vue.js
- The standard used to indicate the purpose of email used by some companies

## What's next for Data Mailing
-Scaling to support more categories
-Extending our support to other mail clients than GMail
-Improving the accuracy of our filtering algorithms

## Running Instructions
To run the server

```bash
make
```

To create a superuser in django

```bash
python manage.py createsuperuser
```

To enable SECRET_KEY and DEBUG_ENABLE

```bash
export DEBUG_ENABLE='TRUE'
export SECRET_KEY="password"
```

To install requirements

```bash
pip install -r requirements.txt
```

Admin site django http://localhost:8000/admin

To generate the table processedemail of the db launch http://localhost:8000/
