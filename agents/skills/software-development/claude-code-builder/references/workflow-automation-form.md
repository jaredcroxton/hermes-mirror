# Workflow Automation Form Pattern

## When to use
Jared asks for a form that connects to Zapier to trigger multi-step automations (Gmail + Calendar + Google Docs, or similar). The form is a planning/bridge artifact — self-contained HTML that POSTs to a Zapier catch webhook.

## Pattern overview

1. Self-contained HTML file with all CSS/JS inline
2. Form fields with validation
3. Dropdown logic that resolves downstream targets (e.g. role + market → manager)
4. On submit: validates, shows summary panel with payload preview
5. Summary panel has three buttons: Send to Zapier, Copy payload, Close
6. Send button POSTs to Zapier webhook with loading/success/error states
7. Webhook URL is a placeholder — Jared swaps it after connecting work accounts

## CSS classes needed

- `.btn-send` — lime filled button matching `.btn-submit` style
- `.btn-send:disabled` — greyed out while sending
- `.zapier-status` — monospace status text below buttons
- `.zapier-status.loading` / `.success` / `.error` — colour-coded states

## JavaScript pattern

```js
document.getElementById('btnSendZapier').addEventListener('click', function () {
  var btn = document.getElementById('btnSendZapier');
  var statusEl = document.getElementById('zapierStatus');
  var webhookURL = 'https://hooks.zapier.com/hooks/catch/PLACEHOLDER/';

  btn.disabled = true;
  btn.textContent = 'Sending...';
  statusEl.className = 'zapier-status loading';
  statusEl.textContent = 'Sending to Zapier...';

  fetch(webhookURL, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: payloadJSON
  })
  .then(function (response) {
    if (response.ok) {
      statusEl.className = 'zapier-status success';
      statusEl.textContent = 'Sent successfully.';
      btn.textContent = 'Sent';
    } else {
      throw new Error('HTTP ' + response.status);
    }
  })
  .catch(function (err) {
    statusEl.className = 'zapier-status error';
    statusEl.textContent = 'Send failed: ' + err.message + '.';
    btn.disabled = false;
    btn.textContent = 'Retry';
  });
});
```

## Payload structure

Standard JSON payload with all form fields plus resolved manager/calendar data. The Zapier catch hook parses this and routes to Gmail, Calendar, and Google Docs actions.

## Pitfalls

- Never hardcode real email addresses or calendar IDs — these are TBC placeholders until Jared connects work accounts
- The summary panel must show the full payload so the team member can review before sending
- Always include Copy payload as a fallback in case Zapier is not yet connected
- Webhook URL is always a placeholder — remind Jared to swap it

## Example build

`phone-screen-form.html` — Phone Screen Workflow for Accor Plus APAC TA team. Role + Market dropdowns resolve hiring manager. Form submits to Zapier which creates Gmail draft, calendar booking, and Google Doc.
