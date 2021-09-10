<div class="alert alert-info" role="alert">
  <h5 class="alert-heading">Testmodus</h5>

  Die Anmeldung befindet sich im Testmodus. Daher werden keine E-Mails
  verschickt und auch keine weiteren Automatisierungen vorgenommen. Dies ist nur
  eine Zusammenfassung der Automatisierung, die bei einer echten Anmeldung
  ablaufen würde.
</div>

### Begrüßungs-E-Mail
Eine E-Mail würde an `${ person.email }` geschickt werden.
Der Text der E-Mail kann unten angesehen werden. Das Design der
E-Mail sieht allerdings anders aus.

<p>
  <%self:collapse_button id="person-email-collapse">
    E-Mail-Inhalt anzeigen
  </%self:collapse_button>
  <%self:action_button action="send_member_email"
                       message="Die E-Mail wurde gesendet. Es kann einen Moment dauern, bis die Mail ankommt.">
    E-Mail trotzdem senden
  </%self:action_button>
</p>

<%self:collapse id="person-email-collapse" title="${ person_email.subject }">
${ person_email }
</%self:collapse>

### Benachrichtigungs-E-Mail
Bei jeder Anmeldung werden bestimmte Empfänger benachrichtigt.
% if not daten["E-Mail Benachrichtigung"]:
Es sind bisher keine Empfänger konfiguriert, daher würde dieser Schritt
übersprungen werden.
% else:
Folgende Empfänger werden benachrichtigt:

% for email in daten["E-Mail Benachrichtigung"]:
  - `${ email }`
% endfor

Wenn du unten auf "E-Mail trotzdem senden" klickst, wird die E-Mail im Testmodus
nur an die von dir angegebene Adresse `${ person.email }` gesendet.

<p>
  <%self:collapse_button id="orga-email-collapse">
    E-Mail-Inhalt anzeigen
  </%self:collapse_button>
  <%self:action_button action="send_orga_email"
                       message="Die E-Mail wurde gesendet. Es kann einen Moment dauern, bis die E-Mail ankommt.">
    E-Mail trotzdem senden
  </%self:action_button>
</p>

<%self:collapse id="orga-email-collapse" title="${ orga_email.subject }">
${ orga_email }
</%self:collapse>
% endif

### Anmeldeliste
Alle eingegebenen Daten werden automatisch zur Anmeldeliste hinzugefügt. Die
Anmeldeliste ist ein Excel-Dokument mit der ID
`${ daten["Anmeldungen"]["Dokument"] }`. Die Daten werden dort der Tabelle
`${ daten["Anmeldungen"]["Tabelle"] }` hinzugefügt. Überschriften werden
automatisch erkannt und den Einträgen zugeordnet.

${ check_table(test_anmeldungen_tabelle) }

<p>
  <%self:action_button action="append_to_table"
                       drive="${ daten["Anmeldungen"]["Bibliothek"] }"
                       file="${ daten["Anmeldungen"]["Dokument"] }"
                       table="${ daten["Anmeldungen"]["Tabelle"] }
                       message="Die Daten wurden zur Anmeldeliste hinzugefügt.">
    Zur Tabelle hinzufügen
  </%self:action_button>
  <a class="btn btn-secondary btn-sm"
     target="_blank"
     href="${ test_anmeldungen_tabelle['file']['webUrl'] }">Tabelle öffnen</a>
</p>
