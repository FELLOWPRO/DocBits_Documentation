# So importieren Sie alle Lieferanten

*
[ ] 
    * [ ] Melden Sie sich in der InforOS-Umgebung an und gehen Sie zur M3-Anwendung. Empfehlung: Stellen Sie sicher, dass Sie Admin-Rechte haben, um alle Programme ausführen zu können.

    ![Infor M3-Startmenü in Infor OS mit der Programmliste, den Panels Favorites und Recent und dem geöffneten Suchfeld evs006](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/6cf93500-2e90-4cfc-a9fb-5873e5dcb953.png)

    * [ ] Führen Sie das Programm _**evs006**_ aus. Drücken Sie command + R, dann sehen Sie die geöffnete Registerkarte zum Suchen und Starten.

    ![Infor-M3-Startmenü mit dem Suchfeld, das unter Recent den Eintrag evs006 Initial Load zum Öffnen bereit zeigt](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/f77b242e-eb2f-43b6-8a2e-03d264198e0c.png)

    * [ ] Wenn _**evs006**_ geöffnet ist, sehen Sie eine leere Tabelle. Bitte füllen Sie die Spalten „BOD noun“ und „Table“ aus. Für „BOD noun“ geben Sie „SupplierPartyMaster“ ein und für „Table“ verwenden wir die M3-Lieferantentabelle „CIDMAS“.

    ![Menübildschirm von Infor M3 mit geöffnetem Suchfeld zum Starten eines Programms](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/827a9dbb-c974-4da7-9bd3-f8e87adad60f.png)

    ![Tabelle EVS006 Initial Load mit den Spalten BOD noun, BOD variant, Table und BOD description](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/e30c7b86-dcfb-41d2-bd32-447b60e4581b.png)

    * [ ] Nachdem Sie diese Spalten ausgefüllt haben, klicken Sie auf die Schaltfläche CREATE (oben in der Leiste des Bildschirms). Sie gelangen zum folgenden Bildschirm.

    ![Leere Tabelle EVS006 Initial Load mit den Spaltenüberschriften BOD noun, BOD variant, Table und BOD description](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/30eee6b2-24ed-4e1f-8812-1304e7dede8e.png)

    ![Panel EVS006 Initial Load mit Table CIDMAS Supplier, BOD noun SupplierPartyMaster und den Bereichen Details und Table keys](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/461b72d3-d576-4c92-95c2-d175183088af.png)

    * [ ] Füllen Sie die „BOD Description“ mit SupplierPartyMaster aus.

    ![Panel „EVS006 Initial Load“ mit der BOD-Beschreibung SupplierPartyMaster unter Details ausgefüllt](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/4dc345a8-8eca-4e03-800a-37a670f8792e.png)

    * [ ] Klicken Sie auf Next (unten links auf dem Bildschirm).

    ![EVS006-Initial-Load-Panel für die Tabelle CIDMAS mit dem BOD-Nomen SupplierPartyMaster und der Schaltfläche Next unten links](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/315aa54b-f0bd-4057-a1ed-e476c9000725.png)

    * [ ] Klicken Sie in diesem Fenster auf Next.

    ![Dialog Text in M3 mit den Spalten Text block und Language sowie dem Namen InvExt](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/c0ff3fe1-a393-43cc-96a5-3e0cb1d878b7.png)

    * [ ] Wenn Sie diesen Bildschirm mit der ausgefüllten Tabelle mit dem BOD SupplierPartyMaster sehen, klicken Sie mit der rechten Maustaste auf das BOD und wählen Sie Related > Run.

    ![EVS006-Initial-Load-Tabelle mit der Zeile SupplierPartyMaster und ihrem Rechtsklick-Kontextmenü mit Related, Run und Change](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/d819fdd5-5b4a-48ef-9412-f211c0d2355f.png)

    * [ ] In diesem nächsten Fenster wählen Sie „Sync“ und Next.

    ![Panel BOD Processor Administration in Infor M3 mit dem Job SupplierPartyMaster, dem Verb Sync und dem Status Pending](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/8fbed442-7deb-4c1e-9295-5038fe124331.png)

    Nachdem Sie alle diese Schritte abgeschlossen haben, haben Sie das BOD aktiviert, um alle Lieferanten aus der Tabelle CIDMAS zu importieren. Nach einigen Minuten sollten Sie die Lieferanten in DocBits sehen. \\
