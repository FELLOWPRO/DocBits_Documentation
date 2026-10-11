# DocBits Release Lifecycle Strategy

DocBits provides two release channels, **VESTA** and **NOVA**, so your organization can prepare for upcoming releases and choose when to adopt them during the parallel production phase.

Both channels are production capable. VESTA provides the current common release, while NOVA introduces the next release through development, validation, and production availability. During parallel production, the channels offer different releases at the same time.

## Lifecycle at a glance

Each release cycle follows three phases, followed by a release rollover and the start of the next cycle. The versions below are illustrative; `x` represents updates within a release series.

| Lifecycle stage | VESTA | NOVA | What this means for you |
| --- | --- | --- | --- |
| Phase 1 — Development | R1.0.x in production | R1.1 in development | Continue using VESTA while the next release is prepared. |
| Phase 2 — QA and acceptance testing | R1.0.x in production | R1.1 in quality assurance and user acceptance testing | Evaluate the upcoming release in the NOVA sandbox while continuing production work on VESTA. |
| Phase 3 — Parallel production | R1.0.x in production | R1.1.x in production | After sandbox evaluation, choose whether and when to switch to NOVA through the application's release-channel setting. |
| Release rollover | R1.1.x becomes the common VESTA release | R1.1.x is carried forward into VESTA | FELLOWPRO manages the rollover following advance email communication. |
| Next cycle | R1.1.x in production | R1.2 in development | The same three-phase lifecycle begins again. |

## Phase 1 — Continue on VESTA while the next release is developed

At the start of the cycle, VESTA runs the current production release, such as R1.0.x. Your organization continues its day-to-day work on this channel.

The next release, R1.1 in this example, is developed in NOVA. VESTA continues to receive maintenance updates as needed while the upcoming release is prepared.

## Phase 2 — Evaluate the upcoming release in the NOVA sandbox

The upcoming NOVA release enters quality assurance (QA) and user acceptance testing (UAT). During this phase, you can evaluate it in the NOVA sandbox and review how its changes fit your organization's workflows.

Use this evaluation to prepare your team and assess the release before choosing it for production. Your production work continues on VESTA R1.0.x throughout this phase.

Sandbox evaluation and production adoption are separate steps. Evaluating NOVA in the sandbox does not itself switch your production release channel.

## Phase 3 — Choose your production release channel

Once NOVA R1.1.x is available in production, both channels run in parallel:

- **VESTA R1.0.x** remains available for organizations continuing with the current release.
- **NOVA R1.1.x** is available for organizations ready to adopt the new release.

During this phase, your organization controls whether and when to move from VESTA to NOVA. To adopt the new release:

1. Evaluate the upcoming release in the NOVA sandbox.
2. Decide when your organization is ready to use it in production.
3. Use the application's **release-channel setting** to switch from VESTA to NOVA.

You can continue using VESTA during parallel production if you prefer to adopt the new release through the subsequent FELLOWPRO-managed rollover.

## Release rollover — NOVA becomes the next VESTA release

Following the parallel production phase, FELLOWPRO manages the release rollover. The release available through **NOVA R1.1.x becomes VESTA R1.1.x**, establishing it as the common production release for the next cycle.

The direction of this rollover is:

**NOVA R1.1.x → VESTA R1.1.x**

Before the rollover, FELLOWPRO sends an advance email announcement to all customers. The announcement invites you to contact FELLOWPRO with any concerns or objections so they can be discussed before the rollover proceeds.

This is a FELLOWPRO-managed lifecycle milestone. It is distinct from your organization's choice to switch from VESTA to NOVA during parallel production.

### Who controls each transition?

| Transition | Managed by | Purpose |
| --- | --- | --- |
| Customer rollout: switch from VESTA to NOVA during Phase 3 | Your organization, through the application's release-channel setting | Adopt the new production release after sandbox evaluation, at a time you choose during parallel production. |
| Release rollover: NOVA R1.1.x becomes VESTA R1.1.x | FELLOWPRO, following advance email communication and discussion of any objections | Make the new release the common VESTA production release and prepare for the next cycle. |

## The next release cycle

After the rollover, VESTA runs R1.1.x and NOVA is prepared for development of R1.2. The three phases repeat: development, QA and acceptance testing, and parallel production. A later rollover then carries the NOVA R1.2.x release forward into VESTA R1.2.x.

The release cycle is expected to repeat approximately every **3–4 months**, subject to release readiness. This is an indicative cadence rather than a fixed schedule; the advance rollover announcement provides the relevant information for each cycle.

## Common questions

### Are VESTA and NOVA both production channels?

Yes. Both channels are production capable, and both offer production releases during Phase 3. An upcoming NOVA release first passes through development and validation before it becomes available for production use.

### Do we need to switch to NOVA as soon as it becomes available?

No. During parallel production, you choose whether and when to switch after evaluating the release in the NOVA sandbox. You may continue using VESTA until the FELLOWPRO-managed rollover brings the new release to VESTA.

### How will we know about the rollover?

FELLOWPRO announces it in advance by email to all customers. If you have concerns or objections, contact FELLOWPRO as invited in that announcement to discuss them before the rollover.

### What happens to NOVA after the rollover?

NOVA is prepared for the next release cycle. For example, after NOVA R1.1.x becomes VESTA R1.1.x, development of R1.2 begins in NOVA.
