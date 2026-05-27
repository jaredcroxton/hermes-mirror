# Bob_Builder Task — PerformOS Course Page Deploy

## Task

Deploy the rebuilt PerformOS course page. The complete HTML is inside `02-course-code.md` in the ```html code block at the bottom of that file.

## Steps

1. Open `build/02-course-code.md`
2. Copy everything inside the ```html code block (lines 50 to 1037)
3. Save as `/Users/jc/Desktop/Website - PerformOS/course.html`
4. Deploy:
```bash
cd "/Users/jc/Desktop/Website - PerformOS"
vercel --prod --yes
```

## What this build contains

Self-contained course page — 981 lines. All CSS inline. All JS embedded. No external dependency except Google Fonts and GA4.

15-beat structure informed by competitor research on 8 AI education sites. Fully Option B compliant (instructor-credential framing, mandatory disclaimers, trademark attribution).

## Post-deploy verification (10 checks)

1. [ ] Hero: "Your personal AI tutor. 12 weeks. Career-ready."
2. [ ] Trust ribbon: 12 / 1-on-1 / $499 / Certificate
3. [ ] Problem section: "Most AI courses treat you like everyone else"
4. [ ] Instructor: Jared Croxton + AI-900 + AI-102 + inline disclaimer
5. [ ] Curriculum: 4 phases with specialisation tracks
6. [ ] Certificate mockup: no third-party marks
7. [ ] Disclosure block present below pricing
8. [ ] FAQ: "Is this a Microsoft-certified course?" + "Why doesn't the certificate say Microsoft or Azure?"
9. [ ] Footer: trademark attribution
10. [ ] All CTAs link to `contact.html?topic=12-Week%20Course`

## Strategy context (from Brock)

- **Research:** 8 competitor sites analysed. Nobody shows pricing → $499 upfront is differentiation. Instructor credentials underutilised → Microsoft certs as trust anchor. "Personalised" is vacant positioning → made it the headline.
- **Legal:** Option B per Atticus_Counsel. Instructor credentials in body text only. No third-party marks on certificate. Mandatory negative disclosure. Trademark attribution in footer.
- **Full strategy docs:** `/Users/jc/Desktop/Obsidian/PerformOS/website-build/`
