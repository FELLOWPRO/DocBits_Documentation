# Postman for DocBits

This guide will show you how to make HTTP requests to your DocBits organization via Postman. It is easy to use and very useful for organization administrators.

## Setup

First, download Postman to your system and sign in/register.

Now follow this step-by-step guide to learn how HTTP requests work in Postman.

Authorization in Postman

Before you can create your HTTP requests, you need to enter your API key from DocBits to authorize them.

* Click on the \`Authorization\` tab and choose \`API Key\` as authorization type.

![](https://lh7-us.googleusercontent.com/L3GaBZJvReeINaKbkq3VYQ9UHTBoKUA3nJkfyLqk61q5xaOJnmMLhbrEbgUgLEyYRkewHuLIAVzoYCZ6quHq0pwx\_69FEYJjzYllivB8WzdAtTFSrzl8VeFthbMsEB9sGjcGlVN38DXEXUwuNEPL6hg)

* Fill in the values. Enter “X-API-key” in the \`Key\` field and your API Key as value (found in DocBits Settings menu under Integration) Select Add to \`Header\`.

&#x20;

* It should look like this:

![](https://lh7-us.googleusercontent.com/SmNfci4z8ECTeXzFPE9YQ8nCzCRHglc\_7RR1cN8a8F7KvYWjJcBnY5wpl7q0AV8bfNLkMk8F4F4aw8j4xMK50HJweBRBPo8EasTn-FG-fmlUJQ41aUX-dvTeWP\_xJQThi8A6EwJl3qIc-Dw1B5W9fVE)

### DocBits API

Available at https://api.polydocs.io

* Click on Authorize in the upper right corner

![](https://lh7-us.googleusercontent.com/kuztHpkmRWlOYSU27r97KH15SJHPF\_hn\_eX3C1DYLVYCwMHXfLjYSyFubUCvlQiBt5q3xY0XBPmkcP6AnKF2C0Mdtx3tg\_dU\_qxqAmI6axYIsXR36\_YBz6j455K3-c2SBu4YzmYIXq8VXQxzgL-0j90)

* Enter your API Key and confirm by clicking \`Authorize\`

![](https://lh7-us.googleusercontent.com/zLhgpdjMnxqNBdjgtDxFEKglICIZul7dgmfFFm2hSnsDQ-HsZHRKRikZ0lcanGYkkZj4waC85mEUFO951ydVnY\_\_m\_TrMrsK3vrDv9FKL-adgWL4lJqp3cSxPeClBm9IHG2cXinRsv12xTeh3psQfO4)

### Create a new Workspace in Postman

* Click on Workspaces and create a new workspace (you can name it whatever you want

![](https://lh7-us.googleusercontent.com/3rZw7jhOgVpkZuer58fPEKqDspJjK3S1lp3XpQuvE4c9212a0ALB-p7oLRwPqEbj10MpoCWsb7V9fPqiAdVvigE00x9mN5-lHFXZVVxlkeroBJd2ratgkJVJDM4LJkUJsycyl6tnFKazcFPY-vWtH2Q)

* You have to select the visibility which determines who can access this workspace.

![](https://lh7-us.googleusercontent.com/ZajvDtMvfM5J\_Go3n\_PgzD3RXTMQAlST8\_3WnsTQ4-iw7e0QdAa3wqFk7Y0gt78IJVjNTN-5E72c1127CpXJWb8WbfDolxENLqxg5VZLPEK7-hxsNwbAyMceSHfeVy6v-b9QT0kFwnMibWndEAJ2lXA)

* After making your selection and clicking \`Create Workspace\` select Collections on the left side of the application and create a new collection for your HTTP requests by clicking \`+\`.

![](https://lh7-us.googleusercontent.com/mbC5t86vaB2G7FQp-40XN-SHc019LKitfUeXRzbcG4HpNai5FPapShx9swHX3mz0va8QFsUQiYn-bhjvER0XYOEDRJpI9x3wG4NgRZCd4beU1NyKJd86bSGubxVbRCtz8HkTDZd28Z7Ice3rmscFMMo)

In this collection, you can add multiple HTTP requests. To do this, click on the 3 points of the collection and select \`Add request\`.

![](https://lh7-us.googleusercontent.com/S5W75clJz7JqoIWPbKBjrJqpTAwjS51Pu4dTU160Q7i6oW-HPnb7aN8WRK2AyAb6-HEqTYMZTy9563P0sq53MAjGpVg1JivZX2ATHa6GeFbTX2UCjud7ot8Y\_ksBuUbUfyEfxIDziV8TN3zDfX9Se58)

## "GET" Method example

The GET method is very useful for getting information about users, sub-organizations, processed documents, and much more.

* Choose the GET method in your HTTP request.
* Authorize yourself as described above.
* Open https://api.polydocs.io and add the path of the function behind the Polydocs URL. For example:

![](https://lh7-us.googleusercontent.com/pIdgyqP7g1UwZbY5yaz1KAnKe\_ESs\_kQyiWAXXM-ukRKakS\_\_OL\_LS9J-07hZnZDf8QqtoN\_lKyuhvOIIIF-4Wp0dkofZYQwXZ0hu2RM0YogRxJah-zf8W\_cDNFf8xsec1tYIsfe0SpBuvdCG4WHMU0)

* Now paste this link in the text box next to the GET method in Postman.

Click \`Send\` and you should receive all the information about every user in your organization.

## "POST" Method example

The POST method is usually used to create users or organizations, for example. This method inserts information into the database.

Create User

* Select the POST Method.
* Authorize yourself as described above
* Open https://api.polydocs.io and add the path of the function behind the Polydocs URL. In this case:

![](https://lh7-us.googleusercontent.com/Gwabl4pN0k0NanHsFOzJj9s2H7ExS-JcWr-Y4EW0FLUYHfnaOZoMWvldJ6yDI33p\_DThVx0Rd5bi59XdOK11l1knc5rd-E5HXMw6v5E3qvHvKVWHlp21S728SVye6KU2W5ZeXtCIOzxBAcMlA2UNFfQ)

* Now paste this link into the text box next to the POST method in Postman.
* Select the \`Body\` tab in your HTTP request and enter the keys and the values ​​for each credential that has a red asterisk next to its name.

When you’re done, it should look like this:

![](https://lh7-us.googleusercontent.com/lSExzZSbTcSRvuLDw0HNYE62yI7xs0eUewKuOcABCGYfsRBRbGz1lJxopR4QdUEoniCnZ83FKpz-AHLORP5cXGPrPhgouzE6zO920jA7A3r-Y14wY\_Gc3C98R2fcxXsWRMcle9qT981YWhCnjlUukPE)

If you want to create an admin account, set the \`is\_admin\` value to true.

&#x20;Finally, click \`Send\` and you can see all the credentials you set in the response below. This means the user has been created.

### Upload Document

You can also use the POST method to upload a document to DocBits.

* Select the POST Method.
* Authorize yourself as described above.
* Open https://api.polydocs.io and add the path of the function behind the Polydocs URL.&#x20;

In this case:

![](https://lh7-us.googleusercontent.com/-EwhMeH\_WXYVmMKus1-IZKLZNyTcYktcf\_YUT\_m2nfStfKXuBxKBb1MZfUIQCN4ZxNKQkNhvO\_pgnt1EUhNB34qG5AOe4wM0OxGRMQsV9a8h0XUgabqq8mLQhza\_AE7gxBetmb9bJmaWBQqEXrWT0VI)

* Now paste this link into the text box next to the POST method in Postman.
* Select the \`Body\` tab in your HTTP request and choose \`form-data\`

![](https://lh7-us.googleusercontent.com/TNrKlyorn\_5YrIu5r4vcfyYgAnfhsl-SRVqWg9RoN0X1pUjXtn6J0EI7aeQ-oc2ZtFeTj8POcMXy6CwXzI1jhv-ufb2u7d80SC-lbGXmnx\_jVDunAbRw1jqAsB4PPsEzcFIOPeH5PJZvytUW2kIDYZ4)

![](https://lh7-us.googleusercontent.com/scAJpTSCqYSKYNNGPIrEsL0zDJIa7Dhe9tpqv\_zDjdLyAydugzdGA1s93njbFOOVbVbQf7oDEtRc14Kt4p1TXX8A--WjvRgeXWsAxDNWdrCN2-QDeya6-FFEG4\_-dhYgrj4yrVYllJs8eZsUgKOPvzo)

Enter file into the \`KEY\` field where you will find the hidden File dropdown. Select \`File\` and move to the \`VALUE\` field where you are able to select your file by clicking \`Select Files\`.

When you click \`Send\`, you should see “success”: true in the response.

It should look like this:

![](https://lh7-us.googleusercontent.com/hNtG\_uTWgxww7iOmHLhnDqdrTlHCI1rk31LozG4l2DLPqxzSn9HoKn8CQIjeBgJLV4bxrGCjWOMRykJ3qBdZLYwxrZJGq\_S3tjVwSZmGTiMgVoqM97TTQjmW8CegEL2FV309NBmV0Fv\_vciSdQRFiOI)

## "DELETE" Method example

The DELETE method is used to delete, for example, users, organizations and so on.

* Select the DELETE Method
* Authorize yourself as described above.
* Open https://api.polydocs.io and add the path of the function behind the Polydocs URL.

&#x20;For example:

![](https://lh7-us.googleusercontent.com/-QqSVIELl1IkxYK\_gGDa7nIv\_B1IvO3OjT3Ge6bAXwPl6jVDETuzXwtYJdRSmqLEP2d6B0L6MuwZvgJpI968pzp1APmJmuQ\_qlqYgZZhesocYCJVMCHhIZAKmlvMybUkUGXYZtySrnEbRTwWTritvKo)

* Now paste this link in the text box next to the DELETE method in Postman.
* Replace the {user\_id} at the end of the URL with the actual user ID you want to delete. (You can get the user\_id using the GET method).
* If you included the user\_id in the URL, you don’t need to add a body key and value for it.
* When you click \`Send\`, you should see “success”: true in the response.

&#x20;It should look like this:

![](https://lh7-us.googleusercontent.com/X8WNtsC9v7jqDIiaVhauJUgZK0yTC1GVz9rBptdiCxyLUiEEfbpIoYHpK7NvlDMTkhgiPyBb22H9GOfDdvmL-dakouTjuRDPwX4YX0Jz5IIo6eHu-wnw1S4jJd5ylHyffUXWKwX6ovDnp\_2WEAtSha4)

## "PUT" Method example

The PUT method is mainly used to update user or organization data. It is very easy to understand and use.

* Select the PUT Method.
* Authorize yourself as described above.
* Open https://api.polydocs.io and add the path of the function behind the Polydocs URL.

&#x20;For example:

![](https://lh7-us.googleusercontent.com/tC3qtPbFb1GsK6dBmB5Jrv5HqFOYLxNR1XB0PEuA8ipkHnH2ZQ6xrrkImNgbGSMoA6aAGvLr6K3cI4u\_qM96BOvR7AnQzmX17HBMBneNpLBc6RIzspfTYgrCWSj0fSE9mSWLIex3hc\_R-m-PI6zT6Rs)

* Now paste this link in the text box next to the PUT method in Postman.
* Replace the {user\_id} at the end of the URL with the actual user ID you want to delete. (You can get the user\_id using the GET method).

## Change Email Address of a User

* In the body, enter “email” as the key and the new email address as the value.
* Then just press \`Send\` and you should see “success” in the response.
