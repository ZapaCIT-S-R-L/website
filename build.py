#!/usr/bin/env python3
"""Builds the static zapakid.ro site: landing, contact and privacy in RO (/), DE (/de/) and EN (/en/).

Edit the texts below, run `python3 build.py`, commit the generated .html files with it.
When the apps are published, set APP_STORE / GOOGLE_PLAY and rebuild: the buttons become links.
"""

from html import escape
from pathlib import Path

ROOT = Path(__file__).parent
APP_STORE = ""  # e.g. https://apps.apple.com/app/id...
GOOGLE_PLAY = ""  # e.g. https://play.google.com/store/apps/details?id=...
EMAIL = "hello@zapakid.ro"
PHONE = {"ro": "0770 972 972", "de": "+40 770 972 972", "en": "+40 770 972 972"}
LANGS = {"ro": "/", "de": "/de/", "en": "/en/"}

APPLE_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M16.4 12.6c0-2.6 2.1-3.8 2.2-3.9-1.2-1.8-3.1-2-3.7-2-1.6-.2-3.1.9-3.9.9-.8 0-2-.9-3.4-.9-1.7 0-3.3 1-4.2 2.6-1.8 3.1-.5 7.7 1.3 10.2.9 1.2 1.9 2.6 3.2 2.6 1.3-.1 1.8-.8 3.3-.8s2 .8 3.4.8c1.4 0 2.3-1.3 3.1-2.5 1-1.4 1.4-2.8 1.4-2.9-.1 0-2.7-1-2.7-4.1zM13.9 5c.7-.9 1.2-2 1-3.2-1 .1-2.2.7-3 1.5-.6.7-1.2 1.9-1.1 3.1 1.2.1 2.3-.6 3.1-1.4z"/></svg>'
PLAY_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 2.6c-.3.3-.4.7-.4 1.2v16.4c0 .5.1.9.4 1.2l9.3-9.4L4 2.6zm10.4 10.5 2.6 2.6-11 6.3 8.4-8.9zm3.9-3.8 2.9 1.7c.9.5.9 1.4 0 1.9l-2.9 1.7-2.8-2.7 2.8-2.6zM6 1.9l11 6.3-2.6 2.6L6 1.9z"/></svg>'

