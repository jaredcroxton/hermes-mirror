---
name: caller-id-business-listing-correction
description: "Use when Jared asks why a phone number shows the wrong business name on Android, iPhone, Google Phone, Google Maps, caller ID, Truecaller, Hiya, Samsung Smart Call, or business listings, and wants to correct or remove the label."
version: 1.0.0
author: Brock / Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [caller-id, google-maps, google-business-profile, android, phone-number, business-listing, privacy]
    related_skills: [google-workspace, maps, domain-dns-debugging]
---

# Caller ID and Business Listing Correction

## Trigger

Use this skill when Jared asks why his number shows as the wrong business, brand, spam label, or caller ID name.

Common phrasing:
- "why does my phone number come up as X"
- "it's showing on Android"
- "something to do with Google Maps"
- "my number is attached to a business"
- "how do I remove my number from Google"
- "wrong caller ID"

## First principle

Do not assume the label is coming from Jared's device. Caller ID labels usually come from external data sources:

- Google Maps / Google Business Profile
- Google Phone caller ID and spam database
- Samsung Smart Call
- Hiya
- Truecaller
- carrier CNAM/business caller ID systems
- someone else's saved contact
- old business listings or scraped directories

## Investigation sequence

### 1. Check whether the label is public

Run searches for the number in multiple formats:

```text
"0400598141"
"0400 598 141"
"0400598141" "Business Name"
"0400 598 141" "Business Name"
"0400 598 141" "Google Maps"
"0400598141" "Google Maps"
```

If no public result appears, say so clearly. Do not overstate the finding. A missing web result does not prove Google has no private/internal caller ID association.

### 1b. Search by business name plus old address

If Jared gives an old business address, search Google Maps directly with the combined string, not just the phone number. Hidden or stale Maps associations may surface only when the business name and old address are queried together.

Useful variants:

```text
Business Name + old street address + postcode
Business Name + old street address + suburb
Business Name + old street name + state
Business Name + current visible phone number, if found
```

Open the Maps result and extract the visible details: current address, category, website, phone, plus code/place ID, and Maps link. Compare the visible phone with Jared's number. If they differ, explain that Android may be using stale Google caller ID data even when the public listing now shows a different number.

### 2. Test whether it is one phone or a database

Ask Jared to test the number on two or three phones:

- one iPhone
- one Android
- one person who has never saved the number

Decision logic:

- Only one person sees the wrong label: likely their contacts or local phone cache.
- Multiple Android phones see it: likely Google Phone / Google Maps / Samsung / Hiya database.
- Multiple platforms see it: likely carrier CNAM, Truecaller/Hiya, or business listing data syndicated widely.

### 3. If Android is involved, prioritise Google Maps and Google Phone

Android often surfaces business identity from Google Maps and Google Business Profile data.

Tell Jared to check on the Android phone where it appears:

1. Open Google Maps.
2. Search the wrong business name.
3. Open matching listings.
4. Tap **Suggest an edit**.
5. Choose **Change name or other details**.
6. Edit or remove the phone number.
7. Submit.

Also check the Android Phone app:

1. Open Phone.
2. Go to Recents.
3. Tap the call.
4. Open Details.
5. Look for **Report inaccurate caller ID**, **Not this business**, **Suggest an edit**, or **Report spam / not spam**.

Wording varies by Android model.

### 4. If Jared owns or can access the profile

Use Google Business Profile:

```text
business.google.com
```

Steps:

1. Search for or select the business profile.
2. Edit contact details.
3. Remove or replace the incorrect phone number.
4. Save.
5. Recheck after Google's update window.

## Explanation to use with Jared

Keep it plain:

- "This is probably not your phone doing something weird."
- "It is a data identity problem attached to the number."
- "Android often pulls business labels from Google Maps or Google's caller ID database."
- "If multiple Android phones show it, we fix the listing/database, not your handset."

## Correction targets

When the source is unclear, give Jared a short ordered list:

1. Google Maps listing correction via Suggest an edit.
2. Android Phone app inaccurate caller ID report.
3. Google Business Profile edit if he owns or can access it.
4. Truecaller unlist/correction.
5. Hiya correction request.
6. Carrier support if the label appears across many platforms.

## Pitfalls

1. **Do not claim the number is publicly listed if searches are empty.** Say the public web did not show a clean match.
2. **Do not confuse Google Maps public search with Google's internal caller ID database.** Android may show a label that is not visible in a normal Maps search.
3. **Do not stop at phone-number search.** If Jared gives an old address, search Maps for the business name plus address. Google may surface the listing even when number searches fail.
4. **Check postcode/suburb variants.** Australian street/postcode memories can be off by one suburb or postcode; verify the street with a geocoder but avoid making the correction the main point unless it changes the fix path.
5. **Do not tell Jared to change his number first.** Fix the listing/database first.
6. **Do not ask too many questions.** One useful question is enough: where does the label appear?
7. **Do not expose or repeat personal phone numbers unnecessarily in final outputs.** Use the number only when needed for exact search/correction context.

## Reference notes

See `references/google-maps-android-wrong-caller-id.md` for the 26 August 2026 session pattern and wording.