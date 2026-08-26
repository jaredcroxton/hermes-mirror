# Google Maps / Android wrong caller ID label

## Session pattern

Jared asked why his mobile number was showing as **Marketing Express**. He clarified it appeared on Android and seemed linked to Google Maps. A later clue was an old address: **36 Forsayth Lane** with postcode remembered as **4556**.

## What was checked

Public searches were run for the number in compact and spaced formats, with and without the business label and Google Maps terms. No clean public web result tied Jared's number to the business label.

A direct Google Maps search for the number did not show a public business result from the agent side.

Searching Google Maps for **Marketing Express + 36 Forsayth Lane + postcode** did surface a live **Marketing Express** listing.

## Listing found

Google Maps result found:

- Business: **Marketing Express**
- Category: Corporate office
- Visible address: **7-9 Brown Beech Dr, Flagstone QLD 4280**
- Visible phone: **0412 882 640**
- Website: `marketingexpress.com`
- Google Maps place ID-style path included `/g/11c5653n01`
- Plus code shown: `6X25+R7 Flagstone, Queensland`

The visible listing did **not** show Jared's number, but Android could still be using stale Google caller ID data linked to the same business identity.

## Address nuance

OpenStreetMap/Nominatim resolved **Forsayth Lane** to Maroochydore / Sunshine Coast, QLD 4558, not 4556. Treat that as a search variant issue, not a debate with Jared. Use it to broaden searches only.

## Reasoning

Because the label appeared on Android and Jared connected it to Google Maps, the likely source was not Jared's handset. It was likely a Google Maps / Google Business Profile / Google Phone caller ID association.

Important nuance: Google's Android caller ID can surface business labels that are not obvious in public web search or a normal Maps search. A business name plus old address query can reveal a listing even when phone-number searches fail.

## Recommended user-facing path

Tell Jared to use the Android phone where the issue appears:

1. Open Google Maps.
2. Search the wrong business name and old address together.
3. Open the matching listing.
4. Tap **Suggest an edit**.
5. Choose **Change name or other details**.
6. Remove or correct the phone number if his number appears on that device.
7. Submit.

Also check Android Phone recents:

1. Open Phone.
2. Tap the call.
3. Open Details.
4. Use **Report inaccurate caller ID**, **Not this business**, **Suggest an edit**, or similar wording.

If Jared owns the business profile, use `business.google.com` to edit the profile directly.

## Wording that worked

"This is probably not your phone doing something weird. It is a Google identity problem attached to the number. Android often pulls caller ID labels from Google Maps or Google's caller ID database."

"The visible listing now shows a different number, but Android may still have your number associated in Google's caller ID layer."

## Avoid

- Do not claim a public listing shows Jared's number if it does not.
- Do not stop at number-only searches when Jared provides an address.
- Do not recommend changing the number before attempting listing/database correction.
- Do not over-explain caller ID infrastructure when Jared needs the fix path.
