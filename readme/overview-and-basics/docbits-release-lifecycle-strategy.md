# DocBits Release Lifecycle Strategy

DocBits uses two release channels, **VESTA** and **NOVA**, to introduce new releases and give your organization time to evaluate them before adoption. During parallel production, you choose whether and when to switch to the new release. FELLOWPRO then manages the rollover that makes it the common production release for all customers.

The version numbers in this guide—R1.0.x, R1.1.x, and R1.2—are illustrative. The same lifecycle repeats with successive releases; `x` represents updates within a release series.

## Release channels

| Channel | Role in the lifecycle |
| --- | --- |
| **VESTA** | Provides the current production release. |
| **NOVA** | Provides the next release as it progresses through development, testing, and production availability. During parallel production, NOVA and VESTA both offer live production releases. |

## Lifecycle overview

![DocBits VESTA and NOVA three-phase release lifecycle](docbits-release-lifecycle-strategy.png)

Each cycle consists of three phases. A FELLOWPRO-managed rollover then brings the NOVA production release into VESTA and starts the next cycle.

| Phase | VESTA | NOVA | What this means for your organization |
| --- | --- | --- | --- |
| **1. Development** | R1.0.x in production | R1.1 in development | Continue using VESTA while the next release is prepared. |
| **2. QA and acceptance testing** | R1.0.x in production | R1.1 in QA and UAT | Evaluate the upcoming release in the NOVA sandbox while production work continues on VESTA. |
| **3. Parallel production** | R1.0.x in production | R1.1.x in production | Remain on VESTA or independently switch to NOVA when ready. |

After the rollover, all customers use VESTA R1.1.x, and NOVA is recycled for development of R1.2. Phase 1 begins again with these updated versions.

### Phase 1 — Development

VESTA provides the current production release, R1.0.x, while the next release, R1.1, is developed in NOVA. Your organization continues its day-to-day work on VESTA throughout this phase.

### Phase 2 — QA and acceptance testing

The upcoming NOVA release progresses through quality assurance (QA) and user acceptance testing (UAT). You can evaluate it in the NOVA sandbox to assess how the changes fit your organization's workflows and prepare for adoption.

VESTA R1.0.x remains the production release during this phase. You can switch to NOVA for production use once it becomes available in Phase 3.

### Phase 3 — Parallel production

VESTA R1.0.x and NOVA R1.1.x are both live production releases. Your organization decides whether and when to switch to NOVA, based on your needs and the results of your sandbox evaluation.

To adopt NOVA during this phase:

1. Evaluate the release in the NOVA sandbox.
2. Decide when your organization is ready to use it in production.
3. Switch from VESTA to NOVA using the **Release Channel** setting in the DocBits application.

This switch is self-service. FELLOWPRO does not select which customers should move to NOVA. You may continue using VESTA throughout parallel production and adopt the new release through the subsequent rollover.

## Release rollover and the next cycle

When the NOVA release is ready to become the common production release, FELLOWPRO manages the rollover:

**NOVA R1.1.x → VESTA R1.1.x**

### Advance announcement

FELLOWPRO announces the planned rollover to all customers in advance by email. The announcement invites you to contact FELLOWPRO with any concerns or objections so they can be discussed before the transition.

### What changes at rollover

| Change | Outcome |
| --- | --- |
| **The NOVA release becomes the VESTA release** | R1.1.x becomes the common production release in VESTA for all customers. |
| **The previous release is retired** | R1.0.x is decommissioned and is no longer available through either channel or by any other means. |
| **NOVA is recycled for the next release** | Development of R1.2 begins in NOVA, starting Phase 1 of the next cycle. |

The same three phases then repeat with the new version numbers.

### Release cadence

The cycle is expected to repeat approximately every **3–4 months**, subject to release readiness. This cadence is indicative, rather than a fixed schedule or guaranteed release date. FELLOWPRO announces each planned rollover in advance.

## Responsibilities and customer choice

| Transition | Who manages it | What to expect |
| --- | --- | --- |
| **Switch from VESTA to NOVA during Phase 3** | Your organization | Evaluate NOVA in the sandbox and choose whether and when to switch using the application's Release Channel setting. |
| **Roll over NOVA R1.1.x into VESTA R1.1.x** | FELLOWPRO | Receive an advance email announcement, raise any concerns or objections, and prepare for the new common production release and retirement of R1.0.x. |

## Frequently asked questions

### Can we remain on VESTA while NOVA is available in production?

Yes. During Phase 3, you may remain on VESTA or switch to NOVA when your organization is ready. At the subsequent rollover, the new release becomes VESTA and the previous release is retired.

### How do we switch to NOVA?

Once NOVA is available in production, use the **Release Channel** setting in the DocBits application. Your organization makes this choice independently, based on its needs and evaluation of the release in the NOVA sandbox.

### When is NOVA available for production use?

NOVA becomes a live production release in Phase 3, after development and QA/UAT. During this phase, VESTA and NOVA run in production in parallel with different software versions.

### How will we know about the rollover, and can we raise objections?

FELLOWPRO emails all customers in advance of the planned rollover. You are invited to contact FELLOWPRO with any concerns or objections to discuss before the transition.

### Can we continue using R1.0.x after the rollover?

No. R1.0.x is decommissioned at rollover and is no longer available through either channel or by any other means. R1.1.x becomes the common VESTA production release for all customers.

### How does the rollover differ from our switch to NOVA?

Your switch to NOVA during Phase 3 is a self-service choice about when to adopt the new production release. The rollover is the subsequent transition managed by FELLOWPRO: NOVA R1.1.x becomes VESTA R1.1.x, the previous release is retired, and the next cycle begins.

### What happens to NOVA after the rollover?

NOVA is recycled for development of the next release, R1.2 in this example. VESTA provides R1.1.x while NOVA progresses through development, QA/UAT, and parallel production again.

### Is a new release guaranteed every three to four months?

No. The approximate 3–4 month cadence depends on release readiness. FELLOWPRO communicates the planned rollover in advance for each cycle.
