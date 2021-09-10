Liebe\*r Herr\*Frau ${ person.name.last },

vielen Dank für Ihre Anmeldung zum Projektchor "Deutschland singt!". Dies ist
eine automatische Bestätigung, dass wir Ihre Anmeldung empfangen haben.

Sie haben folgende Angaben gemacht:

|Feld          |Deine Angabe              |
|--------------|--------------------------|
|Name          | ${ person.name }         |
|Telefonnummer | ${ person.phone_number } |
|E-Mail        | ${ person.email }        |
|Adresse       | ${ adresse(person) }   |

Sie haben außerdem angegeben, dass Sie zu folgenden Proben dabei sind:

% for date in daten["Probentermine"]:
<%
    the_date = date[0] if isinstance(date, list) else date
    text = format_date(the_date, 'E, d. MMMM yyyy')
    if isinstance(date, list):
        text += " (" + date[1] + ")" 
%>
% if probentermine.get(the_date, False):
- ${ text }
% endif
% endfor

Sie haben außerdem folgende Angaben gemacht:
> ${ anmerkungen }

Viele Grüße  
Der Landesmusikrat Hamburg