T = {
    "ro": {
        "html_lang": "ro",
        "title": "ZapaKid — Chatul criptat al familiei, între părinți și copii",
        "desc": "ZapaKid: chat criptat end-to-end între părinți și copii — mesaje, poze și mesaje vocale. Părinții adaugă copiii cu un cod QR. Date doar în UE, fără reclame. În curând pe App Store și Google Play.",
        "nav_contact": "Contact",
        "nav_privacy": "Confidențialitate",
        "h1": "Familia ta, <span>la un mesaj distanță.</span>",
        "lead": "ZapaKid este chatul privat dintre părinți și copii: mesaje, poze și mesaje vocale, criptate end-to-end. Doar familia voastră le poate citi — nici măcar noi.",
        "dl": "Disponibil pe",
        "soon": "În curând",
        "signin": "Conectare doar cu Apple sau Google — fără parole, fără conturi noi de reținut.",
        "feat_h": "Ce găsești în ZapaKid",
        "features": [
            (
                "🔒",
                "Criptat end-to-end",
                "Mesajele se criptează pe telefon. Cheile rămân pe telefoanele familiei; serverele noastre văd doar date criptate.",
            ),
            ("💬", "Mesaje, poze și voce", "Text, fotografii și mesaje vocale între părinți și copii."),
            (
                "👨‍👩‍👧",
                "Doar familia",
                "Copilul vorbește doar cu părinții din familia lui. Fără căutare, fără profiluri publice, fără străini.",
            ),
            (
                "📱",
                "Copilul, adăugat de părinte",
                "Părintele scanează un cod QR pe telefonul copilului. Copiii nu își fac singuri cont.",
            ),
            (
                "🔁",
                "Telefon nou, aceleași conversații",
                "Conversațiile revin pe telefonul nou din keychain-ul criptat al telefonului sau de pe alt telefon din familie.",
            ),
            ("🇪🇺", "Date doar în UE", "Toate datele sunt stocate exclusiv în Uniunea Europeană."),
        ],
        "band": [
            (
                "Pentru părinți de peste 18 ani",
                "Contul de părinte se face doar cu Apple sau Google, iar telefonul confirmă că ai cel puțin 18 ani.",
            ),
            (
                "Fără reclame, fără urmărire",
                "Nu vindem date, nu afișăm reclame și nu facem profilare. Site-ul nu folosește cookie-uri.",
            ),
        ],
        "contact_title": "Contact",
        "contact_intro": "Ai o întrebare despre ZapaKid, o idee sau o problemă? Scrie-ne, răspundem de obicei în 1–2 zile lucrătoare.",
        "contact_privacy": 'Pentru cereri legate de datele personale (acces, ștergere etc.) scrie-ne la <a href="mailto:privacy@zapakid.ro">privacy@zapakid.ro</a>.',
        "company_h": "Firma",
        "privacy_title": "Politica de confidențialitate",
        "updated": "Ultima actualizare: 26 octombrie 2026",
        "privacy": [
            (
                "Cine suntem",
                [
                    'ZapaKid este un produs al <b>Zapacit S.R.L.</b>, Str. Zambilei nr. 76, Ghimbav 507075, județul Brașov, România, J2020002568087, CUI RO43395664 („noi”), operator al datelor personale descrise aici, conform Regulamentului (UE) 2016/679 (GDPR). Contact pentru datele personale: <a href="mailto:privacy@zapakid.ro">privacy@zapakid.ro</a>.'
                ],
            ),
            (
                "Site-ul zapakid.ro",
                [
                    "Site-ul este doar o pagină de prezentare. Nu are conturi, formulare, cookie-uri sau instrumente de analiză și nu încarcă resurse de la terți. Cloudflare, care găzduiește site-ul, înregistrează temporar, din motive de securitate, adresa IP, data și pagina cerută."
                ],
            ),
            (
                "Contul: doar părinți, doar Apple sau Google",
                [
                    "Contul de părinte se creează exclusiv prin <b>Sign in with Apple</b> sau <b>Sign in with Google</b>. Nu avem parole. Primim de la Apple/Google un identificator unic al contului și adresa de email.",
                    "Verificarea vârstei: aplicația cere telefonului (Apple Declared Age Range, Google Play Age Signals) doar confirmarea că părintele are cel puțin 18 ani; nu primim data nașterii. Dacă telefonul indică un minor, aplicația nu creează contul.",
                    "Copiii nu își creează singuri cont: telefonul copilului funcționează doar după ce un părinte scanează codul QR, acceptă Acordul părintelui și setează profilul copilului (poreclă, interval de vârstă, avatar).",
                    "Dacă îți pierzi accesul, îți recuperezi contul cu Apple/Google, cu un cod pe email sau cu un cod prin SMS (trimise prin <b>Twilio</b>).",
                ],
            ),
            (
                "Conversațiile familiei",
                [
                    "Mesajele, pozele și mesajele vocale sunt <b>criptate end-to-end</b> pe telefon. Cheile rămân pe telefoanele familiei și în keychain-ul criptat al telefonului (iCloud Keychain, Android). Serverele noastre stochează doar datele criptate și <b>nu le pot citi, asculta sau recupera</b>, nici la cererea unei autorități.",
                    "Pentru notificări folosim Apple (APNs) și Google (FCM). Notificările spun doar cine a scris, niciodată conținutul.",
                ],
            ),
            (
                "Unde sunt datele și cui le transmitem",
                [
                    "Toate datele sunt stocate <b>exclusiv în UE</b>. Persoane împuternicite, fiecare cu acord de prelucrare a datelor: <b>Cloudflare</b> (găzduire și stocare), <b>Google</b> (conectare, notificări pe Android, copii de siguranță criptate, pagina de status), <b>Apple</b> (conectare, verificarea vârstei, notificări pe iOS), <b>Twilio</b> (coduri prin SMS și email). Când Apple, Google sau Twilio prelucrează date în afara UE pentru conectare sau notificări, transferul se face în baza Cadrului UE–SUA privind protecția datelor sau a clauzelor contractuale standard.",
                    "Nu vindem date, nu afișăm reclame și nu facem profilare.",
                ],
            ),
            (
                "Cât timp păstrăm datele",
                [
                    "Mesajele criptate: cât timp conversația există pe cel puțin un telefon. Metadatele conversației (cine, când, dimensiune): până când ambele părți șterg conversația. Jurnalele de securitate: 90 de zile.",
                    "Ștergerea contului sau a unui copil se face imediat, din aplicație. Copilul nu își poate șterge singur contul; o face părintele. Când ultimul părinte își șterge contul, toți copiii din familie sunt șterși. Copiile de siguranță criptate se rotesc după 30 de zile. Dovada acordului părintelui se păstrează pe durata contului și încă 5 ani.",
                ],
            ),
            (
                "Temeiul legal și copiii",
                [
                    "Prelucrăm datele pentru a furniza serviciul (executarea contractului, art. 6(1)(b) GDPR), pentru securitate (interes legitim, art. 6(1)(f)) și pentru a dovedi acordul părintelui (obligație legală, art. 6(1)(c) și art. 7). Datele copiilor sunt prelucrate pe baza acordului părintelui sau tutorelui legal (art. 8 GDPR)."
                ],
            ),
            (
                "Drepturile tale",
                [
                    'Ai dreptul de acces, rectificare, ștergere, restricționare, portabilitate și opoziție, pentru tine și pentru copiii tăi. Scrie-ne la <a href="mailto:privacy@zapakid.ro">privacy@zapakid.ro</a>; răspundem în cel mult o lună. Poți depune plângere la Autoritatea Națională de Supraveghere a Prelucrării Datelor cu Caracter Personal (ANSPDCP, <a href="https://www.dataprotection.ro">dataprotection.ro</a>).'
                ],
            ),
            (
                "Modificări",
                [
                    "Când schimbăm această politică, actualizăm data de mai sus; schimbările importante le anunțăm și în aplicație."
                ],
            ),
        ],
    },
    "de": {
        "html_lang": "de",
        "title": "ZapaKid — Der verschlüsselte Familienchat für Eltern und Kinder",
        "desc": "ZapaKid: Ende-zu-Ende-verschlüsselter Chat zwischen Eltern und Kindern — Nachrichten, Fotos und Sprachnachrichten. Eltern fügen Kinder per QR-Code hinzu. Daten nur in der EU, keine Werbung. Bald im App Store und bei Google Play.",
        "nav_contact": "Kontakt",
        "nav_privacy": "Datenschutz",
        "h1": "Deine Familie, <span>eine Nachricht entfernt.</span>",
        "lead": "ZapaKid ist der private Chat zwischen Eltern und Kindern: Nachrichten, Fotos und Sprachnachrichten, Ende-zu-Ende-verschlüsselt. Nur eure Familie kann sie lesen — nicht einmal wir.",
        "dl": "Erhältlich im",
        "soon": "Bald",
        "signin": "Anmeldung nur mit Apple oder Google — keine Passwörter, kein neues Konto zum Merken.",
        "feat_h": "Was ZapaKid kann",
        "features": [
            (
                "🔒",
                "Ende-zu-Ende-verschlüsselt",
                "Nachrichten werden auf dem Telefon verschlüsselt. Die Schlüssel bleiben auf den Telefonen der Familie; unsere Server sehen nur verschlüsselte Daten.",
            ),
            ("💬", "Text, Fotos und Sprache", "Nachrichten, Fotos und Sprachnachrichten zwischen Eltern und Kindern."),
            (
                "👨‍👩‍👧",
                "Nur die Familie",
                "Dein Kind schreibt nur mit den Eltern seiner Familie. Keine Suche, keine öffentlichen Profile, keine Fremden.",
            ),
            (
                "📱",
                "Eltern fügen Kinder hinzu",
                "Ein Elternteil scannt einen QR-Code auf dem Telefon des Kindes. Kinder legen kein eigenes Konto an.",
            ),
            (
                "🔁",
                "Neues Telefon, gleiche Chats",
                "Die Chats kommen aus dem verschlüsselten Schlüsselbund des Telefons oder von einem anderen Telefon der Familie zurück.",
            ),
            ("🇪🇺", "Daten nur in der EU", "Alle Daten werden ausschließlich in der Europäischen Union gespeichert."),
        ],
        "band": [
            (
                "Für Eltern ab 18",
                "Das Elternkonto gibt es nur mit Apple oder Google, und das Telefon bestätigt, dass du mindestens 18 bist.",
            ),
            (
                "Keine Werbung, kein Tracking",
                "Wir verkaufen keine Daten, zeigen keine Werbung und erstellen keine Profile. Die Website verwendet keine Cookies.",
            ),
        ],
        "contact_title": "Kontakt",
        "contact_intro": "Du hast eine Frage zu ZapaKid, eine Idee oder ein Problem? Schreib uns, wir antworten meist innerhalb von 1–2 Werktagen.",
        "contact_privacy": 'Für Anfragen zu personenbezogenen Daten (Auskunft, Löschung usw.) schreib an <a href="mailto:privacy@zapakid.ro">privacy@zapakid.ro</a>.',
        "company_h": "Unternehmen",
        "privacy_title": "Datenschutzerklärung",
        "updated": "Zuletzt aktualisiert: 26. Oktober 2026",
        "privacy": [
            (
                "Wer wir sind",
                [
                    'ZapaKid ist ein Produkt der <b>Zapacit S.R.L.</b>, Str. Zambilei nr. 76, 507075 Ghimbav, Kreis Brașov, Rumänien, J2020002568087, USt-IdNr. RO43395664 („wir“), Verantwortlicher für die hier beschriebenen personenbezogenen Daten gemäß Verordnung (EU) 2016/679 (DSGVO). Kontakt für Datenschutz: <a href="mailto:privacy@zapakid.ro">privacy@zapakid.ro</a>.'
                ],
            ),
            (
                "Die Website zapakid.ro",
                [
                    "Die Website ist nur eine Präsentationsseite. Sie hat keine Konten, Formulare, Cookies oder Analysewerkzeuge und lädt keine Inhalte von Dritten. Cloudflare, das die Website hostet, protokolliert aus Sicherheitsgründen vorübergehend IP-Adresse, Datum und aufgerufene Seite."
                ],
            ),
            (
                "Das Konto: nur Eltern, nur Apple oder Google",
                [
                    "Ein Elternkonto wird ausschließlich mit <b>Mit Apple anmelden</b> oder <b>Mit Google anmelden</b> erstellt. Wir haben keine Passwörter. Wir erhalten von Apple/Google eine eindeutige Kontokennung und die E-Mail-Adresse.",
                    "Altersprüfung: Die App fragt das Telefon (Apple Declared Age Range, Google Play Age Signals) nur, ob der Elternteil mindestens 18 Jahre alt ist; ein Geburtsdatum erhalten wir nicht. Meldet das Telefon eine minderjährige Person, wird kein Konto erstellt.",
                    "Kinder legen kein eigenes Konto an: Das Telefon des Kindes funktioniert erst, wenn ein Elternteil den QR-Code scannt, der Elternvereinbarung zustimmt und das Profil des Kindes anlegt (Spitzname, Altersbereich, Avatar).",
                    "Wenn du den Zugang verlierst, stellst du dein Konto mit Apple/Google, einem Code per E-Mail oder einem Code per SMS wieder her (versendet über <b>Twilio</b>).",
                ],
            ),
            (
                "Die Chats der Familie",
                [
                    "Nachrichten, Fotos und Sprachnachrichten werden auf dem Telefon <b>Ende-zu-Ende-verschlüsselt</b>. Die Schlüssel bleiben auf den Telefonen der Familie und im verschlüsselten Schlüsselbund des Telefons (iCloud-Schlüsselbund, Android). Unsere Server speichern nur verschlüsselte Daten und <b>können sie nicht lesen, anhören oder wiederherstellen</b>, auch nicht auf Verlangen einer Behörde.",
                    "Für Benachrichtigungen nutzen wir Apple (APNs) und Google (FCM). Benachrichtigungen sagen nur, wer geschrieben hat, nie den Inhalt.",
                ],
            ),
            (
                "Wo die Daten liegen und wer sie erhält",
                [
                    "Alle Daten werden <b>ausschließlich in der EU</b> gespeichert. Auftragsverarbeiter, jeweils mit Auftragsverarbeitungsvertrag: <b>Cloudflare</b> (Hosting und Speicherung), <b>Google</b> (Anmeldung, Benachrichtigungen auf Android, verschlüsselte Sicherungskopien, Statusseite), <b>Apple</b> (Anmeldung, Altersprüfung, Benachrichtigungen auf iOS), <b>Twilio</b> (Codes per SMS und E-Mail). Wenn Apple, Google oder Twilio für Anmeldung oder Benachrichtigungen Daten außerhalb der EU verarbeiten, geschieht das auf Grundlage des EU-US-Datenschutzrahmens oder von Standardvertragsklauseln.",
                    "Wir verkaufen keine Daten, zeigen keine Werbung und erstellen keine Profile.",
                ],
            ),
            (
                "Wie lange wir Daten speichern",
                [
                    "Verschlüsselte Nachrichten: solange der Chat auf mindestens einem Telefon existiert. Metadaten des Chats (wer, wann, Größe): bis beide Seiten den Chat löschen. Sicherheitsprotokolle: 90 Tage.",
                    "Das Löschen des Kontos oder eines Kindes erfolgt sofort in der App. Ein Kind kann sein Konto nicht selbst löschen; das macht ein Elternteil. Löscht der letzte Elternteil sein Konto, werden alle Kinder der Familie gelöscht. Verschlüsselte Sicherungskopien werden nach 30 Tagen überschrieben. Der Nachweis der elterlichen Einwilligung wird für die Dauer des Kontos und weitere 5 Jahre aufbewahrt.",
                ],
            ),
            (
                "Rechtsgrundlage und Kinder",
                [
                    "Wir verarbeiten Daten, um den Dienst bereitzustellen (Vertragserfüllung, Art. 6 Abs. 1 lit. b DSGVO), für die Sicherheit (berechtigtes Interesse, Art. 6 Abs. 1 lit. f) und um die elterliche Einwilligung nachzuweisen (rechtliche Verpflichtung, Art. 6 Abs. 1 lit. c und Art. 7). Daten von Kindern werden auf Grundlage der Einwilligung der Eltern oder Erziehungsberechtigten verarbeitet (Art. 8 DSGVO)."
                ],
            ),
            (
                "Deine Rechte",
                [
                    'Du hast das Recht auf Auskunft, Berichtigung, Löschung, Einschränkung, Datenübertragbarkeit und Widerspruch, für dich und deine Kinder. Schreib an <a href="mailto:privacy@zapakid.ro">privacy@zapakid.ro</a>; wir antworten innerhalb eines Monats. Du kannst dich bei der rumänischen Datenschutzbehörde ANSPDCP (<a href="https://www.dataprotection.ro">dataprotection.ro</a>) oder bei der Aufsichtsbehörde deines Landes beschweren.'
                ],
            ),
            (
                "Änderungen",
                [
                    "Wenn wir diese Erklärung ändern, aktualisieren wir das Datum oben; wichtige Änderungen kündigen wir auch in der App an."
                ],
            ),
        ],
    },
    "en": {
        "html_lang": "en",
        "title": "ZapaKid — The encrypted family chat for parents and kids",
        "desc": "ZapaKid: end-to-end encrypted chat between parents and kids — messages, photos and voice messages. Parents add their kids with a QR code. Data in the EU only, no ads. Coming soon to the App Store and Google Play.",
        "nav_contact": "Contact",
        "nav_privacy": "Privacy",
        "h1": "Your family, <span>one message away.</span>",
        "lead": "ZapaKid is the private chat between parents and kids: messages, photos and voice messages, end-to-end encrypted. Only your family can read them — not even us.",
        "dl": "Get it on",
        "soon": "Soon",
        "signin": "Sign in with Apple or Google only — no passwords, no new account to remember.",
        "feat_h": "What's in ZapaKid",
        "features": [
            (
                "🔒",
                "End-to-end encrypted",
                "Messages are encrypted on the phone. The keys stay on your family's phones; our servers only see encrypted data.",
            ),
            ("💬", "Text, photos and voice", "Messages, photos and voice messages between parents and kids."),
            (
                "👨‍👩‍👧",
                "Family only",
                "Your child can only chat with the parents in their family. No search, no public profiles, no strangers.",
            ),
            (
                "📱",
                "Kids are added by a parent",
                "A parent scans a QR code on the child's phone. Kids don't create their own accounts.",
            ),
            (
                "🔁",
                "New phone, same chats",
                "Chats come back from the phone's encrypted keychain or from another phone in your family.",
            ),
            ("🇪🇺", "Data in the EU only", "All data is stored in the European Union only."),
        ],
        "band": [
            (
                "For parents aged 18+",
                "Parent accounts use Apple or Google only, and the phone confirms you're at least 18.",
            ),
            ("No ads, no tracking", "We don't sell data, show ads or build profiles. This site uses no cookies."),
        ],
        "contact_title": "Contact",
        "contact_intro": "Got a question about ZapaKid, an idea or a problem? Write to us; we usually reply within 1–2 working days.",
        "contact_privacy": 'For personal data requests (access, deletion and so on), write to <a href="mailto:privacy@zapakid.ro">privacy@zapakid.ro</a>.',
        "company_h": "Company",
        "privacy_title": "Privacy policy",
        "updated": "Last updated: 26 October 2026",
        "privacy": [
            (
                "Who we are",
                [
                    'ZapaKid is a product of <b>Zapacit S.R.L.</b>, Str. Zambilei nr. 76, Ghimbav 507075, Brașov County, Romania, J2020002568087, VAT RO43395664 (“we”), the controller of the personal data described here under Regulation (EU) 2016/679 (GDPR). Privacy contact: <a href="mailto:privacy@zapakid.ro">privacy@zapakid.ro</a>.'
                ],
            ),
            (
                "The zapakid.ro website",
                [
                    "This site is a presentation page only. It has no accounts, forms, cookies or analytics and loads nothing from other sites. Cloudflare, which hosts the site, briefly logs the IP address, date and page requested, for security."
                ],
            ),
            (
                "Accounts: parents only, Apple or Google only",
                [
                    "A parent account is created only with <b>Sign in with Apple</b> or <b>Sign in with Google</b>. We have no passwords. Apple/Google give us a unique account identifier and your email address.",
                    "Age check: the app asks the phone (Apple Declared Age Range, Google Play Age Signals) only to confirm the parent is at least 18; we never receive a date of birth. If the phone reports a minor, no account is created.",
                    "Kids don't create their own accounts: a child's phone only works after a parent scans the QR code, accepts the Parental Agreement and sets up the child's profile (nickname, age range, avatar).",
                    "If you lose access, you recover your account with Apple/Google, an email code or an SMS code (sent through <b>Twilio</b>).",
                ],
            ),
            (
                "Your family's chats",
                [
                    "Messages, photos and voice messages are <b>end-to-end encrypted</b> on the phone. The keys stay on your family's phones and in the phone's encrypted keychain (iCloud Keychain, Android). Our servers store only encrypted data and <b>cannot read, listen to or recover it</b>, even if an authority asks.",
                    "For notifications we use Apple (APNs) and Google (FCM). Notifications only say who wrote, never what.",
                ],
            ),
            (
                "Where data is stored and who receives it",
                [
                    "All data is stored in the <b>EU only</b>. Processors, each under a data processing agreement: <b>Cloudflare</b> (hosting and storage), <b>Google</b> (sign-in, Android notifications, encrypted backups, status page), <b>Apple</b> (sign-in, age check, iOS notifications), <b>Twilio</b> (SMS and email codes). When Apple, Google or Twilio process data outside the EU for sign-in or notifications, the transfer relies on the EU–US Data Privacy Framework or standard contractual clauses.",
                    "We don't sell data, show ads or build profiles.",
                ],
            ),
            (
                "How long we keep data",
                [
                    "Encrypted messages: as long as the chat exists on at least one phone. Chat metadata (who, when, size): until both sides delete the chat. Security logs: 90 days.",
                    "Deleting an account or a child happens immediately, in the app. A child can't delete their own account; a parent does. When the last parent deletes their account, every child in the family is deleted too. Encrypted backups rotate after 30 days. The record of parental consent is kept for the life of the account plus 5 years.",
                ],
            ),
            (
                "Legal basis and children",
                [
                    "We process data to provide the service (contract, Art. 6(1)(b) GDPR), for security (legitimate interest, Art. 6(1)(f)) and to prove parental consent (legal obligation, Art. 6(1)(c) and Art. 7). Children's data is processed on the basis of their parent's or legal guardian's consent (Art. 8 GDPR)."
                ],
            ),
            (
                "Your rights",
                [
                    'You have the right of access, rectification, erasure, restriction, portability and objection, for yourself and your children. Write to <a href="mailto:privacy@zapakid.ro">privacy@zapakid.ro</a>; we reply within one month. You can complain to Romania\'s data protection authority, ANSPDCP (<a href="https://www.dataprotection.ro">dataprotection.ro</a>), or to the authority in your EU country.'
                ],
            ),
            (
                "Changes",
                [
                    "When we change this policy we update the date above; important changes are also announced in the app."
                ],
            ),
        ],
    },
}

