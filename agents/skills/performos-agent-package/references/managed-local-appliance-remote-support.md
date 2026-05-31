# Managed local appliance remote support model

Use this when Jared asks how PerformOS can maintain, edit, troubleshoot, or support Hermes agents after a PerformOS-owned Mac/local appliance is placed in a client office.

## Strategic rule

Do not position the product as "client systems running from Jared's home Mac or home Wi-Fi." That is not enterprise credible.

Position it as:

> The appliance is installed in the client's approved environment and remotely maintained by PerformOS through a secure, auditable admin channel. No public inbound access is required.

## Deployment models

### Local Appliance

Best for privacy-led clients.

- PerformOS owns the appliance
- Client hosts it in an approved office, IT room, or managed environment
- Client controls physical location, power, network approval, and access policy
- PerformOS controls software configuration, Hermes profiles, agent updates, support, and monitoring
- Contract must cover custody, damage/loss, return, wipe, and recovery

### Private Cloud

Best for clients who will not host hardware.

- Hosted in AWS or similar dedicated private cloud environment
- Easier procurement and uptime story
- Weaker than local appliance for "data stays in your building" positioning
- Stronger than a home-hosted Mac story

### Hybrid

Best mature model.

- Client-site appliance performs sensitive/local work
- Cloud control layer handles monitoring, update queue, status dashboards, and support coordination
- Cloud layer must not become the hidden AI brain unless the client explicitly approves cloud processing

## Editing Hermes agents after shipping the Mac

Use three layers.

### 1. Secure remote admin access

Preferred starter pattern:
- Tailscale, client-approved VPN, or Cloudflare Zero Trust
- SSH key access only
- no public inbound ports
- no shared passwords
- client can revoke access

Example admin actions:

```bash
ssh performos@client-appliance
hermes --profile laralearning gateway status
hermes --profile laralearning gateway restart
hermes --profile laralearning chat -q "Reply exactly LARA_OK" --quiet
```

### 2. Git-backed agent configuration

Agent source should live in a private PerformOS-controlled repo, not only on the client Mac.

Suggested structure:

```text
performos-client-[client]/
  agents/
    lara/SOUL.md
    harry/SOUL.md
    polly/SOUL.md
  skills/
  config/
  scripts/deploy.sh
```

Update flow:
1. Edit source file in repo
2. Commit and push
3. SSH to client appliance or trigger approved deploy
4. Pull repo
5. Run deploy script
6. Restart affected Hermes profile
7. Verify with a one-shot profile probe

### 3. Cloud control layer

Lightsail or another small cloud server can support:
- device health checks
- update queue
- support ticket intake
- deployment status
- audit logs
- agent status
- failed-run alerts

Keep the wording clear: cloud control layer, not cloud AI brain.

## Support operating model

Customer-facing support path:

1. Client reports issue through support bot or dashboard button
2. System captures agent name, time, user, run ID, error/output, and nearby logs
3. PerformOS diagnoses remotely from logs first
4. If needed, client approves temporary support window
5. PerformOS fixes and verifies
6. Change and outcome are logged

## Support levels

### Level 1: User issue
- unclear prompt
- wrong expectation
- bad source file
- missing information

Handle with guidance. No remote admin needed.

### Level 2: Agent issue
- wrong format
- missing template
- stale skill
- SOUL update needed

Handle through Git-backed config update, profile restart, and verification prompt.

### Level 3: System issue
- bot offline
- gateway stopped
- disk full
- model unavailable
- appliance offline

Handle through remote admin, logs, restart, resource checks, or client IT escalation.

### Level 4: Integration issue
- Google/Zapier token expired
- CRM permission changed
- email/calendar scope revoked

Handle with client-side re-auth or integration owner approval.

## Minimum product requirements before selling

- MDM enrolled before shipping: Jamf, Kandji, Mosyle, JumpCloud, Intune, or similar
- FileVault enabled
- dedicated PerformOS admin account
- SSH key access only
- remote wipe/recovery process
- Git-backed agent configs
- deploy script with rollback
- profile restart and verification process
- support bot or Report issue button
- run logs and health checks
- client-approved remote support process

## Customer-facing phrase

> Support is built into the appliance. Every agent has issue reporting, run logs, and a controlled escalation path. Remote access is temporary, controlled, and auditable.

## Pitfalls

- Do not say "I can remote into the Mac whenever I need." Say updates are deployed through a controlled change process with client-approved remote admin access.
- Do not make screen sharing the primary support model. It feels amateur and does not scale.
- Do not store the only copy of agent definitions on the client appliance. Use Git for version control and rollback.
- Do not blur ownership. Client controls environment and approval. PerformOS owns and maintains the appliance.
