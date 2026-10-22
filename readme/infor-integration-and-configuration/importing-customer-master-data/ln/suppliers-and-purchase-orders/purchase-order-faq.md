# Inkooporders: veelgestelde vragen

**Waar controleer ik of synchronisatie-updates van PurchaseOrderBOD correct zijn geïmplementeerd?**

Open de sessie _BOD Implementation Registration (bobod1100m000)_ in LN. Hier kunt u standaard- en aangepaste BOD-implementaties, waaronder PurchaseOrderBOD, bekijken, wijzigen en registreren.

\


<figure><img src="../../../../.gitbook/assets/PO.png" alt=""><figcaption></figcaption></figure>

**Hoe vind ik de BOD-implementatie die ik moet controleren?**

Zoek de velden BOD Implementation Identifier en BOD Name. BOD Name geeft doorgaans het type aan, bijvoorbeeld PurchaseOrderBOD. BOD Implementation Identifier is de unieke identificatie van die BOD-configuratie.

\


**Wat betekent het selectievakje ‘Public’ in BOD Implementation Registration?**

Public geeft aan of de BOD-implementatie beschikbaar is voor externe communicatie.

• Ingeschakeld: het BOD kan buiten LN worden uitgewisseld (openbare en beveiligde interface).

• Uitgeschakeld: het BOD is alleen voor interne verwerking in LN (beveiligde interface).

\


**Waarvoor dient het veld ‘Parent BOD Name’?**

Parent BOD Name toont het bovenliggende BOD als het huidige BOD een afgeleide of afhankelijke versie is. Als Public is ingeschakeld, is dit veld leeg. Anders helpt het de hiërarchie van BOD-implementaties te begrijpen.

\


**Hoe herken ik een standaard- of aangepaste BOD-implementatie?**

Controleer het selectievakje Standard.

• Ingeschakeld: het BOD is een standaardimplementatie die met LN wordt geleverd.

• Uitgeschakeld: het BOD is een aangepaste implementatie van uw team of een partner.

\


**Waarvoor dient het selectievakje ‘Staging’?**

Als Staging is ingeschakeld, worden BOD's eerst klaargezet in plaats van direct gepubliceerd. U kunt ze daarna publiceren via de sessie _Publish Staged BODs (bobod2200m000)_.

Opmerking: voor ProjectBudgetBOD is staging verplicht en niet te wijzigen. Voor standaard-BOD's voor stamgegevens kunt u staging handmatig inschakelen; voor aangepaste BOD's is dit altijd instelbaar.

\


**Hoe beïnvloedt ‘Synchronous Processing’ de verwerking van inkomende BOD's?**

Synchronous Processing bepaalt wat er gebeurt als een vervolgproces na ontvangst van een BOD mislukt.

• Ingeschakeld: zowel het inkomende BOD als het vervolgproces moeten slagen; anders wordt geen van beide verwerkt.

• Uitgeschakeld: het inkomende BOD wordt verwerkt. Als het vervolgproces mislukt, moet dit handmatig worden afgehandeld.

\


**Waar controleer ik of ‘Stage’ actief is voor mijn BOD?**

Controleer Staging in de sessie _BOD Implementation Registration (bobod1100m000)_. Als het vakje uitgeschakeld is, is staging voor dit BOD niet actief.

\


**Wat controleer ik als PurchaseOrderBOD niet bij elke update wordt geactiveerd?**

• Controleer of Staging naar wens is ingesteld. Als staging uitstaat, moet het BOD direct worden gepubliceerd.

• Controleer of Synchronous Processing correct is ingesteld voor uw workflow.

• Controleer of BOD Implementation Identifier en BOD Name juist zijn en u de juiste BOD-configuratie bewerkt.

• Controleer of het BOD standaard of aangepast is en of aangepaste instellingen het standaardgedrag overschrijven.

\


**Waarom zie ik updates van PurchaseOrderBOD soms niet zoals verwacht?**

Bij onjuiste instellingen voor Public, Staging of Synchronous Processing, of een aangepaste implementatie die niet bij uw procesvereisten past, worden updates mogelijk niet naar verwachting geactiveerd. Controleer in de sessie _bobod1100m000_ of alle parameters bij uw gewenste proces passen.
