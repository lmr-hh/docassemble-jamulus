Liebe\*r Herr\*Frau ${ person.name.last },

vielen Dank für Ihre Anmeldung zum Projektchor "Deutschland singt!". Dies ist
eine automatische Bestätigung, dass wir Ihre Anmeldung empfangen haben.

Sie haben folgende Angaben gemacht:

|Feld          |Deine Angabe              |
|--------------|--------------------------|
|Name          | ${ person.name }         |
|Telefonnummer | ${ person.phone_number } |
|E-Mail        | ${ person.email }        |
|Adresse       | ${ adresse(person) }     |
|Stimmlage     | ${ stimmlage }           |

Sie haben außerdem angegeben, dass Sie zu folgenden Proben dabei sind:

% for date in daten["Probentermine"]:
<%
    the_id = None
    the_date = date
    help_text = None
    if isinstance(date, dict):
        the_date = date['date']
        the_id = date.get('id', None)
        help_text = date.get('help', None)
    elif isinstance(date, list):
        the_date = date[0]
        help_text = date[1]
    text = format_date(the_date, 'E, d. MMMM yyyy')
    if the_id is None:
        the_id = the_date
    if help_text:
        text += f", {help_text}" 
%>
% if probentermine.get(the_id, False):
- ${ text }
% endif
% endfor

% if anmerkungen.strip():
Sie haben außerdem folgende Angaben gemacht:
> ${ anmerkungen.replace('\n', '\n> ') }
% endif

Viele Grüße  
Der Landesmusikrat Hamburg
