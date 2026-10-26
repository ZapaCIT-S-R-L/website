#!/usr/bin/env python3
"""Builds the static zapakid.ro site: landing, contact and privacy in RO (/), DE (/de/) and EN (/en/).

Edit the texts below, run `python3 build.py`, commit the generated .html files with it.
When the apps are published, set APP_STORE / GOOGLE_PLAY and rebuild: the buttons become links.
"""
from html import escape
from pathlib import Path

ROOT = Path(__file__).parent
APP_STORE = ""     # e.g. https://apps.apple.com/app/id...
GOOGLE_PLAY = ""   # e.g. https://play.google.com/store/apps/details?id=...
EMAIL = "contact@zapakid.ro"
PHONE = {"ro": "0770 972 972", "de": "+40 770 972 972", "en": "+40 770 972 972"}
LANGS = {"ro": "/", "de": "/de/", "en": "/en/"}

APPLE_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M16.4 12.6c0-2.6 2.1-3.8 2.2-3.9-1.2-1.8-3.1-2-3.7-2-1.6-.2-3.1.9-3.9.9-.8 0-2-.9-3.4-.9-1.7 0-3.3 1-4.2 2.6-1.8 3.1-.5 7.7 1.3 10.2.9 1.2 1.9 2.6 3.2 2.6 1.3-.1 1.8-.8 3.3-.8s2 .8 3.4.8c1.4 0 2.3-1.3 3.1-2.5 1-1.4 1.4-2.8 1.4-2.9-.1 0-2.7-1-2.7-4.1zM13.9 5c.7-.9 1.2-2 1-3.2-1 .1-2.2.7-3 1.5-.6.7-1.2 1.9-1.1 3.1 1.2.1 2.3-.6 3.1-1.4z"/></svg>'
PLAY_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 2.6c-.3.3-.4.7-.4 1.2v16.4c0 .5.1.9.4 1.2l9.3-9.4L4 2.6zm10.4 10.5 2.6 2.6-11 6.3 8.4-8.9zm3.9-3.8 2.9 1.7c.9.5.9 1.4 0 1.9l-2.9 1.7-2.8-2.7 2.8-2.6zM6 1.9l11 6.3-2.6 2.6L6 1.9z"/></svg>'

