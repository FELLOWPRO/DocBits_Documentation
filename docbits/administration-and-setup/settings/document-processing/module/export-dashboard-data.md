# Export Dashboard Data

The **Dashboard** can hand its list to you as a spreadsheet. Once the option is switched on, an export button sits in the dashboard toolbar; every request is queued, prepared in the background and listed in the **Export History** of the dashboard settings.

## Switch the export on

1. Go to **Settings → System & Administration → Dashboard**.
2. Open the **General** panel and scroll to **Dashboard data**.
3. Switch **Export Dashboard Data** on. **Auto refresh dashboard on document updates** above it is a separate option and does not affect the export.

<figure><img src="../../../../.gitbook/assets/dashboard-export-settings-en-20261104.png" alt="The General panel of the dashboard settings with the Dashboard data section: the Auto refresh dashboard on document updates switch and the Export Dashboard Data switch, which is enabled."><figcaption><p>The Export Dashboard Data switch in Settings → Dashboard</p></figcaption></figure>

## Export the list you are looking at

1. Open the **Dashboard** and set the filters, the quick search and the columns you want in the file.
2. Select the **export button** in the toolbar — the icon with a table and an arrow.
3. Choose **Export to CSV File** or **Export to XLSX File**.

<figure><img src="../../../../.gitbook/assets/dashboard-export-menu-en-20261104.png" alt="The dashboard toolbar with the export menu open, offering Export to CSV File and Export to XLSX File; next to it are the other toolbar buttons and the Upload button."><figcaption><p>The export menu in the dashboard toolbar</p></figcaption></figure>

DocBits confirms the request with *Your export request has been received. You will receive an email with the download link shortly.* You can keep working; the file is prepared in the background.

The export is not a copy of the screen. It uses:

- the **filters and the quick search** that are applied when you start it — the Export History later shows which filters were used,
- the **columns of the selected dashboard**. Column changes you have not saved yet are not in the file: when the dashboard has unsaved changes, DocBits warns you and exports the last saved version. Save the dashboard first if the export should follow your new arrangement.

## Follow an export in the Export History

**Settings → System & Administration → Dashboard → Export History** lists every export request of the organisation:

| Column           | Meaning                                                                     |
| ---------------- | --------------------------------------------------------------------------- |
| **Email**        | The address the download link was sent to.                                  |
| **Status**       | `completed` when the file was built, `failed` when the export did not work. |
| **Requested At** | When the export was started.                                                |
| **Completed At** | When the file was ready.                                                    |
| **Format**       | `csv` or `xls`, depending on the option you chose.                          |
| **Filters Used** | The filters that were applied to the list. **+n** shows the rest of them.   |

<figure><img src="../../../../.gitbook/assets/dashboard-export-history-en-20261104.png" alt="The Export History panel in the dashboard settings: a table with the columns Email, Status, Requested At, Completed At, Format and Filters Used, showing completed exports in csv and xls format and a few failed ones."><figcaption><p>The Export History of the dashboard settings</p></figcaption></figure>

If an export stays on `failed`, start it again — a very large list or an interrupted background job is the usual cause. The dashboard itself is unaffected by a failed export.
