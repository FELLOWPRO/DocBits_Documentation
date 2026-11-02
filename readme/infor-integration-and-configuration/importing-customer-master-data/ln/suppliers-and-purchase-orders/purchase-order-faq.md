# Bestellung – FAQ

**Wo prüfe ich, ob die Synchronisierungs-Updates des PurchaseOrderBOD korrekt implementiert sind?**

Navigieren Sie in Infor ERP / SAP zur Session _BOD Implementation Registration (bobod1100m000)_. In dieser Session können Sie sowohl Standard- als auch benutzerdefinierte BOD-Implementierungen, einschließlich des PurchaseOrderBOD, prüfen, ändern und registrieren.

\


<figure><img src="../../../../.gitbook/assets/PO.png" alt="LN-Sitzung BOD Implementation Registration (bobod1100m000) mit BOD-Implementierungen und den Kontrollkästchen Public, Standard und Staging"><figcaption></figcaption></figure>

**Wie kann ich die konkrete BOD-Implementierung identifizieren, die ich prüfen muss?**

Achten Sie auf die Felder BOD Implementation Identifier und BOD Name. Der BOD Name gibt in der Regel den Typ des BOD an (z. B. PurchaseOrderBOD). Der BOD Implementation Identifier ist eine eindeutige Kennung für diese BOD-Konfiguration.

\


**Was bedeutet das Kontrollkästchen „Public“ in der Session BOD Implementation Registration?**

Das Kontrollkästchen Public gibt an, ob die BOD-Implementierung für die externe Kommunikation verfügbar ist.

• Aktiviert: Das BOD kann außerhalb von Infor ERP / SAP ausgetauscht werden (öffentliche und geschützte Schnittstelle).

• Deaktiviert: Das BOD dient ausschließlich der internen Verarbeitung in Infor ERP / SAP (geschützte Schnittstelle).

\


**Ich sehe ein Feld „Parent BOD Name“. Wofür wird es verwendet?**

Das Feld Parent BOD Name zeigt das übergeordnete BOD an, wenn das aktuelle BOD eine abgeleitete oder abhängige Version ist. Ist das Kontrollkästchen Public aktiviert, bleibt dieses Feld leer. Andernfalls hilft es Ihnen, die Hierarchie der BOD-Implementierungen zu verstehen.

\


**Woran erkenne ich, ob die BOD-Implementierung eine Standard- oder eine benutzerdefinierte Implementierung ist?**

Prüfen Sie das Kontrollkästchen Standard.

• Aktiviert: Das BOD ist eine von Infor ERP / SAP ausgelieferte Standardimplementierung.

• Deaktiviert: Das BOD ist eine benutzerdefinierte Implementierung, die Ihr Team oder ein Partner definiert hat.

\


**Wozu dient das Kontrollkästchen „Staging“?**

Ist das Kontrollkästchen Staging aktiviert, werden BODs zunächst zwischengespeichert (Staging), statt sofort veröffentlicht zu werden. Sie können anschließend über die Session _Publish Staged BODs (bobod2200m000)_ veröffentlicht werden.

Hinweis: Für das ProjectBudgetBOD ist Staging zwingend vorgeschrieben und kann nicht geändert werden. Bei Standard-Stammdaten-BODs kann Staging manuell aktiviert werden, bei benutzerdefinierten BODs lässt es sich jederzeit konfigurieren.

\


**Wie wirkt sich das Kontrollkästchen „Synchronous Processing“ auf die Verarbeitung eingehender BODs aus?**

Synchronous Processing legt fest, was geschieht, wenn ein Folgeprozess nach dem Empfang eines BOD fehlschlägt.

• Aktiviert: Das eingehende BOD und der Folgeprozess müssen beide erfolgreich sein, andernfalls wird keines von beiden verarbeitet.

• Deaktiviert: Das eingehende BOD wird verarbeitet, aber wenn der Folgeprozess fehlschlägt, muss er manuell bearbeitet werden.

\


**Wo kann ich prüfen, ob die Funktion „Stage“ für mein BOD aktiv ist?**

Prüfen Sie in der Session _BOD Implementation Registration (bobod1100m000)_ das Kontrollkästchen Staging. Ist es nicht aktiviert, ist Staging für dieses BOD nicht aktiv.

\


**Was sollte ich noch berücksichtigen, wenn das PurchaseOrderBOD nicht bei allen Änderungen ausgelöst wird?**

• Vergewissern Sie sich, dass die Option Staging wie beabsichtigt eingestellt ist. Ist Staging deaktiviert, sollte das BOD sofort veröffentlicht werden.

• Prüfen Sie, ob die Einstellung Synchronous Processing für Ihren Workflow korrekt ist.

• Stellen Sie sicher, dass BOD Implementation Identifier und BOD Name korrekt sind und Sie an der richtigen BOD-Konfiguration arbeiten.

• Prüfen Sie, ob das BOD ein Standard- oder ein benutzerdefiniertes BOD ist, und kontrollieren Sie, ob benutzerdefinierte Einstellungen das Standardverhalten überschreiben.

\


**Gibt es Szenarien, in denen ich die Updates des PurchaseOrderBOD nicht wie erwartet sehe?**

Ja. Ist das BOD nicht richtig konfiguriert (falsche Einstellungen bei Public, Staging oder Synchronous Processing) oder handelt es sich um eine benutzerdefinierte BOD-Implementierung, die nicht zu Ihren Prozessanforderungen passt, werden Updates möglicherweise nicht wie erwartet ausgelöst. Prüfen Sie Ihre Konfiguration in der Session _bobod1100m000_ und stellen Sie sicher, dass alle Parameter zu Ihrem vorgesehenen Prozessablauf passen.