T = {
    "ro": {
        "html_lang": "ro",
        "title": "ZapaKid — Ajutorul de teme cu robotel, pentru toată familia",
        "desc": "ZapaKid: tutore AI care vorbește cu copilul în română, germană sau engleză, teme din poză, teste, jocuri pentru care se câștigă monede la învățat și chat de familie criptat. În curând pe App Store și Google Play.",
        "nav_contact": "Contact", "nav_privacy": "Confidențialitate",
        "h1": "Învățatul, <span>cu un robotel prieten.</span>",
        "lead": "ZapaKid îl ajută pe copil la teme, îi explică pe înțelesul lui și vorbește cu el în română, germană sau engleză. Exersează, câștigă monede și se joacă — iar părinții rămân aproape, printr-un chat de familie criptat.",
        "dl": "Disponibil pe", "soon": "În curând",
        "signin": "Conectare doar cu Apple sau Google — fără parole, fără conturi noi de reținut.",
        "feat_h": "Ce găsești în ZapaKid",
        "features": [
            ("🤖", "Tutore AI cu voce", "Copilul întreabă cu vocea, robotelul răspunde cu vocea, potrivit clasei lui: de la grădiniță la clasa a VIII-a."),
            ("📷", "Teme din poză", "O poză cu exercițiul și robotelul îl ia pas cu pas — explică, nu doar dă răspunsul."),
            ("✏️", "Teste și exerciții", "Exerciții pe clasă și teste care se deblochează pe rând, în ritmul copilului."),
            ("🎮", "Jocuri cu monede", "Monedele câștigate la învățat deschid jocurile: șah cu roboți, blocuri, sudoku, curse și altele."),
            ("💬", "Chat de familie", "Părinții și copiii vorbesc, fiecare în limba lui, cu traducere automată. Mesajele sunt criptate end-to-end."),
            ("🔒", "Controlul părinților", "Părintele asociază telefonul copilului cu un cod QR și stabilește clasa, limbile și regulile."),
        ],
        "band": [
            ("Pentru copii de la grădiniță la clasa a VIII-a", "Totul se adaptează clasei: cuvinte simple pentru cei mici, explicații mai bogate pentru cei mari."),
            ("Fără reclame, fără urmărire", "Nu vindem date și nu afișăm reclame. Site-ul nu folosește cookie-uri."),
        ],
        "contact_title": "Contact",
        "contact_intro": "Ai o întrebare despre ZapaKid, o idee sau o problemă? Scrie-ne, răspundem de obicei în 1–2 zile lucrătoare.",
        "contact_privacy": "Pentru cereri legate de datele personale (acces, ștergere etc.) folosește aceeași adresă și menționează „Date personale” în subiect.",
        "company_h": "Firma",
        "privacy_title": "Politica de confidențialitate",
        "updated": "Ultima actualizare: 19 octombrie 2026",
        "privacy": [
            ("Cine suntem", ["ZapaKid este un produs al <b>Zapacit S.R.L.</b>, Str. Zambilei nr. 76, Ghimbav 507075, județul Brașov, România, J2020002568087, CUI RO43395664 („noi”), operator al datelor personale descrise aici, conform Regulamentului (UE) 2016/679 (GDPR). Contact: <a href=\"mailto:contact@zapakid.ro\">contact@zapakid.ro</a>."]),
            ("Site-ul zapakid.ro", ["Site-ul este doar o pagină de prezentare. Nu are conturi, formulare, cookie-uri sau instrumente de analiză și nu încarcă resurse de la terți. Serverul web înregistrează temporar, din motive de securitate, adresa IP, data și pagina cerută."]),
            ("Contul în aplicație: doar Apple sau Google", [
                "Contul de părinte se creează exclusiv prin <b>Sign in with Apple</b> sau <b>Sign in with Google</b>. Nu avem parole. Primim de la Apple/Google un identificator unic al contului și, la prima conectare, numele și adresa de email (la Apple poate fi o adresă de redirecționare).",
                "Verificarea vârstei: aplicația cere telefonului doar confirmarea că părintele are cel puțin 18 ani; nu primim data nașterii. Dacă vârsta nu poate fi confirmată, aplicația nu creează un cont.",
                "Copiii nu își creează singuri cont: telefonul copilului funcționează doar după ce un părinte scanează codul QR și setează profilul copilului (prenume, vârstă, clasă, limbi).",
            ]),
            ("Chaturile și notițele familiei", [
                "Mesajele, fișierele atașate și notițele sunt <b>criptate end-to-end</b> pe telefon (AES-256-GCM, cheile rămân pe dispozitivele familiei). Serverele noastre stochează doar datele criptate și nu le pot citi.",
                "Traducerea se face pe telefon când sistemul o permite. Pentru limbile pe care telefonul nu le poate traduce (de exemplu româna), textul mesajului este trimis criptat (HTTPS) prin serverul nostru către Google pentru traducere; nu îl stocăm.",
                "Pentru notificări folosim serviciile Apple (APNs) și Google; pentru aceasta păstrăm un identificator de notificare al telefonului.",
            ]),
            ("Funcțiile AI (tutore, voce, poze, teste)", [
                "Întrebările copilului, pozele trimise (teme, cub Rubik, orar) și textele citite cu voce sunt trimise prin serverul nostru către <b>Google Cloud (Vertex AI, Gemini)</b>, care acționează ca persoană împuternicită. Nu trimitem numele, emailul sau alte date de identificare și nu stocăm acest conținut pe serverele noastre. Conform condițiilor Google Cloud, Google nu folosește aceste date pentru antrenarea modelelor.",
                "Istoricul conversațiilor cu tutorele rămâne pe telefon.",
            ]),
            ("Unde sunt datele și cui le transmitem", [
                "Datele sunt stocate pe servere proprii, administrate de echipa noastră, în România (UE). Pentru livrarea rapidă și sigură a site-ului și a aplicației (DNS, rețea de distribuție a conținutului, protecție împotriva atacurilor) colaborăm cu <b>Cloudflare</b>: traficul trece criptat prin rețeaua Cloudflare, dar datele contului și conținutul familiei rămân stocate exclusiv pe serverele noastre. Persoane împuternicite: Cloudflare (livrare și protecție), Google (conectare, AI, traducere, notificări), Apple (conectare, verificarea vârstei, notificări). Când acești parteneri prelucrează date în afara UE, transferul se face în baza garanțiilor prevăzute de GDPR (Cadrul UE–SUA privind protecția datelor sau clauze contractuale standard). Datele pot fi transmise autorităților doar când legea o cere.",
                "Nu vindem date, nu afișăm reclame și nu facem profilare.",
            ]),
            ("Cât timp păstrăm datele", ["Datele contului se păstrează cât timp există contul. Părintele poate șterge oricând toate datele familiei din aplicație (contul 👤 → „Șterge toate datele familiei”): mesajele, profilurile copiilor și sesiunile se șterg imediat. Copiile de siguranță se șterg după cel mult 90 de zile."]),
            ("Temeiul legal și copiii", ["Prelucrăm datele pentru a furniza serviciul cerut (executarea contractului, art. 6(1)(b) GDPR) și pentru securitate (interes legitim, art. 6(1)(f)). Datele copiilor sunt prelucrate cu acordul și sub controlul părintelui sau tutorelui legal (art. 8 GDPR)."]),
            ("Drepturile tale", ["Ai dreptul de acces, rectificare, ștergere, restricționare, portabilitate și opoziție. Scrie-ne la <a href=\"mailto:contact@zapakid.ro\">contact@zapakid.ro</a>. Poți depune plângere la Autoritatea Națională de Supraveghere a Prelucrării Datelor cu Caracter Personal (ANSPDCP, <a href=\"https://www.dataprotection.ro\">dataprotection.ro</a>)."]),
            ("Modificări", ["Când schimbăm această politică, actualizăm data de mai sus; schimbările importante le anunțăm și în aplicație."]),
        ],
    },
    "de": {
        "html_lang": "de",
        "title": "ZapaKid — Hausaufgabenhilfe mit Roboter, für die ganze Familie",
        "desc": "ZapaKid: KI-Tutor, der mit deinem Kind Deutsch, Rumänisch oder Englisch spricht, Hausaufgaben per Foto, Tests, Spiele, für die man beim Lernen Münzen verdient, und ein verschlüsselter Familienchat. Bald im App Store und bei Google Play.",
        "nav_contact": "Kontakt", "nav_privacy": "Datenschutz",
        "h1": "Lernen, <span>mit einem Roboter-Freund.</span>",
        "lead": "ZapaKid hilft deinem Kind bei den Hausaufgaben, erklärt alles kindgerecht und spricht Deutsch, Rumänisch oder Englisch. Üben, Münzen verdienen, spielen — und die Eltern bleiben über einen verschlüsselten Familienchat in der Nähe.",
        "dl": "Erhältlich im", "soon": "Bald",
        "signin": "Anmeldung nur mit Apple oder Google — keine Passwörter, kein neues Konto zum Merken.",
        "feat_h": "Was ZapaKid kann",
        "features": [
            ("🤖", "KI-Tutor mit Stimme", "Dein Kind fragt per Sprache, der Roboter antwortet per Sprache, passend zur Klasse: vom Kindergarten bis Klasse 8."),
            ("📷", "Hausaufgaben per Foto", "Ein Foto der Aufgabe, und der Roboter geht sie Schritt für Schritt durch — er erklärt, statt nur die Lösung zu verraten."),
            ("✏️", "Tests und Übungen", "Übungen pro Klasse und Tests, die nacheinander freigeschaltet werden, im Tempo des Kindes."),
            ("🎮", "Spiele mit Münzen", "Beim Lernen verdiente Münzen öffnen die Spiele: Roboter-Schach, Blöcke, Sudoku, Rennen und mehr."),
            ("💬", "Familienchat", "Eltern und Kinder schreiben sich, jeder in seiner Sprache, mit automatischer Übersetzung. Ende-zu-Ende-verschlüsselt."),
            ("🔒", "Eltern haben die Kontrolle", "Eltern verbinden das Handy des Kindes per QR-Code und legen Klasse, Sprachen und Regeln fest."),
        ],
        "band": [
            ("Für Kinder vom Kindergarten bis Klasse 8", "Alles passt sich der Klasse an: einfache Worte für die Kleinen, ausführlichere Erklärungen für die Großen."),
            ("Keine Werbung, kein Tracking", "Wir verkaufen keine Daten und zeigen keine Werbung. Die Website verwendet keine Cookies."),
        ],
        "contact_title": "Kontakt",
        "contact_intro": "Eine Frage zu ZapaKid, eine Idee oder ein Problem? Schreib uns, wir antworten meist innerhalb von 1–2 Werktagen.",
        "contact_privacy": "Für Anfragen zu personenbezogenen Daten (Auskunft, Löschung usw.) nutze dieselbe Adresse mit dem Betreff „Datenschutz“.",
        "company_h": "Unternehmen",
        "privacy_title": "Datenschutzerklärung",
        "updated": "Zuletzt aktualisiert: 19. Oktober 2026",
        "privacy": [
            ("Wer wir sind", ["ZapaKid ist ein Produkt der <b>Zapacit S.R.L.</b>, Str. Zambilei nr. 76, 507075 Ghimbav, Kreis Brașov, Rumänien, J2020002568087, USt-IdNr. RO43395664 („wir“), Verantwortlicher für die hier beschriebenen personenbezogenen Daten gemäß Verordnung (EU) 2016/679 (DSGVO). Kontakt: <a href=\"mailto:contact@zapakid.ro\">contact@zapakid.ro</a>."]),
            ("Die Website zapakid.ro", ["Die Website ist nur eine Vorstellungsseite. Sie hat keine Konten, Formulare, Cookies oder Analysewerkzeuge und lädt keine Inhalte von Dritten. Der Webserver speichert aus Sicherheitsgründen vorübergehend IP-Adresse, Zeitpunkt und aufgerufene Seite."]),
            ("Das Konto in der App: nur Apple oder Google", [
                "Ein Elternkonto wird ausschließlich mit <b>Mit Apple anmelden</b> oder <b>Mit Google anmelden</b> erstellt. Wir haben keine Passwörter. Wir erhalten von Apple/Google eine eindeutige Kontokennung und bei der ersten Anmeldung Name und E-Mail-Adresse (bei Apple ggf. eine Weiterleitungsadresse).",
                "Altersprüfung: Die App fragt das Handy nur, ob der Elternteil mindestens 18 Jahre alt ist; das Geburtsdatum erhalten wir nicht. Kann das Alter nicht bestätigt werden, wird kein Konto erstellt.",
                "Kinder erstellen kein eigenes Konto: Das Handy des Kindes funktioniert erst, wenn ein Elternteil den QR-Code scannt und das Profil des Kindes festlegt (Vorname, Alter, Klasse, Sprachen).",
            ]),
            ("Chats und Notizen der Familie", [
                "Nachrichten, Anhänge und Notizen sind auf dem Handy <b>Ende-zu-Ende-verschlüsselt</b> (AES-256-GCM, die Schlüssel bleiben auf den Geräten der Familie). Unsere Server speichern nur verschlüsselte Daten und können sie nicht lesen.",
                "Übersetzt wird auf dem Handy, wenn das System es unterstützt. Für Sprachen, die das Handy nicht übersetzen kann (z. B. Rumänisch), wird der Nachrichtentext verschlüsselt (HTTPS) über unseren Server zur Übersetzung an Google gesendet; wir speichern ihn nicht.",
                "Für Benachrichtigungen nutzen wir die Dienste von Apple (APNs) und Google; dafür speichern wir eine Benachrichtigungskennung des Handys.",
            ]),
            ("KI-Funktionen (Tutor, Stimme, Fotos, Tests)", [
                "Die Fragen des Kindes, gesendete Fotos (Hausaufgaben, Zauberwürfel, Stundenplan) und vorgelesene Texte werden über unseren Server an <b>Google Cloud (Vertex AI, Gemini)</b> als Auftragsverarbeiter gesendet. Wir senden weder Namen noch E-Mail oder andere Identifikationsdaten und speichern diese Inhalte nicht auf unseren Servern. Gemäß den Bedingungen von Google Cloud verwendet Google diese Daten nicht zum Trainieren von Modellen.",
                "Der Gesprächsverlauf mit dem Tutor bleibt auf dem Handy.",
            ]),
            ("Wo die Daten liegen und an wen wir sie weitergeben", [
                "Die Daten werden auf eigenen, von unserem Team betriebenen Servern in Rumänien (EU) gespeichert. Für eine schnelle und sichere Auslieferung von Website und App (DNS, Content-Delivery-Netzwerk, Schutz vor Angriffen) arbeiten wir mit <b>Cloudflare</b> zusammen: Der Datenverkehr läuft verschlüsselt über das Cloudflare-Netzwerk, Kontodaten und Familieninhalte bleiben jedoch ausschließlich auf unseren Servern gespeichert. Auftragsverarbeiter: Cloudflare (Auslieferung und Schutz), Google (Anmeldung, KI, Übersetzung, Benachrichtigungen), Apple (Anmeldung, Altersprüfung, Benachrichtigungen). Verarbeiten diese Partner Daten außerhalb der EU, erfolgt die Übermittlung auf Grundlage der Garantien der DSGVO (EU-US Data Privacy Framework oder Standardvertragsklauseln). An Behörden geben wir Daten nur weiter, wenn das Gesetz es verlangt.",
                "Wir verkaufen keine Daten, zeigen keine Werbung und erstellen keine Profile.",
            ]),
            ("Speicherdauer", ["Kontodaten speichern wir, solange das Konto besteht. Eltern können jederzeit alle Familiendaten in der App löschen (Konto 👤 → „Alle Familiendaten löschen“): Nachrichten, Kinderprofile und Sitzungen werden sofort gelöscht. Sicherungskopien werden nach spätestens 90 Tagen gelöscht."]),
            ("Rechtsgrundlage und Kinder", ["Wir verarbeiten die Daten, um den gewünschten Dienst zu erbringen (Vertragserfüllung, Art. 6 Abs. 1 lit. b DSGVO), und für die Sicherheit (berechtigtes Interesse, Art. 6 Abs. 1 lit. f). Daten von Kindern werden mit Zustimmung und unter Kontrolle der Eltern bzw. Erziehungsberechtigten verarbeitet (Art. 8 DSGVO)."]),
            ("Deine Rechte", ["Du hast das Recht auf Auskunft, Berichtigung, Löschung, Einschränkung, Datenübertragbarkeit und Widerspruch. Schreib uns an <a href=\"mailto:contact@zapakid.ro\">contact@zapakid.ro</a>. Du kannst dich bei der rumänischen Datenschutzbehörde (ANSPDCP, <a href=\"https://www.dataprotection.ro\">dataprotection.ro</a>) oder der Aufsichtsbehörde deines Landes beschweren."]),
            ("Änderungen", ["Wenn wir diese Erklärung ändern, aktualisieren wir das Datum oben; wichtige Änderungen kündigen wir auch in der App an."]),
        ],
    },
    "en": {
        "html_lang": "en",
        "title": "ZapaKid — Homework help with a robot friend, for the whole family",
        "desc": "ZapaKid: an AI tutor that talks with your child in English, German or Romanian, homework from a photo, tests, games unlocked with coins earned by learning, and an encrypted family chat. Coming soon to the App Store and Google Play.",
        "nav_contact": "Contact", "nav_privacy": "Privacy",
        "h1": "Learning, <span>with a robot friend.</span>",
        "lead": "ZapaKid helps your child with homework, explains things in words they understand, and speaks English, German or Romanian. Practise, earn coins, play — while parents stay close through an encrypted family chat.",
        "dl": "Get it on", "soon": "Soon",
        "signin": "Sign in with Apple or Google only — no passwords, no new account to remember.",
        "feat_h": "What's inside ZapaKid",
        "features": [
            ("🤖", "AI tutor with a voice", "Your child asks out loud and the robot answers out loud, at their grade level: from kindergarten to grade 8."),
            ("📷", "Homework from a photo", "Snap the exercise and the robot works through it step by step — it explains rather than just giving the answer."),
            ("✏️", "Tests and practice", "Practice for every grade and tests that unlock one by one, at your child's pace."),
            ("🎮", "Games with coins", "Coins earned by learning unlock the games: robot chess, blocks, sudoku, racing and more."),
            ("💬", "Family chat", "Parents and kids talk, each in their own language, with automatic translation. End-to-end encrypted."),
            ("🔒", "Parents in control", "Parents pair the child's phone with a QR code and set the grade, languages and rules."),
        ],
        "band": [
            ("For kids from kindergarten to grade 8", "Everything adapts to the grade: simple words for the little ones, richer explanations for older kids."),
            ("No ads, no tracking", "We don't sell data or show ads. This website uses no cookies."),
        ],
        "contact_title": "Contact",
        "contact_intro": "A question about ZapaKid, an idea or a problem? Write to us; we usually reply within 1–2 working days.",
        "contact_privacy": "For personal-data requests (access, deletion and so on) use the same address with “Personal data” in the subject.",
        "company_h": "Company",
        "privacy_title": "Privacy policy",
        "updated": "Last updated: 19 October 2026",
        "privacy": [
            ("Who we are", ["ZapaKid is a product of <b>Zapacit S.R.L.</b>, Str. Zambilei nr. 76, Ghimbav 507075, Brașov County, Romania, J2020002568087, VAT RO43395664 (“we”), the controller of the personal data described here under Regulation (EU) 2016/679 (GDPR). Contact: <a href=\"mailto:contact@zapakid.ro\">contact@zapakid.ro</a>."]),
            ("The zapakid.ro website", ["The website is only a presentation page. It has no accounts, forms, cookies or analytics and loads nothing from third parties. For security, the web server temporarily logs the IP address, time and page requested."]),
            ("Your account in the app: Apple or Google only", [
                "A parent account is created only with <b>Sign in with Apple</b> or <b>Sign in with Google</b>. We have no passwords. Apple/Google give us a unique account identifier and, on first sign-in, your name and email address (Apple may give a relay address).",
                "Age check: the app only asks the phone to confirm that the parent is at least 18; we never receive a date of birth. If the age can't be confirmed, no account is created.",
                "Children don't create accounts: a child's phone works only after a parent scans its QR code and sets up the child's profile (first name, age, grade, languages).",
            ]),
            ("Family chats and notes", [
                "Messages, attachments and notes are <b>end-to-end encrypted</b> on the phone (AES-256-GCM; the keys stay on the family's devices). Our servers store only encrypted data and cannot read it.",
                "Translation happens on the phone when the system supports it. For languages the phone can't translate (for example Romanian), the message text is sent encrypted (HTTPS) through our server to Google for translation; we don't store it.",
                "For notifications we use Apple (APNs) and Google services, which needs a notification identifier for the phone.",
            ]),
            ("AI features (tutor, voice, photos, tests)", [
                "Your child's questions, photos they send (homework, Rubik's cube, timetable) and texts read aloud are sent through our server to <b>Google Cloud (Vertex AI, Gemini)</b> as our processor. We don't send names, email or other identifying data, and we don't store this content on our servers. Under Google Cloud's terms, Google doesn't use this data to train its models.",
                "The tutor conversation history stays on the phone.",
            ]),
            ("Where data is kept and who receives it", [
                "Data is stored on our own servers, run by our team, in Romania (EU). For fast and secure delivery of the website and the app (DNS, content delivery network, protection against attacks) we work with <b>Cloudflare</b>: traffic passes encrypted through Cloudflare's network, but account data and family content are stored only on our servers. Processors: Cloudflare (delivery and protection), Google (sign-in, AI, translation, notifications) and Apple (sign-in, age check, notifications). Where these partners process data outside the EU, transfers rely on the safeguards provided by the GDPR (the EU–US Data Privacy Framework or standard contractual clauses). We disclose data to authorities only when the law requires it.",
                "We don't sell data, show ads or build profiles.",
            ]),
            ("How long we keep data", ["Account data is kept while the account exists. A parent can delete all family data at any time in the app (account 👤 → “Delete all family data”): messages, children's profiles and sessions are deleted immediately. Backups are deleted within 90 days."]),
            ("Legal basis and children", ["We process data to provide the service you ask for (contract, Art. 6(1)(b) GDPR) and for security (legitimate interest, Art. 6(1)(f)). Children's data is processed with the consent and under the control of a parent or legal guardian (Art. 8 GDPR)."]),
            ("Your rights", ["You have the right of access, rectification, erasure, restriction, portability and objection. Write to <a href=\"mailto:contact@zapakid.ro\">contact@zapakid.ro</a>. You can complain to the Romanian data protection authority (ANSPDCP, <a href=\"https://www.dataprotection.ro\">dataprotection.ro</a>) or the authority in your country."]),
            ("Changes", ["When we change this policy we update the date above; important changes are also announced in the app."]),
        ],
    },
}

