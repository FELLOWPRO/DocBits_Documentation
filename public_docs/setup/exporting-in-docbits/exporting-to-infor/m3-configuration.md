# M3 Configuration

## Prerequisites

You have created:

* An ION API Endpoint
* An ION API File
* A BOD Mapping File
* An IDM Mapping File

## Import Mapping Files

Before you setup the dataflow, you need to import the mapping files into InforOS.

In ION Desk → Connect and open Mappings

![](https://lh7-us.googleusercontent.com/EV8z6b\_W9tjTgML0j3qJAYHCTYLd4N5yLrArdIECftYpMOCRTRJ\_a7eADEzljFM4XHxMUJ6Nx9Z6EN3Hmzote5F0HrM5zd4p1BS0NYicUWDnkhQFX-\_3MGbblEYi6x2a1K25SclYYttgW3cWQbOjvfQ)

Click on the Import icon

![](https://lh7-us.googleusercontent.com/agBHtjNitneogoZsSG1791QAARbvesv9eSriAkw0HL9Fy372Ty6SmQG1sKJjOYZCuE0SnGT3agHAFRJYjgGNxJrN1CMJj9L-fSPhNmXxN78iDKqrrdgEVYFHxsNwy9XLiUFpBCQ1wnWlwyeFH08DsWI)

From here you need to select the various mapping files you will need which include: SyncCaptDoc\_SyncSuppInv, SyncSupplierInvoice\_LoadSupplierInvoice, and LoadSupplierInvoice\_ProcessSupplierInvoice.

Once you have imported all the mappings files, make sure to approve each of them by clicking the tick icon within each of their squares on the Mapping dashboard.

## DocBits to M3

The next step is to setup the Data Flow in ION Desk, navigate to the ION Desk application and select Data Flow → + ADD → Document Flow like below

![](https://lh7-us.googleusercontent.com/Kkro7w2LPfnwf-JPMmPI2DzrSRNEi\_F9aWW02KDtBvAZz\_R7j9DZ71Nqw3ETPSQqDuxBzJ1TU8Uuzz5jU9rOO\_tvDBf9abVF-FDSxln\_pjr-HMRdYBnGMwgcM6hg-pC2B7FgdBkXibivMB4PptvZ6fk)

You will then see this page, this is where you will build the flow of information from DocBits to M3

![](https://lh7-us.googleusercontent.com/K0B1lC\_KLO5RZqGqAltp6JnZZ1sfZG4wg-i\_nxZCnLjML33yvViRUHOInK3iHYbzbV4I0uqDY8JpsZMxssD8bbJy24A1zKr9PfQEyqVxewx\_L87RCIwzn5MDRjMqgx4X42vkKthbyz--5DDe1H0rvHQ)

An M3 data flow will look similar to what is shown below (there are 3 DocBits applications and APIs due to it being used for 3 separate environments).

![](https://lh7-us.googleusercontent.com/6Oy\_UBzYNml-7\_sayDEKhqYF92yDzlUNzmGLQSWZOfDT-avvfg3oNUnv\_DtXNSP0XF43D-zgIizIuTrCXl6ockLU2uQLYFJna72fzL5BP-T89xjF4oWz2eAz9w0hsoVieyTpgSw\_Prvj--89Kc4Kqoo)

All parts of the chain are dragged and dropped from the top section

In the chain, DocBits and M3 are both Applications whereas in between them there are mappings that convert the data into a form that can be understood by the next section of the train and “map” the information so that it goes to where it is needed or meant too.

![](https://lh7-us.googleusercontent.com/1kjgKNmIQ-NbM\_JukcPsj7qmyiMB9b693ixg6Dh1kOlZ6NKgBXViYwn0MNUBHt0WKKWf\_1gpRvxgqjIaqpqcy-SyXoYjhJLt3m\_bv7wbVADzqHRsx8TYXWyIQO82X-Ixfl5b7iI7nxTRkw06sX3xsBM)

### DocBits Application

Give it the appropriate name such as “DocBits” then select the plus sign and search for the connection point you created earlier such as DocBits\_Export or similar and click on it.

To create this connection point, go to ION Desk → Connect → Connection Points

![](https://lh7-us.googleusercontent.com/8qsMIUKMrgmcYqqJPL2zF4GVeHuvSHvn8Z7dfonRuvKFPcXmN4hx2PIrXko4lvW7ayD7s2VRFOMvWkQSxfAH5tTuhg0XhzYmSzlsgnowWRw8GmQC2y5BjcS9X2MjDzLSutgoHg2VN59kCYRunMSxkIY)

Click “+ Add”

![](https://lh7-us.googleusercontent.com/-3-3TzgEQppYmX64-clxjp1JBjNz9fsA2FDPqirgNF0wL8DsDJACzUBuSw5wBL2k9JanqvMzAG352CWafOdtjhMfZalJnBFVSjaWA1AszhCjKtCsTvLUUqq1WwMfF-PqL-u7LRo4TPbj4fP2\_j48240)

Select “IMS via API Gateway” and fill in the following information

![](https://lh7-us.googleusercontent.com/wImUEi9mXiQjW5O6mp7\_IrKk4CTaHFs903DJ6TXqUEcjGq45TnUWdusFTGH1jzpBPP\_TC7rokyjrkYWmh3emSKBQs05qYbO80TO87De0C5OveVURykQMCLFRRYakEMoFHpoeXzxH5QIbKJdjxujeY98)

The ION API Client ID is in the ION API File you created at How to Create an ION API File, this can be found by the “ci” value.

Switch to the document tab, and add the Sync.CaptureDocument BOD to the DocBits connection point like below.

![](https://lh7-us.googleusercontent.com/ga1q0Uwdi2GNwuiz22NvDtCzGL0krSkBPLsEVxE-mtoMV7CtEU8TPO0PhF40oB9NB9iv7DCJi9niLnsKjpqarWJsgGRdc1W0pFl9rTDm7i2\_BSLj3JOrzR7iclPdqOdpztgCxWZG2Teg1gWljaMUq2E)

Then save the connection point by pressing the disk icon in the upper-left corner.

Navigate back to the Dataflow section of ION Desk to access your dataflow. Your DocBits application should look similar to what is shown below.

![](https://lh7-us.googleusercontent.com/fBzKL6RU0XvGpn1cKFZIyAp2amKonBWc8ilbAq5u\_r867xywWWAD7EjP-g-wjlwUsrG4Wz0lS6Ujdnu8P3vc8Q3FbtbRR4qSBmbSLoICfX-aHITMDdHp07bESefC9TuUUUQiHGb1j00HNtB\_7A3iDFs)

### Mapping 1

The first mapping node should look as follows

![](https://lh7-us.googleusercontent.com/F9AcE4V-s9vs-0kRz8BcCtdHUUQoaooyK3GqOj8pAQWuvIguoUO-tJx7WBEW6\_GmzwNsJp8VUYezGCiLPXvPhEynac3FPh\_NJOvqs1SXtMIUsF5\_HjWmcvY3VC-eZsjG0ZE8HmsKsFhocadr96drSbY)

### Mapping 2

The second mapping node should look as follows

![](https://lh7-us.googleusercontent.com/8M\_V2BtkOGyqV-828ct5c2QvSs5n5\_RtLjlH717kspZwlgtfjbz6tpOJCCXDelruBenMjxsJPqncQ5hUw2bQkM3ya7\_WrVyEBz3UnaU-C9oVOWB8nNtXA20RBYgO3EBMon2TfgpefY0lSPBzF9NoTeU)

### Mapping 3

The third mapping node should look as follows

![](https://lh7-us.googleusercontent.com/x9QUHTgQrNaeKnTeMIUflkWjcBr2c3LgsYe2BZBjv01hXiEkvsLtU0GzYt5KppcE12ZqxWeBJ1kbLOC6qA3yKHhujCZt3sFpDNE5yERkHHMJJEjFl0jJE90nQ-iXeMLbR-Bk6G0NIL8AqG3U48Seiuc)

### M3 Application

There should already be a M3 or similarly named connection point created in INFOR so just like the DocBits Application you select it by clicking the “+” sign and it should look as follows

![](https://lh7-us.googleusercontent.com/JTXIN5QxidvFJyjegxSw8kA7yVfHfuypxi5yX21CsSlGtOVgykc52U2r0077-cKqNhc0B4zSSZotlipFesmLo371kho3wUSRPzmwEir-stbxyZV1PwCDXkq6qJMm4PNXt\_wGarDMixGIU0tu-eAqV5Y)

### DocBits API

You will first need to create this API as a connection point which is done by:

ION Desk → Connect → Connection Points

![](https://lh7-us.googleusercontent.com/VOXW6LixmcKjHW0CTOO5L8fK6r-4k3jqk0AnoR6DEVoGgJMbx65hS3yKSgMWItypdz4Ha82T-bKCN0aMv34gif-b0Aw7zpDFPBK9G-K6x9\_csrM9xyKcpmWam15tKqO1\_rwKtMsJ2CSoWqdpLxCD5tA)

Click “+ Add” and select API

![](https://lh7-us.googleusercontent.com/c1RAUNoA3YBhvf6FLJ\_L3ouyZwHK-3bBRU83eL3oAQXjG6SjWEO9O-gDKPItPm8AI\_YhadaCZU-GxY-qUXNuQMiRiKUhBYUtJ8kOFVg\_YYpzJDSoJ68NYSaEtHBSyyfnq0VbHUdWY1e8lBQ0j\_G5xvI)

The information you fill in should look like the following

![](https://lh7-us.googleusercontent.com/h2KU6pKeKl9wX8oyul0KmbL\_kg-iPQJpBqbf29l64ED2e-Z4tNj8-m4hBN\_4SSiNPf2TrE92TD4H0-0AZ0eWxMFmDV22IdPlU9NO4XlQF9k0Swg0X3Sm1HMsSPvWi7Q1HUr8uy8j3aDRheFxZqZ2Gbc)

Switch to the document tab and add the following configuration

![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_api\_docs1-1024x279.png)

**Acknowledge.SupplierInvoice**

The configuration for this BOD is as follows

![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_ack\_11.png)

Make sure you have selected the “Send to API” option in the above menu.

![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_ack\_2-1024x338.png)

Lastly ensure that you alter the request body as well to look like this.

![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_ack\_3-1024x260.png)

Repeat this process for the rest of the BODs, each configuration is shown below.

**Sync.PurchaseOrder**

The configuration for this BOD is as follows

![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_po\_1.png)![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_po\_2-1024x359.png)![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_po\_3-1024x297.png)

**Sync.RemitToPartyMaster**

The configuration for this BOD is as follows

![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_remit\_1-1.png)![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_remit\_2-1024x351.png)![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_remit\_3-1024x299.png)

**Sync.SupplierPartyMaster**

The configuration for this BOD is as follows

![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_sup\_1.png)![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_sup\_2.png)![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_sup\_3-1024x295.png)

### BODs

![](https://lh7-us.googleusercontent.com/zaDSnm844wXqyefN58Y1DvuJOnMaoOrYQ\_12Z5ZSng8-TPy38Th2ZPdAD6hyIYCOvBKGPDSvGpTmtBPq4K5IwyGtsKyMvk-CKOuY-hzD-RL7UrsG39qLN7m3\_IDcDS66KeIQF5e70OWlHO1cbVvQUXM)

The following configurations should look as follows:

#### First

![](https://lh7-us.googleusercontent.com/5gLpbQEYYW90dVLkSc5V60LeToMe2wcOcHHtwTdIdT0o0Gktu8T\_7i7zfNikjgETM3QmzAsJAknlEGeB0W0YFLLi56g2PKPwyr2zPcHaKdu8XJWHgaC1u4--\_CHNYfd1wQ\_\_3kZpv1\_PwyZty3JEyak)

#### Second

![](https://lh7-us.googleusercontent.com/xbWTcP8hYA72Ijt7\_IV6l-9jKeSalbRPvTn7aNVcnWYMQcD2RDjM-EzKpBKjSIKF\_-r8BaxmmCo9uz6-E-vC9flKb4toU3SH24EPLgbXc-VcfJeDdJKglf5P6WV6XYZg0cZVWAoyvS8qgtuR6ZqJYlI)

#### Third

![](https://lh7-us.googleusercontent.com/F8wVWXuHkLLW2kuu\_7Dxe9LhyYdm04tl\_\_Sp6FjeTyk\_JFUzhCIUhVlKS\_cq3I3FP\_h2ksV4zEJHFC\_KXK6sSZ5iz5yhTFZcPnH1HS\_RvZb2Nr-UXYQ1H316UMoj6eRv6wMn3wHX842B5WVfPHVnJ74)

#### Forth

![](https://lh7-us.googleusercontent.com/myhi9y2sCvS5ZFkIJa5ysLbu7p0X6CYqbiuJ3sQ5-O-2QWlfAseunjwhXK0kakmAofplm0zmh\_H1Np7bA559w0-jdurQUsZwYF9CyKYSKSeGnQaIit0HQ5iN-3Xv8CIC-5nk6mMj3JTDS97SlzbsOFE)

#### Fifth

![](https://lh7-us.googleusercontent.com/c-5iaUhhx0swH-mQfXE5Mdwe4J0skGt7mst4kJdOpjL3Uat329TZmKM5Af-lGQWmcmBht-ib\_aUj4dVG7GaUAHHULjly3jxsR8MJNnLDcu5eZB268Vy-dXPxHmkVB8dMZTRhU5SUB59AREurJlW-K6o)

The last icon should be empty as it is not carrying any document or information.

Once you have added all necessary nodes to the data flow, press this button to activate the data flow (after saving the data flow by pressing the hard drive icon).

![](https://lh7-us.googleusercontent.com/WIecHktG7e5dbVScLbR8hUcZUdCEWXBW4xWDEuq0IqTMmguA\_Ih\_oRymvpk6CzowWFG5TTSCPIH-68ICnPSOPxeZksc-n4bmpvuH8dvHuHFU1DlppGRno3PKjCSJiK12p9bNlo\_9cN2t9Ps3nbqF3xE)

