# On‑Premise Uitvoeringsstroom

Voor klanten die DocBits Operator on‑premises uitvoeren, beschrijft de volgende reeks hoe een verwerkt document een Operator-prompt activeert en uitvoert via de lokale DocBits Agent.

1. **Document Upload & Verwerking** Een document wordt geüpload naar DocBits en doorloopt de standaard verwerking (Extractie, validatie, enz.).
2. **Workflow Trigger** Nadat de verwerking is voltooid, evalueert een geconfigureerde Workflow in DocBits zijn triggercondities. Wanneer aan die voorwaarden is voldaan, maakt de Workflow een nieuwe **Operator Taak** aan.
3. **Taakcreatie & Verzending**
   * De workflow stuurt de scripttekst, variabelen, max-stappen, max-herhalingen als een taakpayload naar de gedeelde Werkpool.
4. **Agent Polling Loop**
   * Een on-prem DocBits Agent (geïnstalleerd in de klantomgeving) controleert elke 5 minuten de Werkpool. Als er geen taken worden gevonden, blijft de agent inactief en probeert het opnieuw na het interval.
5. **Taakuitvoering**
   * Wanneer een taak verschijnt in de Werkpool, haalt de Agent deze op en begint met de uitvoering.
6. **Loggeneratie**
   * Voor elke stap - succes of mislukking - registreert de agent gedetailleerde logs (acties, statussen, tijdstempels). Na voltooiing compileert het de volledige log en de definitieve status.
7. **Resultaat Terugkeer & Weergave**
   * De agent stuurt de logs en status terug naar DocBits. De uitvoeringsgeschiedenis van de oorspronkelijke workflow wordt bijgewerkt en gebruikers kunnen details bekijken in het **Workflow Logs** tabblad.
