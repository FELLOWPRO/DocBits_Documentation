# Wijzigingsvoorstellen en rapporten

<!-- touchless-admin-video-v2-20261104:start -->
**Videohoofdstuk (controleversie):** [Voorstellen en historie](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/nl.html#chapter=10).
<!-- touchless-admin-video-v2-20261104:end -->

Een aanbeveling kan vergezeld gaan van een **wijzigingsvoorstel**: één instellingswijziging die zou moeten helpen. Beheerders doorlopen daarbij vier stappen:

1. **Preview**: toont de wijziging (van de huidige naar de voorgestelde waarde) en wat DocBits verwacht. Er wordt niets opgeslagen. **Apply** is pas mogelijk nadat u een voorvertoning hebt bekeken.
2. **Apply**: slaat precies de getoonde wijziging op. De wijziging wordt gelogd.
3. **Measure**: DocBits vergelijkt het touchless-percentage van hetzelfde documenttype **voor en na**, over even lange perioden. Per periode zijn ten minste **20 documenten** nodig, anders meldt het rapport _not measurable_.
4. **Undo**: draait de wijziging terug als dit voorstel omkering ondersteunt. Controleer de beschikbaarheid en verifieer de herstelde instelling.

{% hint style="warning" %}
Een verschil voor/na is een **waarneming**, geen bewijs van oorzaak. Andere zaken kunnen tegelijk veranderen (een nieuwe leverancier, een seizoenspiek).
{% endhint %}

**Voorbeeld (illustratief).** U past _Switch on automatic PO match and export_ toe voor facturen. Twee weken later toont de **Change history** een AP touchless-percentage van 52 % voor (210 documenten) en 61 % na (198 documenten). Dat is +9 pp, met genoeg documenten om meetbaar te zijn. Het gemeten percentage omvat pure en alleen-goedkeuringsdocumenten; het meet niet de extractienauwkeurigheid. Een correctie van brongegevens in Infor moet ook worden gecontroleerd tegen de geïmporteerde gegevens en latere facturen; ga er niet van uit dat het een instellingswijziging in DocBits is of automatisch in deze historie staat.

Beheerders zien tussen de kerncijfers en de grafieken ook twee secties:

* **Improvement requests**: suggesties die gebruikers vanuit de validatieassistent hebben gestuurd, in twee tabbladen **Open** en **History**.
* **Learned rule proposals**: regels die DocBits heeft geleerd uit de correcties van uw team, bijvoorbeeld "voor leverancier X de waarde in veld Y vervangen". Controleer voordat u een regel aanmaakt de documenten waarin die een waarde zou vervangen die uw team had geaccepteerd. De sectie **After activation** toont de handmatige correcties van het doelveld voor en na het live gaan van een regel.

<figure><img src="../../../.gitbook/assets/touchless-consulting-report-nl.png" alt="Het Consulting report met de drie beste voorstellen, een rangschikkingstabel en de problemen per domein"><figcaption><p>Het Consulting report: beste voorstellen, een rangschikking van alle blokkades met documenten en geschatte impact per maand, en de problemen per domein. Voorbeeldorganisatie met demogegevens; de namen van leveranciers zijn fictief.</p></figcaption></figure>

Beheerders vinden het **Consulting report** onderaan het tabblad. Klik op **Create report** om het te laden. Het combineert voor uw organisatie:

* de **wijzigingen met het grootste effect**, gerangschikt, elk met het domein, het probleem, de aanbevolen actie, het aantal documenten en het **geschatte** effect per maand,
* **het domein van elk probleem** (extractie, stamgegevens, PO-matching, automatische boekhouding, instellingen, proces),
* **controles van de tabelconfiguratie**, bijvoorbeeld _structured table output not used_ of _table column type mismatch_ per documenttype en kolom.

De effectwaarden zijn **schattingen**. Antwoordt het rapport _forbidden_, dan staat uw rol het niet toe.

Zie [Touchless met MCP](touchless-mcp.md) voor de bijbehorende toolaanroepen en de classificatie van menselijke acties.

## Gerelateerde pagina's

* [Touchless Intelligence](./)
* [Leveranciersdiagnose en probleemclusters](touchless-supplier-diagnosis.md)
* [PO-matchingdiagnose](touchless-po-matching-diagnosis.md)

<!-- Documentation review 2026-11-04: extraction quality vs process outcomes; KPI and terminal-outcome definitions checked against DocBits_API c51f350c728acb8ac964098d15f7b006bce273f4, module/automation_intelligence/kpi.py and bucket.py. Existing native screenshots retained and checked separately from illustrative examples. -->

<!-- Completion review 2026-11-04: owned synthetic PO examples, MCP schema/read evidence, human-action classification, KPI labels and screenshot proof limits. -->
