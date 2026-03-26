# Watchdog

<figure><img src="../../.gitbook/assets/watchdog-infographic-fr.png" alt="WatchDog Infographic"><figcaption></figcaption></figure>

**Installation and Settings**

After downloading the WatchDog.exe file, search for Command Prompt → Run as administrator on your Windows device.

![](https://lh7-us.googleusercontent.com/a2kmyk7eD7HqZfPiLWmvSGFnpzg9oHejHe5TpE6gFwErFyJYYBB5BZjqopwr-cEqmlMvaW8-PgARZUGI9KMKHSkz-lU\_C\_w6aHrVA4Wqhwo8WBSqnBfVvCpSckqLu4PwUriGs1MxbKHBBkuQ2pPaVRM)

Once this is opened, call the file by typing the path of where the WatchDog.exe file is stored on your device like below

![](https://lh7-us.googleusercontent.com/W\_jDgPVTtpEW96jR0w\_ibnZGY2CVwF2nAN0nEjMW3liw10bgPGlADiVR\_lWyEAlfGYRD--gSQMdEqboRlMW5TAEP6Ao3GOW-hP3tQimA58K9Uh-WNZf7i06YYNqk5\_EgKERYkjMzPx1Xd56qH2Pw8wA)

Type install after the file path and press ENTER on your keyboard

![](https://lh7-us.googleusercontent.com/vZQxNIh\_wY2SFTznxNTboFOSePmEMqXQMWbhsSoO45B\_mIh\_6C-yjfJ4SPleBIIV4p943XBN1E-3HJBgFXRRABVfDX9Ey-dnb9c5KYaNleOmE5x1ocK32zLQ4luc71rmcbv7V\_dQ8pEtH\_WoWZkN0fg)

You should receive the following error message as it will start the application in UI mode and there is no configuration present yet.

![](https://lh7-us.googleusercontent.com/HmudHszeaiAj3xIlb1Oz1IXPh3Kz1JovUvPjkr9UI7EwSGbGWRK7xVhUNwc9LGlt3t1RRVR0l7DFLfG\_Ob2b8Yxd4DffLb27Hv3z22tzf9LqDVTn577CFV-4Bzs2P\_vTsGDJvtNzf8XW0wPiaWLDj2o)

The application will automatically open up after installation. At the top, navigate to Einstellungen (Settings) and here you will see 2 separate sections.

**Folder settings (Ordner Einstellungen)**

![](https://lh7-us.googleusercontent.com/8uSWIY8EJKPrKj9Zk5buY\_ByE9fu2oE7mJ-shG1VB2n7QWyVLAfDfUFdj-Jv3hBq2ncf2Ls1Wh3Lm7Kf-TFqet7yFso2S6srnZev-yzVdKjUxtCMTt2IUtWvUwUU0LMGktA8ioBfIkkZGqG4f53yYHM)

This is where you will configure the file pathways for where the documents will be read and processed. The read pathway will be for the documents that you want WatchDog to extract and process, whereas the processed pathway will be used to indicate which documents from the read folder where extracted and processed.

**General settings (Allgemeine Einstellungen)**

![](https://lh7-us.googleusercontent.com/mTUxSXPBZi\_TTtVEQbGQXyXNonkIuganpTjqaamkB7C7zZ7Qaodvf9Sl8nXjnp6ZpYNf8XOwvuk-MYYEyGkFcKB-SqC9lklBXehC-3jMI7G12tXqfa6ROWywPBFE4fy-p-DcuLo3QdZXy-1rjSzlu9s)

This is where you will configure your DocBits application with WatchDog. You will be required to enter your DocBits environment, API key and the document type (as indicated above). To add more than one document type, separate the names of the document types with a comma (INVOICE,DELIVERY-NOTE,PURCHASE-ORDER, etc.)

If an invalid configuration is entered for any of the fields, you will receive an error message like the one below.

![](https://lh7-us.googleusercontent.com/BIOMuVCPUojfwPVr-cJukzvoBdWdtxzj5XCXocWlZwbaXwkTpb4u5Gk84vKu-\_Z5UxvZ2cq0asHs4aFRLklBrUOKA19d2R4nqsxyZjd3iJlh3y97f07OfzEyv6jl7JpnorANzdPIgyZfqwmCEYZOlek)

Once this is complete, go back to the Command Prompt area and re-run the WatchDog.exe file and this time it will be correctly installed due to the configurations now being present

![](https://lh7-us.googleusercontent.com/GqtwbyvQjjNb1u9DY\_Eww2woOdK1nYMm0oRMFxEGWSP9oSYN51eu1kkWiDzenz1rHGLvYG-ocwosOK2bTM6ruXTI5co05kjV2HPGI-8TgEIBTVCPpTrvs37SKMk9eBWY0KEj9vCCyPeqXYgCVD0DDXw)

To start the application is UI mode, run the following command

![](https://lh7-us.googleusercontent.com/LELZuaiuL8ukiKPE-pbezsOZAICffXxAomx6gSe0vOvYaIdkr8Sr7X2znc\_Lb3G76bh11X6kGPizWzoA05L-nBwUcJV8NNLUgQuGOf0TyICmhyL4syhnZFGu82JP0a3dORlQXz9MnTA\_f-8b6oy8v6g)

If you just want to start the application, run this command instead.

![](https://lh7-us.googleusercontent.com/yHiO-x4CPGIjC9hRx6o-Wr5lAYiwjGi0vNBp3faB91OYIqm8TTZcz3SVDgjSmq\_7TN11aVCsNHoHV5sR0FHsA5DJqxJ74z3lAmXoaDkkMutl7yXj4fCoabX-9SwfsWJwOaooiVZhCvOKFXvJOCBicEA)

**Auto Start**

In order to set up the WatchDog app in a manner that allows it to automatically start once you turn your system on.

Simply open “Services” in the settings of your Windows machine.

![](https://lh7-us.googleusercontent.com/IEqq96LGZ9lBz2E0ApDrTz5huYutY7G1DecXLwhkdIF0pS235RN9HIqcehuJvXv5tyLdOnobhM\_VNeMFA7tnMhwvWCnFRU5G14cHWN1swA4ZYF1rjvKzZtFMaCK2MDsPebvIz3MejDwjiYEiQ-\_BQyg)

Search for WatchDog in the local services and open the service (double-click on the entry)

![](https://lh7-us.googleusercontent.com/qOtVCqR-zytJw2zifnjHmW\_s5Hl6ijJt72d3PRI\_euZU0H3wA-QD69mSFOnyDEnCVJXblEeA\_Zbh5iQsyPa8gPJ85TY8wz-Ir0aMd2SWoKizKw1G4yi9jOmtxZG7-9EZbOvborv45OASD6zSa6lLbAk)

In the above menu you will have the following options for automatic starting:

* Select Automatic, the service will start on boot
* Automatic (Delayed Start), this will wait 2 minutes after boot to start the service