COMPANY = "Zapacit S.R.L.<br>Str. Zambilei nr. 76, Ghimbav 507075<br>Brașov, România<br>J2020002568087 · RO43395664"


def page(lang, name, title, desc, body):
    t, base = T[lang], LANGS[lang]
    path = "" if name in ("index", "404") else name
    alts = "".join(f'<link rel="alternate" hreflang="{l}" href="https://www.zapakid.ro{b}{path}">\n' for l, b in LANGS.items())
    langs = "".join(f'<a href="{b}{path}" hreflang="{l}"{" aria-current=\"page\"" if l == lang else ""}>{l.upper()}</a>' for l, b in LANGS.items())
    return f"""<!DOCTYPE html>
<html lang="{t['html_lang']}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{escape(desc)}">
<meta name="theme-color" content="#0b0f0c">
<link rel="icon" type="image/png" href="/favicon.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="stylesheet" href="/site.css">
<link rel="canonical" href="https://www.zapakid.ro{base}{path}">
{alts}<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(desc)}">
<meta property="og:image" content="https://www.zapakid.ro/img/robot.jpg">
</head>
<body>
<div class="wrap">
<header class="top">
<a class="logo" href="{base}"><img src="/favicon.png" alt="" width="36" height="36"><span>Zapa<b>Kid</b></span></a>
<nav class="langs" aria-label="Language">{langs}</nav>
</header>
{body}
<footer>
<a href="{base}">ZapaKid</a><a href="{base}contact">{t['nav_contact']}</a><a href="{base}privacy">{t['nav_privacy']}</a><a href="mailto:{EMAIL}">{EMAIL}</a>
<span class="copy">© 2026 <a href="https://www.zapacit.com">Zapacit S.R.L.</a></span>
</footer>
</div>
</body>
</html>
"""


