from terminaltables import AsciiTable
from datetime import datetime
from pypeerassets import Deck


def tstamp_to_iso(tstamp):
    '''make iso timestamp from unix timestamp'''

    return datetime.fromtimestamp(tstamp).isoformat()


def print_table(title, heading, data):
    " prints a table to the terminal using terminaltables.AsciiTable "

    data = list(data)
    data.insert(0, heading)
    table = AsciiTable(data, title=title)
    print(table.table)


def deck_title(deck):
    return "Deck id: " + deck.id + " "


def deck_summary_line_item(deck):

    d = deck.__dict__
    return [d["id"],
            d["name"],
            d["issuer"],
            d["issue_mode"]
            ]


def print_deck_list(decks):
    '''Show summary of every deck'''

    print_table(
            title="Decks",
            heading=("ID", "asset name", "issuer", "mode"),
            data=map(deck_summary_line_item, decks))


def print_deck_info(deck: Deck):

    print_table(
            title=deck_title(deck),
            heading=("asset name", "issuer", "issue mode", "decimals", "issue time"),
            data=[[
                getattr(deck, attr) for attr in
                        ["name", "issuer", "issue_mode", "number_of_decimals", "issue_time"]]])