COMPANY = "Zapacit S.R.L.<br>Str. Zambilei nr. 76, Ghimbav 507075<br>Brașov, România<br>J2020002568087 · RO43395664"


def page(lang, name, title, desc, body):
    t, base = T[lang], LANGS[lang]
    path = "" if name in ("index", "404") else name
    alts = "".join(
        f'<link rel="alternate" hreflang="{l}" href="https://www.zapakid.ro{b}{path}">\n' for l, b in LANGS.items()
    )
    langs = "".join(
        f'<a href="{b}{path}" hreflang="{l}"{' aria-current="page"' if l == lang else ""}>{l.upper()}</a>'
        for l, b in LANGS.items()
    )
    return f"""<!DOCTYPE html>
<html lang="{t["html_lang"]}">
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
<span class="brand"><a href="{base}">ZapaKid</a> @ <a class="version" href="__VERSION_URL__">__VERSION__</a></span><a href="{base}contact">{t["nav_contact"]}</a><a href="{base}privacy">{t["nav_privacy"]}</a><a href="mailto:{EMAIL}">{EMAIL}</a>
<span class="copy">© 2026 <a href="https://www.zapacit.com">Zapacit S.R.L.</a></span>
</footer>
</div>
</body>
</html>
"""


def store(icon, small, name, url, soon):
    inner = f"{icon}<span><small>{small}</small><strong>{name}</strong></span>"
    if url:
        return f'<a class="store" href="{url}">{inner}</a>'
    return f'<span class="store soon">{inner}<span class="pill">{soon}</span></span>'


