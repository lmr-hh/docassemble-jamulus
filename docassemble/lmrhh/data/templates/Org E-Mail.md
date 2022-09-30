Hallo,

% if attending:
Ihre Organisation ${ organization.name.text } wurde zur Mitgliederversammlung des
Landesmusikrates Hamburg angemeldet und wird vertreten durch:

% for person in persons:
- ${ person.name } ${ '(Stimmberechtigt)' if person == voter else '' }
% endfor

% else:
Schade, dass Ihre Organisation ${ organization.name.text } nicht auf der
Mitgliederversammlung des Landesmusikrates Hamburg vertreten sein wird.
Sollten Sie doch einen Vertreter zur Versammlung schicken wollen, können Sie die
Anmeldung einfach erneut ausfüllen.
% endif

**Mitgliederversammlung des Landesmusikrates Hamburg**  
Staatliche Jugendmusikschule Hamburg, Aula  
Mittelweg 42, 20148 Hamburg  
Beginn: 22.11.2022, 17:30 Uhr

Viele Grüße  
Der Landesmusikrat Hamburg
