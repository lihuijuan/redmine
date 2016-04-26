#!/usr/bin/python

from src import user
from src import ticket
from src import ticketHandler

def main():
    eId = 'exxxx'
    username = 'mmm'
    passsword = '*****'
    email = 'xx_xx@com.cn'
    tId = 'txxxx'
    title = 'tilte_description'

    author = User(eId, username, password, email)
    assignee = User(eId, username, password, email)
    ticket = Ticket(tId, title, author)
    ticketHandler = TicketHandler()

    ticketHandler.assign_ticket(ticket, assignee)
    ticketHandler.release_code(ticket, assignee)

if __name__ == '__main__':
    main()