def landing(lang):
    t = T[lang]
    cards = "".join(
        f'<div class="card"><div class="ico" aria-hidden="true">{i}</div><h3>{escape(h)}</h3><p>{escape(p)}</p></div>'
        for i, h, p in t["features"]
    )
    band = "".join(f"<div><h3>{escape(h)}</h3><p>{escape(p)}</p></div>" for h, p in t["band"])
    body = f"""<main>
<section class="hero">
<div>
<h1>{t["h1"]}</h1>
<p class="lead">{escape(t["lead"])}</p>
<div class="stores">
{store(APPLE_SVG, t["dl"], "App Store", APP_STORE, t["soon"])}
{store(PLAY_SVG, t["dl"], "Google Play", GOOGLE_PLAY, t["soon"])}
</div>
<p class="signin">{escape(t["signin"])}</p>
</div>
<div class="hero-art"><img src="/img/robot.jpg" alt="ZapaKid robot" width="720" height="720"></div>
</section>
<h2>{escape(t["feat_h"])}</h2>
<section class="features">{cards}</section>
<section class="band">{band}</section>
</main>"""
    return page(lang, "index", t["title"], t["desc"], body)


def contact(lang):
    t = T[lang]
    body = f"""<main class="page">
<h1>{t["contact_title"]}</h1>
<p>{escape(t["contact_intro"])}</p>
<div class="contact-box"><a class="mail" href="mailto:{EMAIL}">{EMAIL}</a><br><a class="mail" href="tel:+40770972972">{PHONE[lang].replace(" ", "&nbsp;")}</a></div>
<p>{escape(t["contact_privacy"])}</p>
<h2>{t["company_h"]}</h2>
<p>{COMPANY}</p>
</main>"""
    return page(lang, "contact", f"{t['contact_title']} — ZapaKid", t["desc"], body)


def privacy(lang):
    t = T[lang]
    sections = "".join(
        f"<h2>{n}. {escape(h)}</h2>\n" + "".join(f"<p>{p}</p>\n" for p in ps)
        for n, (h, ps) in enumerate(t["privacy"], 1)
    )
    body = f"""<main class="page">
<h1>{t["privacy_title"]}</h1>
<p class="updated">{t["updated"]}</p>
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
