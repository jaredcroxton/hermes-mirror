# Deploy Instructions

## What you're deploying

The new `course.html` — a 15-beat, Option B compliant course page for the PerformOS 12-week AI course.

## Prerequisites

- Vercel CLI installed (`vercel --version` — should return v53+)
- Vercel CLI authenticated to your account
- Access to the GitHub repo: `jaredcroxton/performos-com-au`

## Method 1: Vercel CLI direct deploy (fastest)

```bash
cd "/Users/jc/Desktop/Website - PerformOS"

# Make sure the new course.html is in place
# (copy it from the build folder if needed)
cp "/Users/jc/Desktop/performos-course-build/build/02-course.html" course.html

# Deploy directly to production
vercel --prod --yes
```

This bypasses git entirely. Vercel uploads the files from disk and deploys. Takes about 8 seconds.

After deploy, Vercel outputs the deployment URL and aliases it to performos.com.au.

## Method 2: Git push (triggers auto-deploy)

```bash
cd "/Users/jc/Desktop/Website - PerformOS"

# Copy the new course.html in place
cp "/Users/jc/Desktop/performos-course-build/build/02-course.html" course.html

# Commit and push
git add course.html
git commit -m "Option B: instructor-credential framing + Outlier-informed 15-beat structure"
git push origin main
```

Vercel auto-deploys on push to main.

## Post-deploy verification

After deploying, check these 10 things on the live page:

1. [ ] Hero reads "Your personal AI tutor. 12 weeks. Career-ready."
2. [ ] Trust ribbon shows 12 / 1-on-1 / $499 / ✓ Certificate
3. [ ] Problem section: "Most AI courses treat you like everyone else" with side-by-side contrast
4. [ ] Instructor section shows AI-900 and AI-102 certs with inline disclaimer
5. [ ] Curriculum shows 4 phases including "Your Specialisation Track"
6. [ ] Certificate mockup has NO Microsoft/OpenAI marks
7. [ ] Pricing section shows $499 with full inclusions list
8. [ ] Disclosure block present below pricing: "This course is not a Microsoft, OpenAI, or ChatGPT certification program"
9. [ ] FAQ includes "Is this a Microsoft-certified course?" and "Why doesn't the certificate say Microsoft or Azure?"
10. [ ] Footer has full trademark attribution

## DNS note

The apex domain `performos.com.au` has a known dual-project conflict in Vercel. If the apex domain returns 404 or errors, use the Vercel deployment URL directly (it will be printed by the deploy command, format: `https://performos-com-XXXXX-jaredcroxtons-projects.vercel.app/course`). To fix permanently, resolve the dual-project conflict in the Vercel dashboard under Domains.

## Rollback

If something goes wrong:

```bash
cd "/Users/jc/Desktop/Website - PerformOS"
git checkout HEAD~1 -- course.html
vercel --prod --yes
```

Or in the Vercel dashboard, promote the previous deployment back to production.
