from docassemble.base.functions import value
from docassemble.base.util import format_date, validation_error, Address, Person

__all__ = ["adresse", "date_checklist", "dates_review"]


def adresse(thing):
    """
    Gibt eine formatierte Postadresse zurück.
    """
    if isinstance(thing, str):
        return thing
    if isinstance(thing, Person):
        address = thing.address
    elif isinstance(thing, Address):
        address = thing
    else:
        raise ValueError(f"Cannot format object of type {type(thing)}")
    components = []
    if getattr(address, "route", None) and getattr(address, "street_number",
                                                   None):
        components.append(f"{address.route} {address.street_number}")
    elif getattr(address, "route", None):
        components.append(address.route)
    elif address.address:
        components.append(address.address)
    city_components = []
    if getattr(address, "zip", None):
        city_components.append(str(int(address.zip)))
    if getattr(address, "city", None):
        city_components.append(address.city)
    components.append(" ".join(city_components))
    return ", ".join(components)


def date_checklist(dates: dict, help_format=None, default=True):
    """
    Formats a list of checkbox entries to select dates from the given list.
    """
    checklist = []
    for date in dates:
        if isinstance(date, dict):
            date_id = date.get('id', date['date'])
            value = {
                date_id: format_date(date['date'], 'E, d. MMMM'),
                'default': default
            }
            if help_format and 'help' in date:
                value[date_id] += help_format % date['help']
            checklist.append(value)
        elif isinstance(date, list) and help_format is None:
            checklist.append({
                date[0]: format_date(date[0], 'E, d. MMMM'),
                'default': default,
                'help': date[1]
            })
        elif isinstance(date, list):
            checklist.append({
                date[0]: format_date(date[0], 'E, d. MMMM') +
                         (help_format % date[1]),
                'default': default
            })
        else:
            checklist.append({
                date: format_date(date, 'E, d. MMMM'),
                'default': default
            })
    return checklist


def dates_review(dates: dict, selections: dict, help_format=None):
    """
    Erstellt eine Liste von Terminen, in denen Fehltermine gekennzeichnet sind.
    Das Ergebnis kann dem Benutzer angezeigt werden.
    """
    output = ""
    for date in dates:
        the_date = date
        help_text = None
        date_id = None
        if isinstance(date, dict):
            the_date = date['date']
            date_id = date.get('id', None)
            help_text = date.get('help', None)
        elif isinstance(date, list):
            the_date = date[0]
            help_text = date[1]
        if date_id is None:
            date_id = the_date
        text = format_date(the_date, 'E, d. MMMM yyyy')
        if help_text is not None and help_format:
            text += help_format % help_text
        if selections.get(date_id, False):
            output += "- " + text + "\n"
        else:
            output += '- <span style="color: red; ' \
                      'text-decoration: line-through">' + text + '</span>\n'
    return output
