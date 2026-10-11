# DocBits Release Lifecycle Strategy

DocBits uses two release channels—**VESTA** and **NOVA**—to introduce new functionality while giving customers flexibility in adopting upcoming releases.

> **Illustrative versions:** Release numbers **R1.0.x**, **R1.1.x**, and **R1.2** in this guide are examples only. They do not limit the releases to which this strategy applies. The lifecycle repeats with successive versions, following the same principles.

## Release channels

| Channel | Purpose |
|---|---|
| **VESTA** | The current production release channel. |
| **NOVA** | The channel used to prepare and introduce the next release. During the parallel-production phase, NOVA is also a live production release channel. |

VESTA and NOVA are **release channels**, not indicators of release quality. Both can operate in production at the same time with different software versions.

## Lifecycle overview

| Phase | VESTA | NOVA | Customer experience |
|---|---|---|---|
| **Phase #1 — VESTA Production + NOVA Development** | **R1.0.x** in production | **R1.1** in development | Customers use VESTA while the next release is developed. |
| **Phase #2 — VESTA Production + NOVA QA and UAT** | **R1.0.x** in production | **R1.1** in QA and UAT | The upcoming NOVA release undergoes testing and acceptance activities. |
| **Phase #3 — NOVA Gradual Client Rollout / Parallel VESTA & NOVA Operation** | **R1.0.x** in production | **R1.1.x** in production | Both channels are live; customers can evaluate NOVA and independently switch when ready. |
| **Phase #1 (New Release Cycle)** | **R1.1.x** in production | **R1.2** in development | Following rollover, the lifecycle begins again with updated versions. |

### Phase #1 — VESTA Production + NOVA Development

VESTA continues to provide the current production release (**R1.0.x**) while the next release (**R1.1**) is developed in NOVA. Customers continue using VESTA throughout this phase.

### Phase #2 — VESTA Production + NOVA QA and UAT

The upcoming NOVA release (**R1.1**) progresses through **Quality Assurance (QA)** and **User Acceptance Testing (UAT)**. VESTA (**R1.0.x**) remains the production channel. Customers can evaluate the upcoming NOVA release in the NOVA sandbox before considering a switch once it becomes available in production.

### Phase #3 — NOVA Gradual Client Rollout and Parallel VESTA & NOVA Operation

NOVA (**R1.1.x**) becomes available as a production release alongside VESTA (**R1.0.x**). **Both release channels run live in production.**

Each customer can evaluate NOVA in its sandbox environment and **switch from VESTA to NOVA independently**, based on their needs and NOVA sandbox testing results, using the **Release Channel** setting in the DocBits application.

**During this phase, switching is the customer's choice.** FELLOWPRO does not select which customers should switch to NOVA.

## New release cycle: rollover and recycle

When the NOVA release is ready to become the common production release, **FELLOWPRO manages the release-channel rollover**.

Before the rollover, **FELLOWPRO informs all customers in advance by email** about the planned transition. Customers with concerns or objections are invited to contact FELLOWPRO to discuss them.

The transition has four steps:

1. **Rollover — NOVA → VESTA:** The release currently running in **NOVA (R1.1.x)** becomes the release running in **VESTA (R1.1.x)**.
2. **Retire the superseded release:** The previous **R1.0.x** release is **decommissioned and no longer available by any means**.
3. **Recycle NOVA:** The NOVA channel becomes available for development of the next release, **R1.2**.
4. **Restart at Phase #1:** All customers use **VESTA R1.1.x**, while **NOVA R1.2** enters development.

**Important:** R1.2 is **not** copied into VESTA during this rollover. It is the *next* release to be developed in NOVA after **NOVA R1.1.x → VESTA R1.1.x**.

### Release cadence

The cycle is expected to repeat approximately **every three to four months**, subject to release readiness. This is an indicative interval, not a guaranteed release date.

## Who controls each transition?

| Transition | Controlled by | What happens |
|---|---|---|
| **VESTA → NOVA during Phase #3** | **Customer** | The customer evaluates NOVA and can switch independently using the in-app Release Channel setting. |
| **NOVA → VESTA at the new-cycle rollover** | **FELLOWPRO** | FELLOWPRO announces the planned rollover to all customers in advance, invites concerns or objections, and manages the transition. |

## Common questions

### Can I remain on VESTA while NOVA is available in production?

**Yes.** During Phase #3, both channels are available in production. You can remain on VESTA or switch to NOVA when it suits your organization.

### Who decides when we switch to NOVA?

**You do.** During Phase #3, each customer can independently switch through the application's **Release Channel** setting, based on their needs and evaluation of NOVA in the sandbox.

### Is NOVA a production release channel?

**Yes.** In Phase #3, VESTA and NOVA are both live production release channels.

### Will we be informed before the rollover?

**Yes.** FELLOWPRO will announce the planned rollover to all customers in advance by email and invite customers to contact the team with any concerns or objections.

### What happens to the old R1.0.x release after rollover?

Once **NOVA R1.1.x** is rolled over into **VESTA R1.1.x**, the old **R1.0.x** release is **decommissioned**. It will no longer be available through either channel or by any other means. NOVA is then recycled for the next release, **R1.2**.

### Is the rollover the same as my voluntary switch to NOVA?

**No.** Your switch during Phase #3 is self-service and customer-controlled. The subsequent **NOVA → VESTA** rollover is a release-cycle transition managed by FELLOWPRO and communicated to all customers in advance.

### What happens after the new cycle begins?

The process repeats: **VESTA R1.1.x** is the production release, **NOVA R1.2** enters development, then QA/UAT, then parallel production. Subsequent release cycles follow the same pattern with newer version numbers.