def store(icon, small, name, url, soon):
    inner = f'{icon}<span><small>{small}</small><strong>{name}</strong></span>'
    if url:
        return f'<a class="store" href="{url}">{inner}</a>'
    return f'<span class="store soon" aria-label="{name}: {soon}">{inner}<span class="pill">{soon}</span></span>'


def landing(lang):
    t = T[lang]
    cards = "".join(f'<div class="card"><div class="ico" aria-hidden="true">{i}</div><h3>{escape(h)}</h3><p>{escape(p)}</p></div>'
                    for i, h, p in t["features"])
    band = "".join(f'<div><h3>{escape(h)}</h3><p>{escape(p)}</p></div>' for h, p in t["band"])
    body = f"""<main>
<section class="hero">
<div>
<h1>{t['h1']}</h1>
<p class="lead">{escape(t['lead'])}</p>
<div class="stores">
{store(APPLE_SVG, t['dl'], 'App Store', APP_STORE, t['soon'])}
{store(PLAY_SVG, t['dl'], 'Google Play', GOOGLE_PLAY, t['soon'])}
</div>
<p class="signin">{escape(t['signin'])}</p>
</div>
<div class="hero-art"><img src="/img/robot.jpg" alt="ZapaKid robot" width="720" height="720"></div>
</section>
<h2>{escape(t['feat_h'])}</h2>
<section class="features">{cards}</section>
<section class="band">{band}</section>
</main>"""
    return page(lang, "index", t["title"], t["desc"], body)


