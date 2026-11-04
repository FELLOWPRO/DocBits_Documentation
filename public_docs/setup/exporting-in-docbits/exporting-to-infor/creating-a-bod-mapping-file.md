# Creating a BOD Mapping File

Download a BOD Mapping File and open it in your applicable file editor of choice to edit it. For this walkthrough, VSCode is used.

## Editing Mapping File

Change the company to the correct one (SFV\_AccountingEntityID) and edit location ID if needed.

![](https://lh7-us.googleusercontent.com/eJQI1CKlxEkS_Pwp0VH2hgS220b-q8NSFG5iJKpLOL457qTN3CbUB8IHTw1lRinbB_kP00UUNgepWNsbh3_Ko-SExObePjqmxP7ee_lQnADTtDmxEtRM_S7AONMbcpjwtnHTakYd1Q06GVm2G0o-UDA)

Check the document code by going to the field settings of the document type you are trying to export (found in URL of field settings of document type in DocBits like below

![](https://lh7-us.googleusercontent.com/AhU3i27qFS7BMCgpNQnmLWAjcIWHXHOlxMKqd2Yob5RQKa8qysQQsSsacr6zao4cnAh3DISPgYu1GnjubIJpgtAdiBR_0vy3WJZXPY-HeEfVQkWnlRI9UEJWMPQ7DbWYLQhz339BOlbd4KgxU9B_CPE)

Lastly, edit the SFV\_LogicalID which can be found in INFOR ION DESK → Connect → Connection points and select the DocBits\_Export or similar connection point and within that page you will find the Logical ID you need.

![](https://lh7-us.googleusercontent.com/f50i7pzRuZULJ6shehba0lWIWFBTsPZyip-LQxAYJpYDXK66SlzdGOpdEG-wqLQfqXMgMMhm5SAvj57UOCvF6xf2OMCXtFiEEKr9yiQr4xtv8vbV-NGcLuJwuQ9zHMBBKfTktAp1nSfBJhdPeAu3RWc)

![](https://lh7-us.googleusercontent.com/qyEt4iYRIjOZCCrVbImeK6EdZGun2YrAy8li8u3tulcD8bwzl_sl1TiEXKqbik-4MxnbV_MCwltvuA2WAgzzvDpTVd7W52he9QD9IK0qijoz3ZihUYcWJlqlD5kbcsRTj3SfP1CDqcyhoFfBeiE1Xfo)

## Create Logical ID (Connection Point)

If this Connection Point does not yet exist, you need to create one.

First, go to ION Desk → Connect → Connection Points and click on the “+ Add” button”

![](https://lh7-us.googleusercontent.com/fQPmV8KgffyWhM0i0cQlyh7fyQe37p8uR6C_pVD5SboEx2emIJX2212GXqk_KT71DfYMKSjkfYFFTARqgLLxoOPNQFXHxUOo9vMXH2pmDN469VgbQkV-JjRtCevZJsbvS8vbfUtasN83xN25tX6_S5U)

Then select the “IMS via API Gateway” option

![](https://lh7-us.googleusercontent.com/uPLiiLHp6Z3jPCzYBOzHVuI8sGY5XQuUfv66fZYH0HndSBL7yvzFHh3lJjEMxteJfXsVMhUe3U_38xZHDRFSn0jeiMZUQBJJLzZ2oaIQAixY7wUPd6D0PJwg7wvC8XBeZxPmjNoiUvP3ImoG_aOhFmY)

![](https://lh7-us.googleusercontent.com/VhyMDEuglPfxeX-3cATu6ZFB_Mz2Y7C-yJ99EvBvrhD8IoVzGd4ksjrWAE0mIPub2PX5_Zua10ZHQeWI82QbJ8ZgJKN-tVpVrYGvMdfQOj3Uco5efsPT6JYkDyPu_lkeR9aTGhh5-q2bzZztXuTUixM)

You will be taken to the above screen where you must now fill in the necessary information, the name should be something like “DocBits\_export” or similar.

For “ION API Client ID” you enter the same Client ID you obtained earlier for the ION Mapping File.

Then select the Document tab of the Connection Point creation menu and add the following documents by pressing the “+” sign, this will only become useful later.

![](https://lh7-us.googleusercontent.com/GtHlTliePV-JIDLP9YNGlXELKuWIU2VSlUt4mvWO4q_XM54MSL9zTmtxPMdeOl24VFtNC0pQ-nbXyHb9PaeMkKvgzpCOo5kLdL3A8Bw54ILniwIdTyfxFhPuzRUGKs2hRi5ioKvfkdsPMgq4x6EHOtM)

Once you save this Connection Point you will obtain the Logical ID as shown below

![](https://lh7-us.googleusercontent.com/P7cihsQT2Qcq_XGL08dTV2jHMUK7YCMQyXsJudkVDXDh73GZ-hS61IoAKSHptPyX4C5e_xPKP0yZGzpQOwCFw6BppPlzZuFWZ_VGIrOUmJH2egxaCEXMoVBHBM6lkZeb3gPYWYdMYpuNqFFPC-4Qol0)

Then insert this Logical ID into the appropriate section of the BOD Mapping File and save the file.

## Upload File to DocBits

Drag and drop the file into your export configuration in DocBits. This is available at Settings → Export.

![](https://lh7-us.googleusercontent.com/AqCo7QgC-kaAxbaIJD8MYeKGLBXbwGVJPGx9_2yfUp3R2MYxJPowVAjnO80uxQ9qMDxNoXy1eY3WH-mEpaeWwatwi91edm_0lS9Hg93FSAjQGtDAR5y7Ptce-ARfetSiXIBJKiGwujSggVXXHUhG77U)
