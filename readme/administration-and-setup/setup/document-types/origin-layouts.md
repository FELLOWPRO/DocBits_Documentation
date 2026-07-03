# Origin Layouts

{% embed url="https://youtu.be/-m45XGiIeig" %}
DocBits Origin Setting Explained: Country Standards for Dates & Number Formats
{% endembed %}

DocBits excels in adapting document layouts according to their geographical origins while standardizing elements like currency formats based on user browser settings. Let’s explore how you can leverage the Layout Builder to customize layouts for different origins, such as the U.S. and Germany.

<figure><img src="../../../.gitbook/assets/origin_layout_1.png" alt=""><figcaption></figcaption></figure>

## **Understanding Origin-Based Customization**

* Currency and Format Standardization: Regardless of the original document’s currency or format, DocBits converts these elements into a standardized ISO format on the server, in line with the user’s browser settings.
* Geographical Layout Customization: The system allows customization of document layouts based on their geographical origin. This means you can define specific fields and formats for documents from different countries.

## **Example: U.S. vs. Germany Layouts**

* U.S. Layout: For a U.S. invoice, you might include fields for city tax, aligning with the common tax structure in the U.S.
* Germany Layout: In contrast, a German invoice layout may omit the city tax field, as it’s not a standard charge in Germany.

## **Using the Layout Builder**

* Select Origin Layout: In the Layout Builder, choose the base layout corresponding to the document’s origin.
* Customize Fields: Adapt the layout by adding or removing fields. For instance, include ‘City Tax’ for a U.S. layout.
* Apply and Test: Once customized, apply the layout to your documents and test to ensure accuracy.

<figure><img src="../../../.gitbook/assets/origin_layout_2.svg" alt=""><figcaption></figcaption></figure>

## **Tips for Effective Customization**

* Understand Regional Differences: Familiarize yourself with the tax and format nuances of different regions.
* Consistent Updates: Regularly update your layouts to reflect any changes in regional regulations.
* User Feedback: Utilize feedback from users in different regions to refine layouts further.

## Applying Default Layout to Multiple Origins

When you want to apply the default layout to multiple origins, press **Apply Default To Origins**.

<figure><img src="../../../.gitbook/assets/origin_layout_3.png" alt=""><figcaption></figcaption></figure>

A popup will appear where you can select the origins you want to apply the default layout to. You can use **Select All** or **Unselect All** to quickly manage your selection. The popup displays the number of currently selected origins.

<figure><img src="../../../.gitbook/assets/origin_layout_4.png" alt=""><figcaption></figcaption></figure>

After making your selection, click **Apply to Origins**. A success message will confirm that the origins were updated.