def contact(lang):
    t = T[lang]
    body = f"""<main class="page">
<h1>{t['contact_title']}</h1>
<p>{escape(t['contact_intro'])}</p>
<div class="contact-box"><a class="mail" href="mailto:{EMAIL}">{EMAIL}</a><br><a class="mail" href="tel:+40770972972">{PHONE[lang]}</a></div>
<p>{escape(t['contact_privacy'])}</p>
<h2>{t['company_h']}</h2>
<p>{COMPANY}</p>
</main>"""
    return page(lang, "contact", f"{t['contact_title']} — ZapaKid", t["desc"], body)


def privacy(lang):
    t = T[lang]
    sections = "".join(f"<h2>{n}. {escape(h)}</h2>\n" + "".join(f"<p>{p}</p>\n" for p in ps)
                       for n, (h, ps) in enumerate(t["privacy"], 1))
    body = f"""<main class="page">
<h1>{t['privacy_title']}</h1>
<p class="updated">{t['updated']}</p>
{sections}</main>"""
    return page(lang, "privacy", f"{t['privacy_title']} — ZapaKid", t["desc"], body)


def not_found():
    body = """<main class="page">
<h1>404</h1>
<p>Pagina nu există. · Diese Seite gibt es nicht. · This page doesn't exist.</p>
<p><a href="/">ZapaKid</a> · <a href="/de/">Deutsch</a> · <a href="/en/">English</a></p>
</main>"""
    return page("ro", "404", "404 — ZapaKid", T["ro"]["desc"], body)


for lang, base in LANGS.items():
    out = ROOT / base.strip("/")
    out.mkdir(exist_ok=True)
    for name, fn in (("index", landing), ("contact", contact), ("privacy", privacy)):
        (out / f"{name}.html").write_text(fn(lang))
(ROOT / "404.html").write_text(not_found())
print("built", ", ".join(f"{b}{{index,contact,privacy}}.html" for b in LANGS.values()), "+ /404.html")
